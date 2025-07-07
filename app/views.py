import time
import json
import re
from flask import jsonify, request, render_template, flash
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from .config import *
import os
import sys

def get_browser_path():
    if getattr(sys, 'frozen', False):
        # Running in a PyInstaller bundle
        base_path = sys._MEIPASS
        return os.path.join(base_path, 'playwright', 'chrome.exe')
    else:
        # Running in normal Python environment
        return None


def extract_phone_numbers(text):
    """Extract phone numbers from text using regex patterns"""
    phone_patterns = [
        r'\b\d{3}\s\d{8}\b',  # Egyptian format: 011 55580913
        r'\b\d{3}\s\d{3}\s\d{4}\b',  # Format: 012 220 1030
        r'\b0\d{2}\s\d{8}\b',  # Format: 011 55580913
        r'\b0\d{10}\b',  # Format: 01155580913
        r'\+20\d{9,10}',  # Egyptian international format
        r'\b\d{11}\b',  # 11 digit numbers
        r'\b\d{3}-\d{3}-\d{4}\b',  # Format: 123-456-7890
        r'\(\d{3}\)\s*\d{3}-\d{4}',  # Format: (123) 456-7890
    ]
    
    phones = []
    for pattern in phone_patterns:
        matches = re.findall(pattern, text)
        phones.extend(matches)
    
    # Clean and validate phone numbers
    cleaned_phones = []
    for phone in phones:
        # Remove extra spaces and clean
        phone = re.sub(r'\s+', ' ', phone.strip())
        # Check if it's a valid phone number (has enough digits)
        digits_only = re.sub(r'\D', '', phone)
        if len(digits_only) >= 10:
            cleaned_phones.append(phone)
    
    return list(set(cleaned_phones))  # Remove duplicates

def extract_emails(text):
    """Extract email addresses from text"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return list(set(emails))

def extract_websites(text):
    """Extract website URLs from text"""
    url_patterns = [
        r'https?://[^\s<>"]+',  # http/https URLs
        r'www\.[^\s<>"]+',  # www URLs
        r'\b[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]?\.[a-zA-Z]{2,}(?:/[^\s<>"]*)?',  # domain names
    ]
    
    websites = []
    for pattern in url_patterns:
        matches = re.findall(pattern, text)
        websites.extend(matches)
    
    # Clean and validate URLs
    cleaned_websites = []
    for website in websites:
        # Skip if it looks like an email
        if '@' in website:
            continue
        # Skip if it's just a file extension or doesn't look like a website
        if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9-]*\.[a-zA-Z]{2,}', website.replace('www.', '').replace('https://', '').replace('http://', '')):
            continue
        # Add protocol if missing
        if not website.startswith(('http://', 'https://')):
            if website.startswith('www.'):
                website = 'https://' + website
            else:
                website = 'https://' + website
        cleaned_websites.append(website)
    
    return list(set(cleaned_websites))

def scroll_results_panel(page, target_count):
    """Scroll the results panel to load more businesses"""
    print(f"Attempting to load {target_count} businesses...")
    
    # Try multiple scroll strategies
    max_attempts = 30
    no_change_count = 0
    previous_count = 0
    
    for attempt in range(max_attempts):
        # Get current business count
        businesses = page.query_selector_all('a[data-cid]')
        if not businesses:
            businesses = page.query_selector_all('a[class*="hfpxzc"]')
        
        # Filter out unwanted elements (like the menu button)
        filtered_businesses = []
        for b in businesses:
            tag_name = b.evaluate("el => el.tagName")
            jsaction = b.get_attribute("jsaction")
            if tag_name == "BUTTON" or (jsaction and "navigationrail.more" in jsaction):
                continue  # Skip the menu button
            filtered_businesses.append(b)

        current_count = len(filtered_businesses)
        print(f"Attempt {attempt + 1}: Found {current_count} businesses")
        
        if current_count >= target_count:
            print(f"Target reached: {current_count} businesses")
            break
        
        if current_count == previous_count:
            no_change_count += 1
            if no_change_count >= 5:
                print("No new businesses loaded after 5 attempts, stopping")
                break
        else:
            no_change_count = 0
        
        previous_count = current_count
        
        # Multiple scroll strategies
        try:
            # Strategy 1: Scroll the results panel
            page.evaluate("""
                const resultsPanel = document.querySelector('div[role="main"]');
                if (resultsPanel) {
                    resultsPanel.scrollTop = resultsPanel.scrollHeight;
                }
            """)
            
            time.sleep(2)
            
            # Strategy 2: Scroll to the last business item
            if filtered_businesses:
                page.evaluate("""
                    (el) => el.scrollIntoView({ behavior: 'smooth', block: 'center' })
                """, filtered_businesses[-1])
            time.sleep(2)
            
            # Strategy 3: Try to find and click "More results" if available
            try:
                more_button = page.query_selector('button[jsaction*="more"]')
                if more_button and more_button.is_visible():
                    more_button.click()
                    time.sleep(3)
            except:
                pass
            
            # Check for the close button and click it if found
            close_btn = page.query_selector('button[jsaction="settings.close"]')
            if close_btn:
                print("Found settings close button, clicking it to close popup.")
                close_btn.click()
                time.sleep(1)  # Give time for the popup to close
            
        except Exception as e:
            print(f"Scroll error: {e}")
            continue
    
    final_businesses = page.query_selector_all('a[data-cid]')
    if not final_businesses:
        final_businesses = page.query_selector_all('a[class*="hfpxzc"]')
    
    print(f"Final count: {len(final_businesses)} businesses loaded")
    
    # After scrolling and before processing businesses:
    # Filter out unwanted buttons (like the menu button)
    filtered_businesses = []
    for b in final_businesses:
        # Exclude elements that are buttons or have jsaction="navigationrail.more"
        tag_name = b.evaluate("el => el.tagName")
        jsaction = b.get_attribute("jsaction")
        if tag_name == "BUTTON" and jsaction and "navigationrail.more" in jsaction:
            continue
        filtered_businesses.append(b)

    return filtered_businesses

from .config import app

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with sync_playwright() as p:
            keyword = request.form.get("keyword")
            city = request.form.get("city")
            district = request.form.get("district")
            result_qtn = int(request.form.get("qtn"))
            
            if keyword == "" or city == "" or district == "":
                flash("gerekli kısımlardan birisi doldurulmamış sanki...")
                return render_template("index.html")
            
            # browser = p.chromium.launch(headless=False)
            browser = p.chromium.launch(
                            headless=False,
                            executable_path=get_browser_path()
                        )
            page = browser.new_page()
            
            # Set a longer timeout for page loads
            page.set_default_timeout(60000)
            
            try:
                page.goto("https://www.google.com/maps")
                
                # Wait for page to load
                page.wait_for_selector("input#searchboxinput")
                
                # Put user-provided keywords and trigger search button
                search_query = f"{keyword} in {district} {city}"
                page.fill("input#searchboxinput", search_query)
                page.click("button#searchbox-searchbutton")
                
                # Wait for results to load
                page.wait_for_selector('div[role="main"]', timeout=30000)
                time.sleep(3)
                
                # Scroll to load more businesses
                businesses = scroll_results_panel(page, result_qtn)
                
                print(f"Total businesses found: {len(businesses)}")
                
                data = []
                processed_names = set()  # To avoid duplicates
                
                # Use filtered_businesses instead of businesses in your loop
                for i, business in enumerate(businesses[:result_qtn]):
                    print(f"Processing business {i+1}/{min(result_qtn, len(businesses))}")
                    
                    try:
                        # Click on the business
                        business.click()
                        time.sleep(2)
                        
                        # Wait for the business details to load
                        page.wait_for_selector('h1', timeout=10000)
                        
                        # Get the main content
                        main_content = page.query_selector('div[role="main"]')
                        if not main_content:
                            print(f"Business {i+1}: No main content found")
                            continue
                        
                        # Extract business name
                        name_element = page.query_selector('h1[class*="DUwDvf"]')
                        if name_element:
                            name = name_element.inner_text().strip()
                        else:
                            name = f"Business {i+1}"
                        
                        # Skip if we've already processed this business
                        if name in processed_names:
                            print(f"Skipping duplicate: {name}")
                            continue
                        processed_names.add(name)
                        
                        # Extract address
                        address_element = page.query_selector('button[data-item-id="address"]')
                        if address_element:
                            address = address_element.inner_text().strip()
                        else:
                            # Try alternative selector
                            address_element = page.query_selector('div[class*="Io6YTe fontBodyMedium"]')
                            address = address_element.inner_text().strip() if address_element else "No address found"
                        
                        # Get all text content from the page for extraction
                        all_text = main_content.inner_text()
                        
                        # Extract contact information from all text
                        phones = extract_phone_numbers(all_text)
                        emails = extract_emails(all_text)
                        websites = extract_websites(all_text)
                        
                        # Try to get phone from phone button
                        try:
                            phone_button = page.query_selector('button[data-item-id="phone"]')
                            if phone_button:
                                phone_text = phone_button.inner_text().strip()
                                phone_numbers = extract_phone_numbers(phone_text)
                                phones.extend(phone_numbers)
                        except:
                            pass
                        
                        # Try to get website from website button
                        try:
                            website_button = page.query_selector('a[data-item-id="authority"]')
                            if website_button:
                                website_href = website_button.get_attribute('href')
                                if website_href:
                                    websites.append(website_href)
                        except:
                            pass
                        
                        # Remove duplicates and clean
                        phones = list(set(phones))
                        emails = list(set(emails))
                        websites = list(set(websites))
                        
                        business_data = {
                            "name": name,
                            "address": address,
                            "phone": phones[0] if phones else None,
                            "email": emails[0] if emails else None,
                            "website": websites[0] if websites else None,
                        }
                        
                        data.append(business_data)
                        
                        print(f"✓ {name}")
                        if phones:
                            print(f"  📞 Phone: {phones[0]}")
                        if emails:
                            print(f"  📧 Email: {emails[0]}")
                        if websites:
                            print(f"  🌐 Website: {websites[0]}")
                        print(f"  📍 Address: {address}")
                        print("---")
                        
                        # Small delay to avoid overwhelming the server
                        time.sleep(0.5)
                        
                    except Exception as e:
                        print(f"Error processing business {i+1}: {str(e)}")
                        continue
                
                # Save the scraped data to a JSON file
                with open("app/scraped_data.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                print(f"✅ Successfully scraped {len(data)} unique businesses")
                browser.close()
                
                return jsonify({
                    "success": True,
                    "total_scraped": len(data),
                    "requested": result_qtn,
                    "data": data
                })
                
            except Exception as e:
                print(f"❌ Error during scraping: {str(e)}")
                browser.close()
                flash(f"Scraping error: {str(e)}")
                return render_template("index.html")
    
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run()