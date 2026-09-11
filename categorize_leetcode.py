
#!/usr/bin/env python3
"""
Organize LeetCode solution files into category folders by inferring type from the filename.

Usage:
  python categorize_leetcode.py [--dry] [--ext .py] [--unknown unknown]

- It scans the current working directory (where you run it) for files with the given extension.
- It creates folders like: dp, list, string, tree, graph, bit, search (only if used).
- If no rule matches a file, it moves it into the "unknown" folder (default: "unknown").
- Use --dry to preview what would happen without moving anything.
- Edit the CONFIG below to tweak categories and rules.
"""


import argparse
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

# ========== CONFIG ==========
# 1) Simple substring/regex rules (order matters). First match wins.
#    Key = compiled regex, Value = target folder.
RULES: List[Tuple[re.Pattern, str]] = [
    # ---- trees / graphs ----
    (re.compile(r"(?:^|[^A-Za-z])(BST|BinarySearchTree|BinaryTree|N-aryTree|Tree)(?:$|[^A-Za-z])", re.I), "tree"),
    (re.compile(r"(?:^|[^A-Za-z])(Graph|DAG|Topological)(?:$|[^A-Za-z])", re.I), "graph"),

    # ---- strings ----
    (re.compile(r"(?:^|[^A-Za-z])(String|Substr(?:ing)?s?)(?:$|[^A-Za-z])", re.I), "string"),

    # ---- arrays / lists / matrices ----
    (re.compile(r"(?:^|[^A-Za-z])(Array|Subarray|Matrix|Grid|Intervals?|Deque|Queue|Stack)(?:$|[^A-Za-z])", re.I), "list"),
    (re.compile(r"(?:^|[^A-Za-z])(List|LinkedList|LList)(?:$|[^A-Za-z])", re.I), "list"),

    # ---- searching / sorting / two pointers / sliding window ----
    (re.compile(r"(?:^|[^A-Za-z])(BinarySearch|Search(?:ing)?|TwoPointers|SlidingWindow|Sort(?:ing)?)(?:$|[^A-Za-z])", re.I), "list"),

    # ---- bits / math ----
    (re.compile(r"(?:^|[^A-Za-z])(Bit|Bits|Bitwise|XOR|AND|OR|BinaryNumber)(?:$|[^A-Za-z])", re.I), "bit"),
    (re.compile(r"(?:^|[^A-Za-z])(Math|Roman|Integer|Digits?|Number)(?:$|[^A-Za-z])", re.I), "list"),  # treat numeric utils as array/list bucket by default

    # ---- tries / sets / maps (treat as list bucket by default) ----
    (re.compile(r"(?:^|[^A-Za-z])(Trie|Hash(?:Map|Set)?|Map|Set|Dictionary|KeyValue)(?:$|[^A-Za-z])", re.I), "list"),
]

# 2) "Heuristic DP" keywords: if any of these appear, file goes to "dp"
#    (You can expand/shrink this list to your taste. It's purely filename-based.)
DP_KEYWORDS = [
    "HouseRobber", "Robber", "Knapsack", "DecodeWays", "CoinChange", "PalindromePartition",
    "LongestPalindrome", "PalindromicSubstrings", "StrangePrinter", "RemoveBoxes", "StoneGame",
    "StoneGameII", "EditDistance", "PerfectSquare", "Fibonacci", "MaxSubarray", "MinCost",
    "MinimumCost", "Chalk", "Bookcase", "DeleteAndEarn", "ArithmeticSlices", "LIS", "LCS",
]

# ========== END CONFIG ==========

def infer_category(filename: str, unknown_folder: str) -> str:
    stem = Path(filename).stem
    # DP wins if any keyword is found
    for kw in DP_KEYWORDS:
        if re.search(rf"(?:^|[^A-Za-z]){re.escape(kw)}(?:$|[^A-Za-z])", stem, flags=re.I):
            return "dp"
    # Otherwise apply RULES in order
    for pattern, target in RULES:
        if pattern.search(stem):
            return target
    return unknown_folder

def plan_moves(base: Path, ext: str, unknown_folder: str, script_name: str) -> Dict[Path, Path]:
    moves: Dict[Path, Path] = {}
    for p in base.iterdir():
        if not p.is_file():
            continue
        if p.name == script_name:
            continue
        if p.suffix.lower() != ext.lower():
            continue
        target_folder = infer_category(p.name, unknown_folder)
        dst_dir = base / target_folder
        dst_dir.mkdir(exist_ok=True)
        dst = dst_dir / p.name
        if p.resolve() == dst.resolve():
            continue  # already in place
        moves[p] = dst
    return moves

def main():
    parser = argparse.ArgumentParser(description="Categorize LeetCode files into folders by filename patterns.")
    parser.add_argument("--dry", action="store_true", help="Preview moves without changing files")
    parser.add_argument("--ext", default=".py", help="File extension to consider (default: .py)")
    parser.add_argument("--unknown", default="unknown", help='Folder name for uncategorized files (default: "unknown")')
    args = parser.parse_args()

    base = Path.cwd()
    script_name = Path(__file__).name

    moves = plan_moves(base, args.ext, args.unknown, script_name)

    if not moves:
        print("No files to move. (Nothing matched the extension, or everything is already categorized.)")
        return

    print(f"Planned moves ({'dry run' if args.dry else 'executing'}):")
    for src, dst in moves.items():
        print(f"  {src.name}  ->  {dst}")
        if not args.dry:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

    print("Done." if not args.dry else "Dry run complete. Use without --dry to apply.")

if __name__ == "__main__":
    main()