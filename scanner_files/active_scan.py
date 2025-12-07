import requests
import sys
from utils.output_print import print_error, print_success, print_info, print_panel

# 1. The scanning logic (Optimized for stability)
def scan_url(target_url):
    print_info(f"Scanning {target_url} ...")
    
    # --- SQL Injection Test ---
    sqli_payload = "'"
    sqli_url = target_url + sqli_payload
    
    try:
        # We added 'verify=False' to ignore SSL errors (common in test labs)
        # We catch specifically RequestException to handle connection errors gracefully
        response = requests.get(sqli_url, timeout=5, verify=False)
        
        sql_errors = [
            "You have an error in your SQL syntax",
            "Warning: mysql_",
            "Unclosed quotation mark after the character string",
            "Quote inside string",
            "SequelizeDatabaseError"
        ]
        
        is_sqli_vuln = False
        for error in sql_errors:
            if error in response.text:
                is_sqli_vuln = True
                break
        
        if is_sqli_vuln:
            print_error(f"[CRITICAL] Possible SQL Injection detected in {target_url}", (0, 0))
        else:
            print_success(f"[SAFE] No simple SQL errors in {target_url}", (0, 0))

    except requests.exceptions.RequestException:
        # This handles "Site Down", "Connection Refused", etc. quietly
        print_error(f"[!] Connection failed for SQLi test on {target_url}")
    except Exception as e:
        # This catches anything else weird
        print_error(f"[!] Unexpected error during SQLi test: {str(e).split('(')[0]}")

    # --- XSS Test ---
    xss_payload = "<script>alert('XSS')</script>"
    if "=" in target_url:
        try:
            base_url = target_url.split('=')[0] + "="
            xss_url = base_url + xss_payload

            response = requests.get(xss_url, timeout=5, verify=False)
            
            if xss_payload in response.text:
                print_error(f"[HIGH] Possible Reflected XSS detected in {target_url}", (0, 0))
            else:
                print_success(f"[SAFE] No XSS reflected in {target_url}", (0, 0))

        except requests.exceptions.RequestException:
             print_error(f"[!] Connection failed for XSS test on {target_url}")
        except Exception as e:
            print_error(f"[!] Unexpected error during XSS test: {str(e).split('(')[0]}")

# 2. The Main Menu (With Anti-Crash Protection)
def run_active_scan():
    print_panel("Active Vulnerability Scanner (SQLi & XSS)", "Active Scan")
    
    try:
        target_url = input("Enter the full URL to scan (e.g., http://testphp.vulnweb.com/artists.php?artist=1): ").strip()
        
        if not target_url:
            print_error("Error: You didn't enter a URL.")
            return

        if "=" not in target_url:
            print_error("Error: URL must contain parameters (e.g., ?id=1) to test for injections.")
            return

        scan_url(target_url)

    except KeyboardInterrupt:
        print("\n")
        print_error("[!] Scan cancelled by user. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    # We also wrap the startup to catch Ctrl+C immediately
    try:
        # Suppress annoying SSL warnings for cleaner output
        requests.packages.urllib3.disable_warnings()
        run_active_scan()
    except KeyboardInterrupt:
        print("\n")
        print_error("[!] Exiting...")
        sys.exit(0)
