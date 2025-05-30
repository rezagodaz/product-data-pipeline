import openai
import os
import json
from dotenv import load_dotenv

class ProductSummarizer:
    def __init__(self, api_key_env_var="OPEN_AI_KEY"):
        load_dotenv()
        self.api_key = os.getenv(api_key_env_var)
        if not self.api_key:
            raise ValueError(f"API key not found in environment variable '{api_key_env_var}'")
        openai.api_key = self.api_key

    def generate_summary(self, product_info):
        prompt = f"""
        You are a product marketing expert. Given the following product details, generate a short 2–3 sentence marketing summary highlighting its key features and appeal.

        Product Title: {product_info.get("title", "N/A")}
        Price: {product_info.get("price", "N/A")}
        Rating: {product_info.get("rating", "N/A")}
        Badge: {product_info.get("badge", "N/A")}

        Write in an engaging, clear, and informative tone.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=100
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            print("OpenAI API error:", e)
            return "Summary generation failed."

    def summarize_all_products(self, products_dict):
        summarized_products = []
        for title, product in products_dict.items():
            product["title"] = title  # Add title back as a field
            print(f"Summarizing: {title}...")
            summary = self.generate_summary(product)
            product["summary"] = summary
            summarized_products.append(product)
        return summarized_products

    def save_to_json(self, products_list, filename="summarized_products.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(products_list, f, indent=4, ensure_ascii=False)
        print(f"Saved to {filename}")
