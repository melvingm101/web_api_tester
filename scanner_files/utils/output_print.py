# This file is for formatting the text output
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree

custom_theme = Theme({
    "info": "cyan3",
    "warning": "sky_blue1",
    "danger": "red",
    "success": "green",
    "repr.number": "bold sky_blue1"
})

console=Console(theme=custom_theme)

def print_info(message):
    console.print(message, style="info")

def print_tree(options_list):
    tree = Tree("Options")
    for option in options_list:
        tree.add(option)
    
    console.print(tree)

def print_panel(message, heading):
    console.print(Panel(message, title=heading), style="info", justify="center")

def print_log(message):
    console.log(message, style="info")

def print_table(table_title, columns, data_tuple_list):
    table = Table(title=table_title)
    for column in columns:
        table.add_column(column["name"], style=column["style"])
    
    for data_item in data_tuple_list:
        table.add_row(*data_item)
    
    console.print(table)

def print_success(message):
    console.print(message, style="success")

def print_error(message):
    console.print(message, style="danger")

def print_progress_bar(func, message, *args):
    with console.status(message) as status:
        func(*args)
