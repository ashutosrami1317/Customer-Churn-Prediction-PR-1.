"""Load customer data from CSV, JSON, SQLite and a REST API endpoint."""
from pathlib import Path
import sqlite3
import pandas as pd
import requests

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def load_csv():
    return pd.read_csv(DATA_DIR / "customers_csv.csv")

def load_json():
    return pd.read_json(DATA_DIR / "customers_json.json")

def load_sql():
    with sqlite3.connect(DATA_DIR / "customers.db") as conn:
        return pd.read_sql_query("SELECT * FROM customers", conn)

def load_api():
    """Try the local REST API; use the bundled API response file if server is off."""
    url = "http://127.0.0.1:5000/api/customers"
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except requests.RequestException:
        print("Local API server not running; loading bundled API response JSON instead.")
        return pd.read_json(DATA_DIR / "api_customers.json")

def acquire_all_data():
    frames = [load_csv(), load_json(), load_sql(), load_api()]
    combined = pd.concat(frames, ignore_index=True)
    print("Source records:", [len(frame) for frame in frames])
    print("Combined shape:", combined.shape)
    return combined

if __name__ == "__main__":
    data = acquire_all_data()
    print(data.head())
