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
git clone https://github.com/Gemy-Dev/GoogleMapsScraper.git
cd GoogleMapsScraper
```
# Setup Instructions for GoogleMapsScraper Flask Application

## Prerequisites

- Python 3.7 or higher installed on your system. Use `python3` command if `python` is not available.
- pip package manager installed.
- Node.js and npm installed (required for Playwright browsers).

## Environment Setup

1. **Create and activate a virtual environment (recommended):**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Install Playwright browsers:**

```bash
playwright install
```

This will download the necessary browser binaries for Playwright.

## Running the Flask Application

1. **Set the FLASK_APP environment variable:**

On macOS/Linux:

```bash
export FLASK_APP=app
```

On Windows (cmd):

```cmd
set FLASK_APP=app
```

2. **Run the Flask app:**

```bash
flask run
```

or if `python` command is not available, use:

```bash
python3 -m flask run
```

3. **Access the app:**

Open your browser and go to `http://127.0.0.1:5000/`

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
