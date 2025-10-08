package com.ai.gcp.monitoring.logging.gui;

import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;

import com.ai.gcp.monitoring.logging.repository.LoggingRepository;
import com.ai.gcp.monitoring.logging.repository.MonitoringRepository;

public class UnifiedGUI extends JFrame {

	private static final long serialVersionUID = 1L;

	private final MonitoringRepository monitoringRepo;
	private final LoggingRepository loggingRepo;
	private final JTextArea textArea;

	public UnifiedGUI() {
		monitoringRepo = new MonitoringRepository();
		loggingRepo = new LoggingRepository();
		textArea = new JTextArea();
		JScrollPane scrollPane = new JScrollPane(textArea);

		JButton btnFetchMetrics = new JButton("Fetch Monitoring + AI");
		btnFetchMetrics.addActionListener(e -> fetchMetrics());

		JButton btnFetchLogs = new JButton("Fetch Logs + AI");
		btnFetchLogs.addActionListener(e -> fetchLogs());

		JPanel panel = new JPanel();
		panel.add(btnFetchMetrics);
		panel.add(btnFetchLogs);

		setTitle("AI + GCP Monitoring & Logging GUI");
		setSize(900, 600);
		setLayout(new BorderLayout());
		add(panel, BorderLayout.NORTH);
		add(scrollPane, BorderLayout.CENTER);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	private void fetchMetrics() {
		try {
			String metricType = JOptionPane.showInputDialog(this, "Enter GCP Metric Type:",
					"compute.googleapis.com/instance/cpu/utilization");
			if (metricType != null && !metricType.trim().isEmpty()) {
				String result = monitoringRepo.getMetricsDataWithAI(metricType);
				textArea.setText(result);
			}
		} catch (Exception ex) {
			textArea.setText("Error fetching metrics: " + ex.getMessage());
		}
	}

	private void fetchLogs() {
		try {
			String result = loggingRepo.getLogsDataWithAI();
			textArea.setText(result);
		} catch (Exception ex) {
			textArea.setText("Error fetching logs: " + ex.getMessage());
		}
	}

	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> new UnifiedGUI().setVisible(true));
	}
}
