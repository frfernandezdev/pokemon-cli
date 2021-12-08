from App import App
from pokemon.PokemonView import PokemonView
from trainer.TrainerView import TrainerView
from MenuView import MenuView


class PokemonCLI(App):
    def __init__(self):
        App.__init__(self)
        self.page = 0

        self.trainer_view = TrainerView(self)
        self.menu_view = MenuView(self)
        self.pokemon_view = PokemonView(self)

    def render(self):
        if self.page == 0:
            self.trainer_view.run()
        if self.page == 1:
            self.menu_view.run()
        if self.page == 2:
            self.pokemon_view.run()
