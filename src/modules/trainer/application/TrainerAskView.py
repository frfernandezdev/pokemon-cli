import sys
from App import App


class TrainerAskView(App):
    def __init__(self, parent):
        App.__init__(self)

        self.parent = parent
        self.trainer = parent.trainer

    def render(self):
        try:
            self.trainer.name = input("Trainer what's your name?\n")
            self.parent.parent.page = 1
        except KeyboardInterrupt as e:
            sys.exit()
