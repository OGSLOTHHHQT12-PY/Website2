from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "ceaab884a6mshcfe0a4329130fdfp1e913bjsncb9dc8b4b7a7"

@app.route("/")
def home():
    return "Live Price Finder Running"

@app.route("/search")
def search():

    product = request.args.get("product")

    url = "https://real-time-product-search.p.rapidapi.com/search"

    querystring = {
        "query": product,
        "country": "in"
    }

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

app.run(host="0.0.0.0", port=10000)
