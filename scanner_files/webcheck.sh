#!/bin/bash
python main_menu.py "basic_info"
echo "Please enter the website you wish to scan: "
read website_name

# website_name would contain something like http://test-website:3000
# This will run whatweb which will provide a lengthy verbose output with -v
# Whatweb results would be passed in the basic_info.py file
whatweb -q $website_name --log-json | python basic_info.py
