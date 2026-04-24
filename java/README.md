# Java (Spring Boot) サンプル

`google-genai` SDK を使用して
Vertex AI Gemini モデルに問い合わせる CLI アプリケーションです。

## 前提条件

- Java 21 以上
- Maven 3.9 以上（Maven Wrapper 同梱）
- ルートの `.env` が設定済みであること
  （[ルート README](../README.md) 参照）

## 使い方

ルートの `.env` を読み込んでから実行します。

```bash
# .env を読み込んで実行
source ../.env && ./mvnw spring-boot:run

# プロンプトを引数で指定
source ../.env && ./mvnw spring-boot:run \
  -Dspring-boot.run.arguments="日本の首都はどこですか？"
```

## 設定

`src/main/resources/application.properties` で
モデルを変更できます。

```properties
vertex-ai.model=gemini-3-flash-preview
```
