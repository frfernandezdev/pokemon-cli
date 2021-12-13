import sys
from ...core.infrastructure.App import App
from ...core.infrastructure.ClientRequestFactory import ClientRequestFactory
from ...pokemon.infrastructure.PokemonRepository import PokemonRepository
from ...trainer.domain.Trainer import Trainer
from ...trainer.application.TrainerAskView import TrainerAskView
from ...trainer.application.TrainerSinglePokemonView import TrainerSinglePokemonView
from ...trainer.application.TrainerPokemonView import TrainerPokemonView


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
