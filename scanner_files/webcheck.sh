#!/bin/bash
echo "Please enter the website you wish to scan: "
read website_name

# website_name would contain something like http://test-website:3000
# This line is to delete any existing scan_report.json files in current directory
rm -f scan_report.json

# This will run whatweb which will provide a lengthy verbose output with -v
# Aggressive setting is set to 3 with -a 3
# Output is logged in scan_report.json
mkdir webscan
whatweb -q --log-json=$(pwd)/webscan/scan_report.json -a 3 $website_name
python basic_info.py