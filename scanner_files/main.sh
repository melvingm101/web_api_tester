#!/bin/bash
python $(pwd)/utils/output_print.py "print_panel" "Welcome to the Web API Tester. Please choose among these options in order to proceed." "Web API Tester"
echo "1: Check web technologies in given website"
echo "Please type the option to continue (1):"
read choice
case $choice in
    1)./webcheck.sh;;
    *)echo "Wrong option. Exiting now...";;
esac