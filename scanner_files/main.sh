#!/bin/bash
python main_menu.py "main_menu"
read choice
case $choice in
    1)./webcheck.sh;;
    2)./clickjacking.sh;;
    3)echo "Exiting now...";;
    *)echo "Wrong option. Exiting now...";;
esac