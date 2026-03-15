import pandas as pd
import os

print("Starting Data Transformation...")

base_dir = os.path.dirname(os.path.dirname(__file__))
input_file = os.path.join(base_dir, "data", "server_logs.csv")

df = pd.read_csv(input_file)

print("Dataset loaded")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df["CPU_Stress"] = df["CPU_Usage_Percent"].apply(
    lambda x: "High" if x > 80 else "Normal"
)

df["Memory_Stress"] = df["Memory_Usage_MB"].apply(
    lambda x: "High" if x > 8000 else "Normal"
)

df["Response_Time_sec"] = df["Response_Time_ms"] / 1000

output_file = os.path.join(base_dir, "data", "processed_server_logs.csv")
df.to_csv(output_file, index=False)

print("Transformation completed")
print("Processed file saved:", output_file)