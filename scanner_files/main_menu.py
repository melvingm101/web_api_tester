import sys
from pathlib import Path
from utils.output_print import print_panel, print_tree, print_info, print_no_style, add_padding

def basic_info():
    """
    This function prints the introduction for basic website scan
    """
    print_panel(
        "A passive scan to check basic details about the website",
        ":clipboard: Passive scan"
    )


def main_menu():
    """
    This main_menu function is used to print the main menu when the user runs ./main.sh
    """
    print_panel(
        "Welcome to the Web API Tester. Please choose among the options below in order to proceed.",
        ":globe_with_meridians: Web API Tester"
    )

    print_tree(
        [
            "1) Check details of website (Passive)",
            "2) Active Scan (Single URL)",
            "3) Web Crawler",
            "4) Full Auto Scan",
            "5) Exit"
        ]
    )

    print_info("Please type any of the options above to continue [bold][1/2/3/4/5]:")

if __name__ == "__main__":
    if sys.argv[1] == "main_menu":
        main_menu()
    elif sys.argv[1] == "basic_info":
        basic_info()