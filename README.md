# 割り勘計算（warikan）

「GitHub Actions 入門」のハンズオンで育てるリポジトリです。
合計の金額と人数から、1人あたりの金額を計算します。割り切れない端数は幹事が払い、幹事が多めに払うこともできます。

<!-- ▼ ハンズオン H2 で、ここにワークフローの状態バッジを貼ります
[![CI](https://github.com/<あなたのユーザー名>/warikan/actions/workflows/ci.yml/badge.svg)](https://github.com/<あなたのユーザー名>/warikan/actions/workflows/ci.yml)
-->

## 中身

| ファイル | 役割 |
|---|---|
| `warikan/calc.py` | 割り勘の計算（関数だけの小さなコード） |
| `tests/test_calc.py` | pytest のテスト |
| `scripts/build_site.py` | 早見表（金額 × 人数）の HTML を `site/` に書き出す |
| `pyproject.toml` | pytest・ruff の設定 |
| `requirements-dev.txt` | テストとチェックに使う道具（バージョンは固定） |

`.github/workflows/` はまだありません。ハンズオンで1つずつ作ります。

## 使い方

このリポジトリの右上の **Use this template** → **Create a new repository** で、自分のリポジトリを作ってください（公開リポジトリをおすすめします）。

手元で動かしたい場合（任意。コースはブラウザだけで進められます）:

```bash
pip install -r requirements-dev.txt
ruff check .                  # 書き方のチェック
pytest                        # テスト
python scripts/build_site.py  # 早見表を site/index.html に書き出す
```

## 計算の例

```python
from warikan.calc import split, split_with_extra

split(10000, 3)  # 幹事以外 3,333円、幹事 3,334円
split(10000, 3, unit=100)  # 幹事以外 3,300円、幹事 3,400円
split_with_extra(10000, 4, extra=1000)  # 幹事以外 2,250円、幹事 3,250円
```
