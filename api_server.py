"""Optional local REST API server for the bundled API sample data."""
from pathlib import Path
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
DATA_FILE = Path(__file__).resolve().parent / "data" / "api_customers.json"

@app.get("/api/customers")
def customers():
    data = pd.read_json(DATA_FILE).where(pd.notna(pd.read_json(DATA_FILE)), None)
    return jsonify(data.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
