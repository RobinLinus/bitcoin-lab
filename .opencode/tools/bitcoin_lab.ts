import { tool } from "@opencode-ai/plugin"

const baseURL = (process.env.BITCOIN_LAB_URL ?? "http://127.0.0.1:8080/api/v1").replace(/\/$/, "")

async function call(path: string, options?: RequestInit): Promise<string> {
  const response = await fetch(`${baseURL}${path}`, options)
  const body = await response.text()
  if (!response.ok) throw new Error(`Bitcoin Research Lab ${response.status}: ${body}`)
  return body
}

export const search = tool({
  description: "Search the local Bitcoin research library by full text and optional metadata.",
  args: {
    query: tool.schema.string().describe("Full-text query; use an empty string for metadata-only search"),
    collection: tool.schema.string().optional().describe("papers, delving-bitcoin, or mailing-lists"),
    tag: tool.schema.string().optional().describe("Metadata tag or Bitcoin topic"),
    author: tool.schema.string().optional().describe("Author name fragment"),
    limit: tool.schema.number().optional().describe("Maximum results, from 1 to 50"),
  },
  async execute(args) {
    const params = new URLSearchParams({ q: args.query })
    if (args.collection) params.set("collection", args.collection)
    if (args.tag) params.set("tag", args.tag)
    if (args.author) params.set("author", args.author)
    if (args.limit) params.set("limit", String(args.limit))
    return call(`/search?${params}`)
  },
})

export const script = tool({
  description: "Evaluate unlocking and locking Bitcoin Script ASM with the configured lab backend.",
  args: {
    unlocking_script: tool.schema.string().describe("Unlocking Script in the lab ASM format"),
    locking_script: tool.schema.string().describe("Locking Script in the lab ASM format"),
  },
  async execute(args) {
    return call("/script/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(args),
    })
  },
})

export const bitcoin_status = tool({
  description: "Get chain, height, and reachability from the attached Bitcoin Core regtest node.",
  args: {},
  async execute() {
    return call("/bitcoin/status")
  },
})
