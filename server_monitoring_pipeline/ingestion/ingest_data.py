import pandas as pd
import os

print("Starting ingestion...")

file_path = os.path.join("data", "server_logs.csv")

try:
    
    df = pd.read_csv(file_path)

    print("\nDataset Loaded Successfully")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nColumns:")
    print(df.columns)

    print("\nTotal rows:", len(df))

except Exception as e:
    print("Error while reading file:", e)