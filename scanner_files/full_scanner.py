import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from utils.output_print import print_info, print_success, print_error, print_panel, print_progress_bar, return_console, print_info_label
from active_scan import scan_url

def get_all_links(url):
    try:
        response = requests.get(url, timeout=3)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)

        extracted_links = set()
        for link in links:
            full_url = urljoin(url, link['href'])
            extracted_links.add(full_url)
        return extracted_links
    except:
        return set()

def run_full_scan():
    print_panel("Deep Automated Scanner (Depth=2)", "Full Scan")
    start_url = input("Enter the Homepage URL (e.g., http://testphp.vulnweb.com): ").strip()

    if not start_url.startswith("http"):
        print_error("Error: Invalid Input. Please enter a URL starting with 'http://' or 'https://'")
        return

    base_domain = urlparse(start_url).netloc

    print_info(f"{print_info_label("PHASE 1")} Map the website: Crawling {start_url}...")

    level_1_links = get_all_links(start_url)

    internal_links = {link for link in level_1_links if urlparse(link).netloc == base_domain}

    print_success(f"Found {len(internal_links)} internal pages. Now digging deeper...")

    targets_to_scan = set()

    for link in internal_links:
        if "=" in link:
            targets_to_scan.add(link)

    current_console = return_console()
    count = 0
    with current_console.status("Digging into pages...") as status:
        for page in internal_links:
            count += 1
            if count % 3 == 0:
                print(f" ...Done with page {count}/{len(internal_links)}")

            sub_links = get_all_links(page)
            for sub_link in sub_links:
                if "=" in sub_link and urlparse(sub_link).netloc == base_domain:
                    targets_to_scan.add(sub_link)

    if not targets_to_scan:
        print_error("Still no parameters found. The site might use REST API or JavaScript navigation.")
        return

    print_success(f"{print_info_label("PHASE 2")} Attack Started! Found {len(targets_to_scan)} unique targets with parameters.")
    print("-" * 50)

    for i, target in enumerate(targets_to_scan, 1):
        print(f"Target {i}/{len(targets_to_scan)}: {target}")
        scan_url(target)
        print("-" * 20)

if __name__ == "__main__":
    run_full_scan()
