"""Vertex AI Gemini モデルへの問い合わせサンプル."""

import sys

from google import genai
from google.genai import types


def main() -> None:
    # TODO: プロジェクトIDとリージョンを環境に合わせて変更してください
    project_id = "your-gcp-project-id"
    location = "us-central1"

    client = genai.Client(
        vertexai=True,
        project=project_id,
        location=location,
    )

    prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "こんにちは。自己紹介してください。"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=1024,
        ),
    )

    print(response.text)


if __name__ == "__main__":
    main()
