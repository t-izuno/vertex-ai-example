package com.example.vertexai;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class VertexAiExampleApplication implements CommandLineRunner {

	@Value("${gcp.project-id}")
	private String projectId;

	@Value("${gcp.location}")
	private String location;

	@Value("${vertex-ai.model}")
	private String model;

	public static void main(String[] args) {
		SpringApplication.run(VertexAiExampleApplication.class, args);
	}

	@Override
	public void run(String... args) {
		var prompt = args.length > 0
				? String.join(" ", args)
				: "こんにちは。自己紹介してください。";

		var client = Client.builder()
				.vertexAI(true)
				.project(projectId)
				.location(location)
				.build();

		GenerateContentResponse response = client.models.generateContent(model, prompt, null);
		System.out.println(response.text());
	}
}
