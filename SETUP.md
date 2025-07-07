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

## Notes

- The app uses Playwright to automate Chromium browser for scraping Google Maps data.
- The browser will launch in non-headless mode for visibility.
- Make sure you have a stable internet connection.
- If you encounter issues with Playwright browser path, the app tries to detect the executable path automatically.

## Troubleshooting

- If `python` command is not found, use `python3`.
- If Playwright browsers are not installed, run `playwright install`.
- Ensure your virtual environment is activated before running the app.

## Additional

- To deactivate the virtual environment, run:

```bash
deactivate
```

- To update dependencies, modify `requirements.txt` and run `pip install -r requirements.txt` again.

---

This setup guide should help you get the application running smoothly on your device.
