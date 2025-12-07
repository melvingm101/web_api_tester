import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils.output_print import print_info, print_success, print_error

def run_crawler():
    start_url = input("Enter the website URL to crawl (e.g., http://testphp.vulnweb.com): ").strip()
    
    print_info(f"Crawling {start_url} for links...")
    
    try:
        response = requests.get(start_url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all 'a' tags with an 'href' attribute
        links = soup.find_all('a', href=True)
        
        found_links = set()
        
        for link in links:
            # Get the link and make it a full URL (handles relative paths like /login)
            full_url = urljoin(start_url, link['href'])
            if full_url not in found_links:
                found_links.add(full_url)
        
        if found_links:
            print_success(f"Found {len(found_links)} unique links:")
            for link in found_links:
                print(f" - {link}")
        else:
            print_error("No links found on this page.")
            
    except Exception as e:
        print_error(f"Error crawling page: {e}")

if __name__ == "__main__":
    run_crawler()
