import sys
import nvdlib

from utils.output_print import print_error, print_success, print_progress_bar, print_table, print_info, print_panel
from utils.file_process import parse_json
from utils.parse_headers import parse_x_powered_by
from utils.clickjacking import is_clickjacking_possible

def discover_cves(params):
    search_params = { "keywordSearch": params }

    try:
        cpe_results = nvdlib.searchCPE(
            keywordSearch=params,
            keywordExactMatch=True, # Forces phrase matching for precision
            limit=1, 
        )

        print_success("CPE found: ", cpe_results)

        # This searches the CVE database for keywords like apache 2.4.4 to find vulnerabilities
        vuln_list = nvdlib.searchCVE(**search_params)
        vuln_count = len(vuln_list)

        if vuln_count > 0:
            # Gets a list of high/critical vulnerabilities
            critical_issues = [
                (cve_data.id, str(cve_data.score[1]), cve_data.score[2], cve_data.url) 
                for cve_data in vuln_list if cve_data.score[2] in ["HIGH", "CRITICAL"]
            ]
            
            # The vulnerabilities are now listed.
            print_error(f"[danger]{vuln_count} vulnerability records present", (0, 0))
            if len(critical_issues) > 0:
                print_error(f"Some high/critical CVE records include:", (0, 0))
                print_table("",
                [
                    { "name": "CVE ID", "style": "info" },
                    { "name": "Score", "style": "warning" },
                    { "name": "Category", "style": "danger" },
                    { "name": "URL", "style": "info" },
                ],
                critical_issues
            )
        
    except Exception as e:
        print(f"Error during CVE search: {e}")

def loop_through_cves(services):
    for service in services:
        print_info(f"Technology found: {service}")
        discover_cves(service)

# This function will read and parse the JSON provided by whatweb
def read_scan_report(data_string):
    # Check if JSON file exists
    
    try:
        # Pass the scan report and get website details, services and other information
        website_details, services, other_info = parse_json(data_string)

        # This check is for PHP, as it also provides version along with technology
        if "X-Powered-By" in other_info:
            if 'php' in other_info["X-Powered-By"].lower():
                php_tech, php_ver = parse_x_powered_by(other_info["X-Powered-By"])
                if any("php" in single_service.lower() for single_service in services):
                    new_services = [
                        item for item in services if "php" not in item.lower()
                    ]
                    services = new_services
                services.append(f"{php_tech} {php_ver}")

        # Check if there are any services listed
        if len(services) > 0:
            # Find CVEs associated with the service
            print_progress_bar(loop_through_cves, "[info]Searching for CVEs...", services)
        
        # Print the other information in a table
        print_success(f"More details about {website_details["target"]}:", (0, 0))
        print_table("",
            [
                { "name": "Header info", "style": "info" },
                { "name": "Value", "style": "warning" },
            ],
            [
                (info_key, info_value) for info_key, info_value in other_info.items()
            ]
        )

        print_panel(
            "Clickjacking is a method of tricking users on clicking on items which indirectly causes other actions to occur. Eg: tricking users into clicking on a button to get a free iPad, but instead their messages in the vulnerable application is deleted.",
            ":exclamation_question_mark: What is clickjacking?"
        )
        clickjacking_support = is_clickjacking_possible(header_info=other_info)
        if not clickjacking_support:
            print_success("X-Frame-Options/CSP headers are in place, the provided website is safe from clickjacking")
        else:
            print_error("No X-Frame-Options or CSP Headers present, website is vulnerable to clickjacking.")
    except Exception as e:
        # Handle other general errors
        print_error(f"An unexpected error occurred. Check if the website URL is correct and re-run the scan again.")
        print(e)

json_data_string = sys.stdin.read()
if not json_data_string:
    print_error("Error: No JSON data received from WhatWeb.")
else:
    read_scan_report(json_data_string)