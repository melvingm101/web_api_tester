import sys
from pathlib import Path
from utils.output_print import print_panel, print_tree, print_info

def clickjacking():
    """
    This clickjacking function prints the introduction of the clickjacking section. 
    """
    print_panel(
        "Clickjacking is a method of tricking users on clicking on items which indirectly causes other actions to occur, such as tricking users into clicking on a button to get a free iPad, but instead their messages in another app is deleted.",
        "What is clickjacking?"
    )

    print_info(f"Before proceeding, please ensure to check if your clickjacking template is present in this directory with the filename clickjacking_template.html: {Path.cwd()}/templates")
    print_info("If template is placed, please type the website you wish to test clickjacking on: ")



def main_menu():
    """
    This main_menu function is used to print the main menu when the user runs ./main.sh
    """
    print_panel(
        "Welcome to the Web API Tester. Please choose among these options in order to proceed.",
        "Web API Tester"
    )

    print_tree(
        ["1) Check details of given website", "2) Clickjacking test", "3) Exit"]
    )

    print_info("Please type any of the options above to continue (1, 2, 3):")

if __name__ == "__main__":
    if sys.argv[1] == "main_menu":
        main_menu()
    elif sys.argv[1] == "clickjacking":
        clickjacking()