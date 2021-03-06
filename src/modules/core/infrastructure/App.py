import os
from simple_term_menu import TerminalMenu
from .Spinner import Spinner


class App:
    def __init__(self):
        self.spinner = Spinner()
        self.terminal_menu = TerminalMenu

    def clear_window(self):
        os.system("clear")

    def run(self):
        self.clear_window()
        self.render()
