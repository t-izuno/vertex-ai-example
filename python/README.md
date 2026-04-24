# Python サンプル

`google-genai` SDK を使用して
Vertex AI Gemini モデルに問い合わせるサンプルです。

## 前提条件

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/)
- ルートの `.env` が設定済みであること
  （[ルート README](../README.md) 参照）

## セットアップ

```bash
uv sync
```

## 使い方

```bash
# デフォルトプロンプトで実行
uv run python main.py

# プロンプトを引数で指定
uv run python main.py "日本の首都はどこですか？"
```

ルートの `../.env` から環境変数を自動で読み込みます。
