"""Tests for HardNegativeMiner."""
import unittest
from agent_retrieval_negative_miner.core import HardNegativeMiner

class TestHardNegativeMiner(unittest.TestCase):
    def test_distractor_filtering(self):
        miner = HardNegativeMiner()
        miner.register_negative("run database migration", "doc_v0", "Outdated syntax")
        self.assertTrue(miner.is_negative("database migration", "doc_v0"))
        self.assertFalse(miner.is_negative("database migration", "doc_v1"))
