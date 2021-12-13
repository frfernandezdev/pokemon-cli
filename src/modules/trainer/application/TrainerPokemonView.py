from ...core.infrastructure.App import App


class TrainerPokemonView(App):
    def __init__(self, parent):
        App.__init__(self)

        self.parent = parent
        self.trainer = parent.trainer

    def is_back(self, select, options):
        return select == (len(options) - 1)

    def is_next(self, select, options):
        return select == (len(options) - 3)

    def is_prev(self, select, options):
        return select == (len(options) - 2)

    def render(self):
        print("My Pokemon")

        options = []
        for item in self.trainer.caught_up:
            options.append(item["name"])
        options.append("---------")
        options.append("Back")
        menu = self.terminal_menu(options)
        select = menu.show()

        if select is None:
            return

        select = int(select)
        if self.is_back(select, options):
            self.parent.parent.page = 1
            return self.parent.parent.render()

        pokemon_name = options[select]
        self.parent.pokemon_select = self.trainer.filter_by_name(pokemon_name)
        self.parent.page = 2
