# This file is for formatting the text output
from rich.console import Console, Text
from rich.style import Style
from rich.theme import Theme
from time import sleep

custom_theme = Theme({
    "info": "cyan3",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
    "repr.number": "bold green"
})

console=Console(theme=custom_theme)

def print_success(message):
    console.print(message, style="success")

def print_error(message):
    console.print(message, style="danger")

def print_progress_bar(func, message, **args):
    with console.status(message) as status:
        func(**args)
