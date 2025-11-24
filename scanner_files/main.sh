#!/bin/bash
echo "Welcome to the Web API Tester"
echo "Please type the option to continue:"
echo "1: Check web technologies in given website"
echo
read choice
case $choice in
    1)./webscan/webcheck.sh;;
    *)echo "Wrong option. Exiting now...";;
esac