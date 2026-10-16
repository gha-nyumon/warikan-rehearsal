"""pytest の結果（JUnit 形式の XML）から、実行のまとめ（Markdown）を作る。

使い方（ワークフローの中で）:
    python scripts/summary.py report/junit.xml >> "$GITHUB_STEP_SUMMARY"
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("report/junit.xml")
    title = sys.argv[2] if len(sys.argv) > 2 else "テストの結果"
    print(f"## {title}\n")
    if not path.exists():
        print(
            "テストの結果のファイルがありません（テストの前のステップで失敗した可能性があります）。"
        )
        return

    root = ET.parse(path).getroot()
    suite = root if root.tag == "testsuite" else root.find("testsuite")
    total = int(suite.get("tests", 0))
    failed = int(suite.get("failures", 0)) + int(suite.get("errors", 0))
    skipped = int(suite.get("skipped", 0))
    passed = total - failed - skipped

    mark = "✅ すべて成功" if failed == 0 else f"❌ {failed}件 失敗"
    print(f"**{mark}**\n")
    print("| 成功 | 失敗 | スキップ | 合計 |")
    print("|---:|---:|---:|---:|")
    print(f"| {passed} | {failed} | {skipped} | {total} |\n")

    if failed:
        print("### 失敗したテスト\n")
        for case in suite.iter("testcase"):
            problem = case.find("failure")
            if problem is None:
                problem = case.find("error")
            if problem is not None:
                message = (problem.get("message") or "").splitlines()[0][:200]
                print(f"- `{case.get('name')}`: {message}")
        print()


if __name__ == "__main__":
    main()
