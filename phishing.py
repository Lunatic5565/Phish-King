import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

# Banner function
def display_banner():
    os.system("clear")  # Clears the screen
    banner = r"""
    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
    ██╔══██╗██║  ██║██║██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
    ██████╔╝███████║██║███████╗█████╔╝ ██║██╔██╗ ██║██║  ███╗
    ██╔═══╝ ██╔══██║██║╚════██║██╔═██╗ ██║██║╚██╗██║██║   ██║
    ██║     ██║  ██║██║███████║██║  ██╗██║██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
        Kali Linux - Phishing Detector
    """
    print(banner)

# Phishing detection function
def is_phishing(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"\n[❌] Error fetching {url}: {e}")
        return False

    print("\n[✔] URL Successfully Retrieved!\n")
    
    # Check if the URL is using HTTPS
    if not url.startswith('https://'):
        print("[❌] The URL is NOT using HTTPS! 🚨")
        return True

    # Check if the URL contains an IP address instead of a domain name
    if re.match(r'^https?://(?:\d{1,3}\.){3}\d{1,3}', url):
        print("[❌] The URL contains an IP address instead of a domain! 🚨")
        return True

    # Parse the domain name
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # List of common free domain providers (extendable)
    free_domains = ['000webhostapp.com', 'freenom.com', 'myfreesites.net']
    if any(free_domain in domain for free_domain in free_domains):
        print(f"[❌] The URL is using a known free domain: {domain} 🚨")
        return True

    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text().lower()

    # Check for suspicious keywords
    suspicious_keywords = ['login', 'password', 'verify', 'credit card', 'banking', 'social security']
    for keyword in suspicious_keywords:
        if keyword in text:
            print(f"[⚠] The webpage contains the suspicious keyword: '{keyword}' 🚨")
            return True

    # Check for suspicious form with a POST method (data submission)
    forms = soup.find_all('form', method=True)
    for form in forms:
        if form.get('method', '').lower() == 'post':
            print("[⚠] The webpage contains a form with a POST method! 🚨")
            return True

    # Check if the webpage loads scripts from external domains
    scripts = soup.find_all('script', src=True)
    external_scripts = [script['src'] for script in scripts if urlparse(script['src']).netloc not in domain]
    if external_scripts:
        print(f"[⚠] The webpage contains external scripts: {external_scripts[:3]} 🚨")
        return True

    # Check for iframes that load content from an external domain
    iframes = soup.find_all('iframe', src=True)
    external_iframes = [iframe['src'] for iframe in iframes if urlparse(iframe['src']).netloc not in domain]
    if external_iframes:
        print(f"[⚠] The webpage contains external iframes: {external_iframes[:3]} 🚨")
        return True

    # Check for suspicious external links (phishing sites often redirect users)
    links = soup.find_all('a', href=True)
    external_links = [link['href'] for link in links if urlparse(link['href']).netloc and urlparse(link['href']).netloc not in domain]
    if external_links:
        print(f"[⚠] The webpage contains external links: {external_links[:3]} 🚨")  # Show first 3 links for brevity
        return True

    print("\n✅ The webpage is likely **NOT** phishing.")
    return False

# Main function
def main():
    display_banner()
    url = input("\n[🔍] Enter the URL to check: ").strip()
    print("\n[🛡] Scanning the website...\n")
    is_phishing(url)

if __name__ == "__main__":
    main()
