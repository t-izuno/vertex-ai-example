# Vertex AI Gemini API サンプル

Vertex AI の Gemini モデルに API で問い合わせる
サンプルプロジェクトです。
Python と Java (Spring Boot) の実装を含みます。

## 前提条件

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

## 環境変数の設定

`.env.example` をコピーして GCP プロジェクト ID を設定します。
この `.env` は Python・Java 両方のサンプルから共通で使用します。

```bash
cp .env.example .env
# .env の GCP_PROJECT_ID を実際のプロジェクト ID に変更
```

| 変数 | 必須 | デフォルト | 説明 |
| --- | --- | --- | --- |
| `GCP_PROJECT_ID` | Yes | - | GCP プロジェクト ID |
| `GCP_LOCATION` | No | `us-central1` | Vertex AI のリージョン |

## サンプル

### Python

詳細は [python/README.md](python/README.md) を参照してください。
`.env` は `python-dotenv` で自動的に読み込まれます。

```bash
cd python
uv sync
uv run python main.py "こんにちは"
```

### Java (Spring Boot)

詳細は [java/README.md](java/README.md) を参照してください。
実行前に `.env` を `source` して環境変数をシェルに読み込みます。

```bash
cd java
source ../.env && ./mvnw spring-boot:run
```

## プロジェクト構成

```text
vertex-ai-example/
├── .env.example                 # 環境変数テンプレート（共通）
├── scripts/
│   └── setup-gcp.sh            # GCP 初期設定スクリプト
├── python/
│   ├── main.py                  # CLI サンプル
│   └── pyproject.toml           # uv プロジェクト定義
├── java/
│   ├── src/                     # Spring Boot アプリケーション
│   └── pom.xml                  # Maven プロジェクト定義
└── README.md
```
