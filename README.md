# 📍 GoogleMapsScraper

**GoogleMapsScraper** is a lightweight Python tool that scrapes business data from **Google Maps** using [Playwright](https://playwright.dev/).  
It simulates real user interactions — offering a **free alternative** to the official Google Maps API for basic business info extraction.

---

## 🛠 Features

- 🔍 Simulates user search on Google Maps
- 🧾 Extracts:
  - Business name
  - Address
  - Phone number
  - Website
  - Email (if available)
- 💾 Saves data to `scraped_data.json`
- 🚫 No API keys or billing required

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/GoogleMapsScraper.git
cd GoogleMapsScraper
2. Set up a virtual environment
bash


python -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
3. Install the dependencies
bash


pip install flask playwright beautifulsoup4
python -m playwright install
▶️ Running the App
Make sure your virtual environment is active. Then run:

bash


export FLASK_APP=app/views.py     # On Windows: set FLASK_APP=app/views.py
flask run
Or alternatively:

bash


python -m flask run
Open your browser and go to:

cpp


http://127.0.0.1:5000/
Once the scraper runs, the result will be saved as:

bash


scraped_data.json
🧪 Verifying Setup
If things aren't working as expected, verify that Python and pip are from the virtual environment:

bash


which python
which pip
They should both point to your venv/ directory.

📦 Sample Output
Here's an example of the JSON you’ll get:

json


[
  {
    "name": "Boodigi Digital Solutions",
    "address": "boodigi.com",
    "phone": "010 11781811",
    "email": null,
    "website": "https://www.boodigi.com/"
  },
  {
    "name": "Curve Technology",
    "address": "السياحية السادسة، 190 شارع سامح جادو، قسم أول 6 أكتوبر، محافظة الجيزة 3238024",
    "phone": "010 11781811",
    "email": null,
    "website": "https://cteg.net/"
  }
]


❓ FAQ
⚠️ Why am I not getting email addresses?
Most Google Maps listings don't expose emails. The scraper only extracts emails if they're publicly visible on the profile page.


🔒 Is this against Google’s Terms?
This tool mimics browser behavior without accessing hidden APIs, but always review Google’s Terms of Service before scraping data at scale.



📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute with attribution.

💡 Contributions Welcome
Pull requests, issues, and feedback are always appreciated!

