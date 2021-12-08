import sys
from App import App
from pokemon.ClientRequestFactory import ClientRequestFactory
from pokemon.PokemonRepository import PokemonRepository
from .Trainer import Trainer
from .TrainerAskView import TrainerAskView
from .TrainerSinglePokemonView import TrainerSinglePokemonView
from .TrainerPokemonView import TrainerPokemonView


class TrainerView(App):
    def __init__(self, parent):
        App.__init__(self)

        self.page = 0
        self.parent = parent
        self.trainer_pokemon = None
        self.trainer = Trainer()
        self.trainer_ask = TrainerAskView(self)
        self.trainer_pokemon = TrainerPokemonView(self)
        self.trainer_single_pokemon = TrainerSinglePokemonView(self)

    def render(self):
        if self.page == 0:
            self.trainer_ask.run()
        if self.page == 1:
            self.trainer_pokemon.run()
        if self.page == 2:
            self.trainer_single_pokemon.run()
