import os
from Spinner import Spinner
from simple_term_menu import TerminalMenu


class App:
    def __init__(self):
        self.spinner = Spinner()
        self.terminal_menu = TerminalMenu

    def clear_window(self):
        os.system("clear")

    def run(self):
        self.clear_window()
        self.render()
