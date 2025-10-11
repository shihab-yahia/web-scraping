📘 Overview

This project is a simple yet powerful framework for scraping data from websites. It’s designed for quick setup and reusability — perfect for building new scraping scripts fast with minimal effort.

🚀 Features

Static page scraping using requests + BeautifulSoup

Dynamic page scraping using Selenium (headless mode supported)

Easy-to-edit CSS/XPath selectors

Built-in rate limiting and retry handling

Export data to CSV or JSON

Detailed logging & error handling

Includes Dockerfile and environment configuration

⚙️ Dependencies

Python 3.10+

requests

beautifulsoup4

selenium

pandas

python-dotenv

🧩 Quick Start

Clone the repository

git clone https://github.com/<your-username>/web-scraper-bangla.git
cd web-scraper-bangla


Create a virtual environment & install dependencies

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Set up environment variables
Create a .env file:

TARGET_URL=https://example.com
HEADLESS=true
OUTPUT_FORMAT=csv


Run the scraper

python run_scraper.py --config config/site_example.yaml

🧾 Example Configuration (site_example.yaml)
target: "https://example.com/list"
pagination:
  enabled: true
  page_param: "page"
selectors:
  item: ".product-card"
  title: ".product-title"
  price: ".price"
output:
  format: "csv"
  file: "data/output.csv"

🤝 Contributing

Feel free to open issues, suggest new features, or submit pull requests. See CONTRIBUTING.md for guidelines.

📄 License

MIT License — Free to use and modify.
