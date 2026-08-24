use bitcoinkernel::{
    set_script_trace_callback, unset_script_trace_callback, verify, PrecomputedTransactionData,
    ScriptPubkey, ScriptTraceFrame, Transaction, TxOut, VERIFY_ALL_PRE_TAPROOT,
};
use serde::{Deserialize, Serialize};
use std::io::{self, Read};
use std::sync::{Arc, Mutex};

const BACKEND_REVISION: &str = "691a90cc0c20761cc9b35a783e0e84c77245d555";
const MAX_SCRIPT_BYTES: usize = 10_000;

#[derive(Deserialize)]
struct Request {
    #[serde(default)]
    unlocking_script: String,
    locking_script: String,
}

#[derive(Clone, Serialize)]
struct TraceFrame {
    kind: String,
    script: String,
    opcode_pos: u32,
    opcode: String,
    executing: bool,
    op_count: i32,
    stack: Vec<String>,
    altstack: Vec<String>,
    sig_version: String,
    script_error: i32,
}

impl From<ScriptTraceFrame> for TraceFrame {
    fn from(frame: ScriptTraceFrame) -> Self {
        Self {
            kind: format!("{:?}", frame.kind).to_lowercase(),
            script: hex::encode(frame.script),
            opcode_pos: frame.opcode_pos,
            opcode: format!("0x{:02x}", frame.opcode),
            executing: frame.exec,
            op_count: frame.op_count,
            stack: frame.stack.into_iter().map(hex::encode).collect(),
            altstack: frame.altstack.into_iter().map(hex::encode).collect(),
            sig_version: format!("{:?}", frame.sig_version),
            script_error: frame.script_error,
        }
    }
}

#[derive(Serialize)]
struct Response {
    backend: &'static str,
    backend_revision: &'static str,
    consensus_engine: &'static str,
    consensus_compatible: bool,
    verification_flags: &'static str,
    synthetic_transaction: bool,
    success: bool,
    stack: Vec<String>,
    trace: Vec<TraceFrame>,
    error: Option<String>,
}

impl Response {
    fn error(message: impl Into<String>) -> Self {
        Self {
            backend: "rust-bitcoinkernel",
            backend_revision: BACKEND_REVISION,
            consensus_engine: "Bitcoin Core libbitcoinkernel",
            consensus_compatible: true,
            verification_flags: "VERIFY_ALL_PRE_TAPROOT",
            synthetic_transaction: true,
            success: false,
            stack: Vec::new(),
            trace: Vec::new(),
            error: Some(message.into()),
        }
    }
}

fn opcode(name: &str) -> Option<u8> {
    match name {
        "OP_0" | "OP_FALSE" => Some(0x00),
        "OP_1NEGATE" => Some(0x4f),
        "OP_1" | "OP_TRUE" => Some(0x51),
        "OP_2" => Some(0x52),
        "OP_3" => Some(0x53),
        "OP_4" => Some(0x54),
        "OP_5" => Some(0x55),
        "OP_6" => Some(0x56),
        "OP_7" => Some(0x57),
        "OP_8" => Some(0x58),
        "OP_9" => Some(0x59),
        "OP_10" => Some(0x5a),
        "OP_11" => Some(0x5b),
        "OP_12" => Some(0x5c),
        "OP_13" => Some(0x5d),
        "OP_14" => Some(0x5e),
        "OP_15" => Some(0x5f),
        "OP_16" => Some(0x60),
        "OP_VERIFY" => Some(0x69),
        "OP_RETURN" => Some(0x6a),
        "OP_DEPTH" => Some(0x74),
        "OP_DROP" => Some(0x75),
        "OP_DUP" => Some(0x76),
        "OP_OVER" => Some(0x78),
        "OP_SWAP" => Some(0x7c),
        "OP_SIZE" => Some(0x82),
        "OP_EQUAL" => Some(0x87),
        "OP_EQUALVERIFY" => Some(0x88),
        "OP_ADD" => Some(0x93),
        "OP_SUB" => Some(0x94),
        "OP_BOOLAND" => Some(0x9a),
        "OP_BOOLOR" => Some(0x9b),
        "OP_NUMEQUAL" => Some(0x9c),
        "OP_LESSTHAN" => Some(0x9f),
        "OP_GREATERTHAN" => Some(0xa0),
        "OP_SHA256" => Some(0xa8),
        "OP_HASH160" => Some(0xa9),
        _ => None,
    }
}

fn encode_script_num(value: i64) -> Vec<u8> {
    if value == 0 {
        return Vec::new();
    }
    let negative = value < 0;
    let mut absolute = value.unsigned_abs();
    let mut output = Vec::new();
    while absolute > 0 {
        output.push((absolute & 0xff) as u8);
        absolute >>= 8;
    }
    let last = output.len() - 1;
    if output[last] & 0x80 != 0 {
        output.push(if negative { 0x80 } else { 0x00 });
    } else if negative {
        output[last] |= 0x80;
    }
    output
}

fn push_data(script: &mut Vec<u8>, data: &[u8]) -> Result<(), String> {
    if data.len() > 520 {
        return Err("pushed stack item exceeds Bitcoin Script's 520-byte limit".into());
    }
    match data.len() {
        0 => script.push(0x00),
        1..=75 => script.push(data.len() as u8),
        76..=255 => {
            script.push(0x4c);
            script.push(data.len() as u8);
        }
        _ => {
            script.push(0x4d);
            script.extend_from_slice(&(data.len() as u16).to_le_bytes());
        }
    }
    script.extend_from_slice(data);
    Ok(())
}

fn compile_asm(asm: &str) -> Result<Vec<u8>, String> {
    if asm.len() > MAX_SCRIPT_BYTES {
        return Err(format!("ASM input exceeds {MAX_SCRIPT_BYTES} bytes"));
    }
    let mut script = Vec::new();
    for token in asm.split_whitespace() {
        let upper = token.to_ascii_uppercase();
        if let Some(code) = opcode(&upper) {
            script.push(code);
            continue;
        }
        if let Some(hex_value) = token.strip_prefix("0x") {
            let value = hex::decode(hex_value).map_err(|error| format!("invalid hex literal {token}: {error}"))?;
            push_data(&mut script, &value)?;
            continue;
        }
        if let Some(text) = token.strip_prefix("str:") {
            push_data(&mut script, text.as_bytes())?;
            continue;
        }
        if let Ok(number) = token.parse::<i64>() {
            match number {
                -1 => script.push(0x4f),
                0 => script.push(0x00),
                1..=16 => script.push(0x50 + number as u8),
                _ => push_data(&mut script, &encode_script_num(number))?,
            }
            continue;
        }
        return Err(format!("unsupported ASM token: {token}"));
    }
    if script.len() > MAX_SCRIPT_BYTES {
        return Err(format!("compiled script exceeds {MAX_SCRIPT_BYTES} bytes"));
    }
    Ok(script)
}

fn compact_size(value: usize, output: &mut Vec<u8>) {
    if value < 253 {
        output.push(value as u8);
    } else if value <= u16::MAX as usize {
        output.push(253);
        output.extend_from_slice(&(value as u16).to_le_bytes());
    } else {
        output.push(254);
        output.extend_from_slice(&(value as u32).to_le_bytes());
    }
}

fn synthetic_transaction(script_sig: &[u8]) -> Vec<u8> {
    let mut transaction = Vec::new();
    transaction.extend_from_slice(&2i32.to_le_bytes());
    transaction.push(1); // input count
    transaction.extend_from_slice(&[0u8; 32]);
    transaction.extend_from_slice(&u32::MAX.to_le_bytes());
    compact_size(script_sig.len(), &mut transaction);
    transaction.extend_from_slice(script_sig);
    transaction.extend_from_slice(&u32::MAX.to_le_bytes());
    transaction.push(1); // output count
    transaction.extend_from_slice(&0i64.to_le_bytes());
    transaction.push(1);
    transaction.push(0x6a); // OP_RETURN
    transaction.extend_from_slice(&0u32.to_le_bytes());
    transaction
}

fn evaluate(request: Request) -> Response {
    let unlocking = match compile_asm(&request.unlocking_script) {
        Ok(script) => script,
        Err(error) => return Response::error(error),
    };
    let locking = match compile_asm(&request.locking_script) {
        Ok(script) => script,
        Err(error) => return Response::error(error),
    };

    let script_pubkey = match ScriptPubkey::try_from(locking.as_slice()) {
        Ok(script) => script,
        Err(error) => return Response::error(format!("libbitcoinkernel rejected scriptPubKey: {error}")),
    };
    let raw_transaction = synthetic_transaction(&unlocking);
    let transaction = match Transaction::new(&raw_transaction) {
        Ok(transaction) => transaction,
        Err(error) => return Response::error(format!("libbitcoinkernel rejected synthetic transaction: {error}")),
    };
    let transaction_data = match PrecomputedTransactionData::new(&transaction, &Vec::<TxOut>::new()) {
        Ok(data) => data,
        Err(error) => return Response::error(format!("libbitcoinkernel precomputation failed: {error}")),
    };

    let frames: Arc<Mutex<Vec<TraceFrame>>> = Arc::new(Mutex::new(Vec::new()));
    let callback_frames = Arc::clone(&frames);
    if let Err(error) = set_script_trace_callback(move |frame: ScriptTraceFrame| {
        callback_frames.lock().expect("trace frame lock poisoned").push(frame.into());
    }) {
        return Response::error(format!("libbitcoinkernel script tracing unavailable: {error}"));
    }

    let verification = verify(
        &script_pubkey,
        Some(0),
        &transaction,
        0,
        Some(VERIFY_ALL_PRE_TAPROOT),
        &transaction_data,
    );
    unset_script_trace_callback();

    let trace = frames.lock().expect("trace frame lock poisoned").clone();
    let stack = trace.last().map(|frame| frame.stack.clone()).unwrap_or_default();
    Response {
        backend: "rust-bitcoinkernel",
        backend_revision: BACKEND_REVISION,
        consensus_engine: "Bitcoin Core libbitcoinkernel",
        consensus_compatible: true,
        verification_flags: "VERIFY_ALL_PRE_TAPROOT",
        synthetic_transaction: true,
        success: verification.is_ok(),
        stack,
        trace,
        error: verification.err().map(|error| error.to_string()),
    }
}

fn self_test() -> bool {
    let response = evaluate(Request {
        unlocking_script: "2 3 OP_ADD".into(),
        locking_script: "5 OP_EQUAL".into(),
    });
    response.success && !response.trace.is_empty()
}

fn main() {
    let argument = std::env::args().nth(1);
    if argument.as_deref() == Some("--version") {
        println!("bitcoin-script-kernel 0.1.0 rust-bitcoinkernel {BACKEND_REVISION}");
        return;
    }
    if argument.as_deref() == Some("--self-test") {
        if self_test() {
            println!("rust-bitcoinkernel self-test ok ({BACKEND_REVISION})");
            return;
        }
        eprintln!("rust-bitcoinkernel self-test failed");
        std::process::exit(1);
    }

    let mut input = String::new();
    if let Err(error) = io::stdin().read_to_string(&mut input) {
        eprintln!("failed to read request: {error}");
        std::process::exit(2);
    }
    let response = match serde_json::from_str::<Request>(&input) {
        Ok(request) => evaluate(request),
        Err(error) => Response::error(format!("invalid request JSON: {error}")),
    };
    match serde_json::to_string(&response) {
        Ok(json) => println!("{json}"),
        Err(error) => {
            eprintln!("failed to serialize response: {error}");
            std::process::exit(2);
        }
    }
}

