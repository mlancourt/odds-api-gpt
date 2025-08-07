import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/get-odds")
def get_odds():
    sport = request.args.get("sport", "baseball_mlb")
    market = request.args.get("market", "moneyline")
    region = request.args.get("region", "us")

    api_key = os.environ.get("ODDS_API_KEY")
    if not api_key:
        return jsonify({"error": "Missing ODDS_API_KEY env var"}), 500

    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds"
    params = {
    "apiKey": api_key,
    "regions": region,
    "markets": market,
    "oddsFormat": "american",
    "bookmakers": "fanduel"  # Only pull FanDuel odds
    }
    r = requests.get(url, params=params, timeout=15)
    return jsonify(r.json()), r.status_code

@app.get("/health")
def health():
    return "ok", 200
