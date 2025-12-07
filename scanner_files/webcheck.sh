#!/bin/bash
python main_menu.py "basic_info"
echo "Please enter the website you wish to scan: "
read website_name

# website_name would contain something like http://test-website:3000
# This line is to delete any existing scan_report.json files in current directory
rm -f scan_report.json

# This will run whatweb which will provide a lengthy verbose output with -v
# Output is logged in scan_report.json
mkdir -p webscan
whatweb -q --log-json=$(pwd)/webscan/scan_report.json $website_name
python basic_info.py
rm -f webscan/scan_report.json