# This file is for formatting the text output
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from rich.padding import Padding
import questionary

custom_theme = Theme({
    "regular": "#EFEFEF",
    "info": "#65CCFF",
    "warning": "#FFFC31",
    "danger": "#D1345B"+ " bold",
    "success": "#1EFFBC" + " bold",
    "error_label": "bold reverse #D1345B",
    "success_label": "bold reverse #1EFFBC",
    "info_label": "bold reverse #65CCFF"
})

console=Console(theme=custom_theme)

def print_interactive_selection(question, question_list):
    final_item = questionary.select(
        question,
        choices=[
            questionary.Choice(
                title=question["title"],
                value=question["value"] 
            ) for question in question_list
        ],
    ).ask()

    return final_item

def print_info_label(message):
    return f"[info_label] {message} [/info_label]"

def print_success_label(message):
    return f"[success_label] {message} [/success_label]"

def print_error_label(message):
    return f"[error_label] {message} [/error_label]"

def return_console():
    return console

def add_padding(item, padding_tuple):
    """
    add_padding adds padding around the element
    
    :param item: Item where we need to add padding. Can be text, panel, tree etc.
    :param padding_tuple: Should be in format (x, y), where x -> top/bottom padding and y -> left/right padding
    """
    return Padding(
        item,
        padding_tuple
    )

def print_no_style(message):
    console.print(message)

def print_info(message):
    console.print(message, style="info")

def print_tree(options_list):
    tree = Tree("Options", guide_style="bold")
    for option in options_list:
        tree.add(option)
    
    console.print(tree)

def print_panel(message, heading):
    console.print(
        add_padding(
            Panel(f"[italic][regular]{message}", title=heading),
            (2, 4)
        ),
        style="info", justify="center"
    )

def print_table(table_title, columns, data_tuple_list):
    """
    print_table prints out a table with title, columns and populated data in the terminal
    applying colorful themes
    
    :param table_title: Title of the table, can be kept empty
    :param columns: Column of the table, must be a dictionary of type {"name": "", "style": ""}.  
    :param data_tuple_list: Data of the table which we need to populate the table. 
    """
    table = Table(title=table_title)
    for column in columns:
        table.add_column(column["name"], style=column["style"])
    
    for data_item in data_tuple_list:
        table.add_row(*data_item)
    
    console.print(add_padding(table, (1, 0)))

def print_success(message, padding_tuple=(1, 0)):
    """
    print_success will print the success message on terminal based on the theme.

    :param message: Message that needs to be printed out
    """
    console.print(add_padding(f":white_check_mark: {message}", padding_tuple), style="success")

def print_error(message, padding_tuple=(1, 0)):
    """
    print_error will print the error message on terminal based on the theme.

    :param message: Message that needs to be printed out
    """
    console.print(add_padding(f":cross_mark: {message}", padding_tuple), style="danger")

def print_progress_bar(func, message, *args):
    with console.status(message) as status:
        func(*args)
