import pandas as pd
import os

def extract_data(filepath):

    if "D:" in filepath:
        filepath = filepath.replace("D:", "/mnt/d").replace("\\", "/")

    print(f"Attempting to read file from: {filepath}")

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at: {filepath}")

    df = pd.read_csv(filepath)
    print(f"✅ Extracted {len(df)} rows.")
    return df