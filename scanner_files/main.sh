#!/bin/bash
python main_menu.py
read choice
case $choice in
    1)./webcheck.sh;;
    2)echo "Exiting now...";;
    *)echo "Wrong option. Exiting now...";;
esac