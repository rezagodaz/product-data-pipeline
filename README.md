# Small-Scale Product Data Pipeline

This project scrapes product data from Staples (Windows laptops category), generates marketing summaries using OpenAI GPT-4, and serves the summarized data via a Flask API with a simple frontend.

---

## Features

- Scrapes product details like title, price, rating, badge, URL, and image from Staples.ca
- Uses OpenAI GPT-4 via a class-based wrapper to generate concise 2-3 sentence marketing summaries
- Provides a Flask REST API to serve product data with summaries
- Displays products and summaries on a simple HTML page

---

## Tech Stack

- Python  
- Playwright + BeautifulSoup for web scraping  
- OpenAI GPT-4 (via `openai` Python SDK)  
- Flask for API and frontend  
- dotenv for environment variable management  

---

## Setup Instructions

### Prerequisites

- Python 3.8+  
- Git
- Working only under Linux  

### Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/rezagodaz/product-data-pipeline.git
    cd product-data-pipeline
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

4. Create a `.env` file in the root folder with your OpenAI API key:

    ```ini
    OPEN_AI_KEY=your_openai_api_key_here
    ```

---

## Usage

### Scrape and Summarize

Run a Python script or interactive shell:

```python
from webscraper import scrape_staples_with_bs
from my_openai import ProductSummarizer

products = scrape_staples_with_bs()
summarizer = ProductSummarizer()
summarized = summarizer.summarize_all_products(products)
summarizer.save_to_json(summarized)
```

### Run Flask API

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser to view the product list with summaries.

---

## Project Structure

- `webscraper.py`: Scrapes product data from Staples
- `my_openai.py`: ProductSummarizer class for LLM summary generation and JSON saving
- `app.py`: Flask API and frontend server
- `templates/index.html`: Frontend HTML template

---

## Assumptions & Limitations

- Scrapes only 10 products from a single category
- Simple error handling for API and scraping failures
- No advanced anti-bot or infinite scroll handling implemented

---

## Future Work

- Handle infinite scrolling and anti-bot measures
- Enhance prompts for better marketing summaries
- Add image and rating display improvements
- Deploy API and frontend on cloud platforms (e.g., GCP)
- Expand scraping targets to other retailers and categories

---

## License

This project is licensed under the MIT License.

---

## Contact

Created by rezagodaz.
