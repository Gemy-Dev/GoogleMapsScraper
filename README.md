# 🌐 Google Maps Scraper - Professional Business Data Extraction Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.30%2B-green)
![MIT License](https://img.shields.io/badge/License-MIT-orange)

**GoogleMapsScraper** is an enterprise-grade Python solution for extracting business intelligence from Google Maps without relying on official APIs. Leveraging [Playwright](https://playwright.dev/) for browser automation, this tool provides reliable, scalable data collection while simulating organic user behavior.

## 🔍 Key Features

### 🏆 Core Capabilities
- **Comprehensive Business Profiles**: Extract name, address, contact details, and digital presence
- **Advanced Data Collection**:
  - Primary contact information (phone, website)
  - Email addresses (when publicly available)
- **Structured Output**: Clean JSON format ready for analysis

### ⚡ Performance Advantages
- **API-Free Operation**: No usage limits or billing requirements
- **Headless Browser Automation**: Mimics human interaction patterns
- **Lightweight Architecture**: Low resource consumption

## 🚀 Implementation Guide

### System Requirements
- Python 3.8+
- Playwright-compatible browser binaries
- 2GB+ RAM (recommended)

### Installation


#### Clone repository
```bash
git clone https://github.com/your-username/GoogleMapsScraper.git
cd GoogleMapsScraper
```
#### Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
#### Install dependencies
```bash
pip install -r requirements.txt
python -m playwright install
```
# Execution


#### ▶️Start the Flask application
```bash
export FLASK_APP=app/views.py  # Windows: set FLASK_APP=app/views.py
flask run --host=0.0.0.0 --port=5000
```
Access the web interface at: http://localhost:5000

### 📊 Data Output
Results are automatically saved to scraped_data.json with the following structure:
```bash
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
```
### ⚠️ Important Considerations

#### Legal Compliance
Review Google's Terms of Service before deployment

Implement reasonable request rates to avoid detection

Consider using proxies for large-scale scraping

#### Technical Limitations
Email availability depends on public listing information

Google's anti-bot measures may require periodic adjustments

📜 License
MIT License - Free for commercial and personal use with attribution
