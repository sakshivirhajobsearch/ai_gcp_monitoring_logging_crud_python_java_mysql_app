package com.ai.gcp.monitoring.logging.repository;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

public class MonitoringRepository {
	
	private static final String BASE_URL = "http://127.0.0.1:5000";

	public String getMetricsDataWithAI(String metric) throws Exception {
		String encoded = URLEncoder.encode(metric, "UTF-8");
		URL url = new URL(BASE_URL + "/monitoring/data?metric=" + encoded);
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
