#!/bin/bash
choice=$(python main_menu.py "main_menu" < /dev/tty)

case $choice in
    "Check details of website (Passive)")./webcheck.sh;;
    "Active Scan (Single URL)") python active_scan.py;;
    "Web Crawler") python crawler.py;;
    "Full Auto Scan") python full_scanner.py;;
    "Exit")echo "Exiting now...";;
    *)echo "Wrong option. Exiting now...";;
esac