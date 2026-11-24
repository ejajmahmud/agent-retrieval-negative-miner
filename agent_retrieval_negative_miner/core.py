"""Core Hard Negative Miner implementation."""
from typing import Dict, List, Set

class NegativeSample:
    def __init__(self, doc_id: str, query: str, distractor_reason: str):
        self.doc_id = doc_id
        self.query = query
        self.distractor_reason = distractor_reason

class HardNegativeMiner:
    def __init__(self):
        self.mined_negatives: Dict[str, Set[str]] = {}  # query_keyword -> set of bad doc_ids

    def register_negative(self, query: str, bad_doc_id: str, reason: str):
        keywords = query.lower().split()
        for kw in keywords:
            if len(kw) > 3:
                if kw not in self.mined_negatives:
                    self.mined_negatives[kw] = set()
                self.mined_negatives[kw].add(bad_doc_id)

    def is_negative(self, query: str, doc_id: str) -> bool:
        keywords = query.lower().split()
        for kw in keywords:
            if doc_id in self.mined_negatives.get(kw, set()):
                return True
        return False
