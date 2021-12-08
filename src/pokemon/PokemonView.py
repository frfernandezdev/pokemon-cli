from App import App

from .PokemonListView import PokemonListView
from .PokemonSingleView import PokemonSingleView


class PokemonView(App):
    def __init__(self, parent):
        App.__init__(self)

        self.page = 0
        self.pokemon_select = None
        self.parent = parent

        self.list_pokemon = PokemonListView(self)
        self.single_pokemon = PokemonSingleView(self)

    def render(self):
        if self.page == 0:
            self.list_pokemon.run()
        if self.page == 1:
            self.single_pokemon.run()
