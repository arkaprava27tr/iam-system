import pandas as pd
try:
  df = pd.read_csv("sensor_data.csv")
except FileNotFoundError:
  print("Error:sensor_data.csv not found. Run data_collector.py first.")
  exit()

summary = {
  "Total Records":len(df),
  "Average Temperature":df["temperature"].mean(),
  "Max Temperature":df["temperature"].max(),
  "Min Temperature":df["temperature"].min(),
  "Average Vibration":df["vibration"].mean(),
  "Max Vibration":df["vibration"].max(),
  "Min Vibration":df["vibration"].min(),
}

with open("analysis_summary.txt","w") as f:
  for key,value in summary.items():
     f.write(f"{key}:{value}\n")
print("Analysis complete -> results saved in analysis_summary.txt")

