package com.ai.gcp.monitoring.logging.repository;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class LoggingRepository {
	
	private static final String BASE_URL = "http://127.0.0.1:5000";

	public String getLogsDataWithAI() throws Exception {
		URL url = new URL(BASE_URL + "/logging/data");
		HttpURLConnection conn = (HttpURLConnection) url.openConnection();
		conn.setRequestMethod("GET");

		try (BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
			String inputLine;
			StringBuilder content = new StringBuilder();
			while ((inputLine = in.readLine()) != null) {
				content.append(inputLine).append("\n");
			}
			return content.toString();
		}
	}
}
