"""CLI for Hard Negative Miner."""
import argparse
from .core import HardNegativeMiner

def main():
    parser = argparse.ArgumentParser(description="Agent Retrieval Hard Negative Miner CLI")
    parser.add_argument("--demo", action="store_true", help="Run negative mining demo")
    args = parser.parse_args()

    miner = HardNegativeMiner()
    miner.register_negative("deploy service", "doc-deprecated-v1", "Triggers hallucinated flag --old")
    flagged = miner.is_negative("deploy service to staging", "doc-deprecated-v1")
    print(f"Distractor check for 'doc-deprecated-v1': Flagged={flagged}")

if __name__ == "__main__":
    main()
