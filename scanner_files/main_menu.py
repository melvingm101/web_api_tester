import sys
from pathlib import Path
from utils.output_print import print_panel, print_tree, print_info, print_interactive_selection

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
        "Welcome to the Website Security Tester. Please choose among the options below in order to proceed.",
        ":globe_with_meridians: Web Security Tester"
    )
    final_item = print_interactive_selection("Website Tester Menu", [
        { "title": "Check details of website (Passive)", "value": 1 },
        { "title": "Active Scan (Single URL)", "value": 2 },
        { "title": "Web Crawler", "value": 3 },
        { "title": "Full Auto Scan", "value": 4 },
        { "title": "Exit", "value": 5 },
    ])

    if final_item is None:
        sys.exit(5)
    else:
        sys.exit(final_item)

if __name__ == "__main__":
    if sys.argv[1] == "main_menu":
        main_menu()
    elif sys.argv[1] == "basic_info":
        basic_info()
