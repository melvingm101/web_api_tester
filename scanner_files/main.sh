#!/bin/bash
python $(pwd)/utils/output_print.py "print_panel" "Welcome to the Web API Tester. Please choose among these options in order to proceed." "Web API Tester"
python $(pwd)/utils/output_print.py "print_tree" "1) Check details of given website" "2) Exit"

echo "Please type any of the options above to continue (1, 2):"
read choice
case $choice in
    1)./webcheck.sh;;
    *)echo "Wrong option. Exiting now...";;
esac