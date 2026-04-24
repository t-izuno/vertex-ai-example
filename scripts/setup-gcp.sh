#!/usr/bin/env bash
# Vertex AI を利用するための GCP 初期設定スクリプト
#
# 使い方:
#   ./scripts/setup-gcp.sh <PROJECT_ID> [REGION]
#
# 前提条件:
#   - gcloud CLI がインストール済みであること
#   - gcloud auth login 済みであること
#   - 対象プロジェクトのオーナーまたは編集者権限を持つこと

set -euo pipefail

PROJECT_ID="${1:?エラー: PROJECT_ID を第1引数に指定してください}"
REGION="${2:-us-central1}"

echo "=== Vertex AI セットアップ ==="
echo "プロジェクト: ${PROJECT_ID}"
echo "リージョン:   ${REGION}"
echo ""

# 1. プロジェクトを設定
echo "[1/4] プロジェクトを設定..."
gcloud config set project "${PROJECT_ID}"

# 2. Vertex AI API を有効化
echo "[2/4] Vertex AI API を有効化..."
gcloud services enable aiplatform.googleapis.com

# 3. デフォルトリージョンを設定
echo "[3/4] デフォルトリージョンを設定..."
gcloud config set compute/region "${REGION}"

# 4. アプリケーションデフォルト認証を設定
echo "[4/4] アプリケーションデフォルト認証を設定..."
gcloud auth application-default login

echo ""
echo "=== セットアップ完了 ==="
echo "main.py の project_id を '${PROJECT_ID}' に変更して実行してください。"
