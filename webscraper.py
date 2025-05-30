from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def scrape_staples_with_bs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            viewport={'width': 1280, 'height': 720}
        )
        page = context.new_page()

        products_dict = {}             

        try:
            page.goto("https://www.staples.ca/collections/windows-laptops-91", timeout=30000)
            time.sleep(5)  # Wait for dynamic content to load

            # Get the full HTML content after rendering
            html = page.content()
            soup = BeautifulSoup(html, 'html.parser')

            products = soup.select('div.product-thumbnail')
            if not products:
                print("No products found in rendered HTML.")
                return

            for product in products[:10]:
                # Title
                title_tag = product.select_one('a.product-thumbnail__title')
                title = title_tag.get_text(strip=True) if title_tag else "N/A"

                # URL
                url = title_tag['href'] if title_tag else "N/A"
                if url.startswith("/"):
                    url = "https://www.staples.ca" + url

                # Image
                image_tag = product.select_one('img.product-thumbnail__image')
                image = image_tag['src'] if image_tag else "N/A"

                # Rating
                rating_anchor = product.select_one('.product-thumbnail__rating a')
                rating = rating_anchor['aria-label'] if rating_anchor else "No rating"

                # Badge
                badge = product.select_one('span.quantity-break-badge')
                badge_text = badge.get_text(strip=True) if badge else "No badge"

                # Price
                price_tag = product.select_one('span.money.pre-money')
                price = price_tag.get_text(strip=True) if price_tag else "No price"

                products_dict[title] = {
                    "url": url,
                    "image": image,
                    "rating": rating,
                    "badge": badge_text,
                    "price" : price
                }
 
        except Exception as e:
            print("Error encountered:", e)
        finally:
            browser.close()
    
    return products_dict

