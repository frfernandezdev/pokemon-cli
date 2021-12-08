from App import App


class MenuView(App):
    def __init__(self, parent):
        App.__init__(self)
        self.parent = parent
        self.trainer = parent.trainer_view.trainer

    def render(self):
        trainer_name = self.trainer.name
        print("Welcome to back %s" % trainer_name)

        options = []
        options.append("Let's catch pokemon")
        options.append("See my pokemon")
        menu = self.terminal_menu(options)
        select = menu.show()

        if select is None:
            return

        select = int(select)
        if select == 0:
            self.parent.page = 2
            self.parent.pokemon_view.page = 0
        if select == 1:
            self.parent.page = 0
            self.parent.trainer_view.page = 1

        self.parent.render()
