# This file is for formatting the text output
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from time import sleep

custom_theme = Theme({
    "info": "cyan3",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
    "repr.number": "bold green"
})

console=Console(theme=custom_theme)

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
