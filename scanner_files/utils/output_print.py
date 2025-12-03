# This file is for formatting the text output
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree

custom_theme = Theme({
    "info": "cyan3",
    "warning": "sky_blue1",
    "danger": "red3",
    "success": "green",
    "repr.number": "bold sky_blue1"
})

console=Console(theme=custom_theme)

def print_console_test(message):
    console.print(message)

def print_info(message):
    console.print(message, style="info")

def print_tree(options_list):
    tree = Tree("Options")
    for option in options_list:
        tree.add(option)
    
    console.print(tree)

def print_panel(message, heading):
    console.print(Panel(message, title=heading), style="info", justify="center")

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
    
    console.print(table)

def print_success(message):
    """
    print_success will print the success message on terminal based on the theme.

    :param message: Message that needs to be printed out
    """
    console.print(message, style="success")

def print_error(message):
    """
    print_error will print the error message on terminal based on the theme.

    :param message: Message that needs to be printed out
    """
    console.print(message, style="danger")

def print_progress_bar(func, message, *args):
    with console.status(message) as status:
        func(*args)
