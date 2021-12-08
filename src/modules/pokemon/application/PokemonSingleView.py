import sys
from ...core.infrastructure.App import App
from ...core.infrastructure.ClientRequestFactory import ClientRequestFactory
from ...pokemon.infrastructure.PokemonRepository import PokemonRepository


class PokemonSingleView(App):
    def __init__(self, parent):
        App.__init__(self)

        self.parent = parent
        self.trainer = parent.parent.trainer_view.trainer

        request = ClientRequestFactory()
        self.repository = PokemonRepository(request)

    def render(self):
        self.spinner.start()
        pokemon = self.repository.findOne(self.parent.pokemon_select["url"])
        self.spinner.stop()

        print("You selected (%s)\n" % pokemon["name"])

        text = ""
        text += "  Id: %s\n" % pokemon["id"]
        text += "  Name: %s\n" % pokemon["name"]
        text += "  Height: %s (cm)\n" % (pokemon["height"] * 10)
        text += "  Weight: %s (gr)\n" % (pokemon["weight"] * 100)
        text += "  Order: %s\n" % pokemon["order"]
        text += "  Base Experience: %s\n" % pokemon["base_experience"]
        text += "  Specie: %s\n" % pokemon["species"]["name"]
        text += "\n"
        text += (
            "Trainer wants to catch (%s)?, or you want to keep looking. (b) to return to the menu: (Y/n/b): "
            % pokemon["name"]
        )
        try:
            answer = input(text)
        except KeyboardInterrupt as e:
            sys.exit()

        if answer.lower() == "b":
            self.parent.parent.page = 1
            return self.parent.parent.render()

        if answer.lower() == "y":
            self.parent.page = 0
            self.trainer.add_caught_up(self.parent.pokemon_select)
            return self.parent.render()

        if answer.lower() == "n":
            self.parent.page = 0
            return self.parent.render()
