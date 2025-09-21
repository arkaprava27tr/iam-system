import csv
import time
import argparse
import random
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("--interval", type=int, default=5, help="Interval in seconds between readings")
parser.add_argument("--duration", type=int, default=60, help="Total duration in seconds")
args = parser.parse_args()


end_time = time.time() + args.duration


with open("sensor_data.csv", "w", newline="")as file:
  writer = csv.writer(file)
  writer.writerow(["timestamp","temperature","vibration"])
  while time.time() < end_time:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature = round(random.uniform(20,100),2)
    vibration = round(random.uniform(0.1,5.0),2)

    writer.writerow([timestamp,temperature,vibration])
    print(f"{timestamp}|Temp:{temperature}°C|Vib:{vibration}m/s^2")
    time.sleep(args.interval)

