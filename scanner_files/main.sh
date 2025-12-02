#!/bin/bash
python main_menu.py
read choice
case $choice in
    1)./webcheck.sh;;
    *)echo "Wrong option. Exiting now...";;
esac