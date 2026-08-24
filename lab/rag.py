"""Internal deterministic extractive-retrieval helper."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Set

from .library import SearchIndex


def _terms(text: str) -> Set[str]:
    return {term.lower() for term in re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]+", text)}


def _best_sentence(text: str, question: str) -> str:
    question_terms = _terms(question)
    sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]
    if not sentences:
        return text[:320].strip()
    ranked = sorted(
        sentences,
        key=lambda sentence: (len(_terms(sentence).intersection(question_terms)), -len(sentence)),
        reverse=True,
    )
    return ranked[0][:500]


def answer(question: str, index: SearchIndex, top_k: int = 3) -> Dict[str, Any]:
    question = question.strip()
    if not question:
        raise ValueError("question is required")
    results = index.search(question, limit=max(1, min(top_k, 8)))
    citations: List[Dict[str, Any]] = []
    extracts = []
    for result in results:
        document = index.get(result["id"])
        if document is None:
            continue
        extract = _best_sentence(document["body"], question)
        extracts.append("[{}] {}".format(document["id"], extract))
        citations.append(
            {
                "id": document["id"],
                "title": document["title"],
                "canonical_url": document["canonical_url"],
                "extract": extract,
                "checksum": document["checksum"],
            }
        )
    if not citations:
        response = "No indexed document matched the question. Add or revise library metadata, rebuild the index, and retry."
    else:
        response = "Local extractive test answer (no language model): " + " ".join(extracts)
    return {
        "question": question,
        "answer": response,
        "citations": citations,
        "mode": "local-extractive",
        "model": None,
        "grounded": bool(citations),
    }
