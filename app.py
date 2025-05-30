from flask import Flask, jsonify
from flask import send_from_directory
from webscraper import scrape_staples_with_bs
from my_openai import ProductSummarizer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/products", methods=["GET"])
def get_products():
    products_dict = scrape_staples_with_bs()
    summarizer = ProductSummarizer()
    summarized = summarizer.summarize_all_products(products_dict)
    summarizer.save_to_json(summarized)
    return jsonify(summarized)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)