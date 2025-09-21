#!/bin/bash
echo "Starting Data Collection for 30 seconds..."
timeout 30 python3 data_collector.py

echo "Analyzing data..."
python3 data_analyzer.py
echo "Generating PDF report..."
python3 generate_report.py

