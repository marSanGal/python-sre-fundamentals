#!/usr/bin/env python3
import argparse, sys

def run(args: argparse.Namespace) -> int:
    print("✅ Hello from fundamentals exercise!")
    return 0

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Fundamentals exercises")
    return p

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        code = run(args)
        sys.exit(code)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
