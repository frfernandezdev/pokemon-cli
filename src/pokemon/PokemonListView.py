import re
from App import App
from .ClientRequestFactory import ClientRequestFactory
from .PokemonRepository import PokemonRepository


class PokemonListView(App):
    def __init__(self, parent):
        App.__init__(self)

        self.parent = parent
        self.trainer = parent.parent.trainer_view.trainer

        request = ClientRequestFactory()
        self.repository = PokemonRepository(request)

    def is_back(self, select, options):
        return select == (len(options) - 1)

    def is_next(self, select, options):
        return select == (len(options) - 3)

    def is_prev(self, select, options):
        return select == (len(options) - 2)

    def render(self):
        options = []
        self.spinner.start()
        pagination = self.repository.pagination()
        self.spinner.stop()

        self.clear_window()
        print("List Pokemon")

        for item in pagination.items:
            if self.trainer.filter_by_name(item["name"]):
                options.append("x %s" % item["name"])
                continue
            options.append("  %s" % item["name"])
        options.append("---------")
        options.append("Next page")
        options.append("Prev page")
        options.append("Back")
        menu = self.terminal_menu(options)
        select = menu.show()

        if select is None:
            return sys.exit()

        select = int(select)
        if self.is_back(select, options):
            self.parent.parent.page = 1
            return self.parent.parent.render()
        if self.is_next(select, options):
            pagination.next()
            return self.render()
        if self.is_prev(select, options):
            pagination.prev()
            return self.render()

        pokemon_name = options[select]
        pokemon_name = re.sub(r"^x?(\s)", "", pokemon_name).strip()
        self.parent.pokemon_select = self.repository.filterPaginationByName(
            pokemon_name
        )
        self.parent.page = 1
