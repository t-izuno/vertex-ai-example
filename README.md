# Vertex AI Gemini API サンプル

Vertex AI の Gemini モデルに API で問い合わせる
Python サンプルプロジェクトです。

## 前提条件

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/) (Python パッケージマネージャ)
- [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
- Vertex AI API が有効な GCP プロジェクト

## GCP セットアップ

セットアップスクリプトを実行します。

```bash
./scripts/setup-gcp.sh <PROJECT_ID> [REGION]
```

引数:

| 引数 | 必須 | デフォルト | 説明 |
| --- | --- | --- | --- |
| `PROJECT_ID` | Yes | - | GCP プロジェクト ID |
| `REGION` | No | `us-central1` | Vertex AI のリージョン |

スクリプトは以下を実行します:

1. `gcloud config set project` でプロジェクトを設定
2. `gcloud services enable aiplatform.googleapis.com` で
   Vertex AI API を有効化
3. `gcloud config set compute/region` でリージョンを設定
4. `gcloud auth application-default login` で認証を設定

### 手動で設定する場合

```bash
# プロジェクトを設定
gcloud config set project YOUR_PROJECT_ID

# Vertex AI API を有効化
gcloud services enable aiplatform.googleapis.com

# リージョンを設定
gcloud config set compute/region us-central1

# アプリケーションデフォルト認証
gcloud auth application-default login
```

## Python 環境セットアップ

```bash
# 依存関係をインストール
uv sync
```

## 使い方

実行前に `main.py` の `project_id` を
実際の GCP プロジェクト ID に変更してください。

```bash
# デフォルトプロンプトで実行
uv run python main.py

# プロンプトを引数で指定
uv run python main.py "日本の首都はどこですか？"
```

## プロジェクト構成

```text
vertex-ai-example/
├── scripts/
│   └── setup-gcp.sh    # GCP 初期設定スクリプト
├── main.py              # Gemini API 問い合わせサンプル
├── pyproject.toml       # プロジェクト定義
├── uv.lock              # 依存関係ロックファイル
└── README.md
```
