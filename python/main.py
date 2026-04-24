"""Vertex AI Gemini モデルへの問い合わせサンプル."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main() -> None:
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")

    project_id = os.environ["GCP_PROJECT_ID"]
    location = os.environ.get("GCP_LOCATION", "us-central1")

    client = genai.Client(
        vertexai=True,
        project=project_id,
        location=location,
    )

    prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "こんにちは。自己紹介してください。"

    response = client.models.generate_content(
        model=os.environ.get("VERTEX_AI_MODEL", "gemini-2.5-flash"),
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=1024,
        ),
    )

    print(response.text)


if __name__ == "__main__":
    main()
