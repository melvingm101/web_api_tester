#!/bin/bash
echo "Please enter the website you wish to scan: "
read website_name

# website_name would contain something like http://test-website:3000
whatweb -v -a 3 $website_name