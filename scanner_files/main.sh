#!/bin/bash
python main_menu.py "main_menu"
read choice
case $choice in
    1)./webcheck.sh;;
    2) python full_scanner.py;;
    3) python active_scan.py;;
    4) python crawler.py;;
    5)./clickjacking.sh;;
    6)echo "Exiting now...";;
    *)echo "Wrong option. Exiting now...";;
esac