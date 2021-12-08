#!/bin/python3
# import os
# import sys
# import requests
# from halo import Halo
# from simple_term_menu import TerminalMenu


# class PokemonRequest:
#    def __init__(self, url, **params):
#        self.__cursor = 0
#        self.__url = url
#        self.__params = params
#
#    def request(self):
#        try:
#            self.__request = requests.get(self.__url, self.__params)
#            return self.__request.json()
#        except requests.exceptions.RequestException as e:
#            print("Error to get pokemons: %s" % str(e))
#
#
# class Pokemon:
#    def __init__(
#        self,
#        _id=0,
#        name="",
#        height=0,
#        weight=0,
#        order=0,
#        base_experience=0,
#        held_items=[],
#        is_default=False,
#        location_area_encounters="",
#        moves=[],
#        past_types=[],
#        species={},
#        sprites={},
#        stats=[],
#        types=[],
#        abilities=[],
#        forms=[],
#        url="",
#    ):
#        self._id = _id
#        self.name = name
#        self.height = height
#        self.weight = weight
#        self.order = order
#        self.base_experience = base_experience
#        self.held_items = held_items
#        self.is_default = is_default
#        self.location_area_encounters = location_area_encounters
#        self.moves = moves
#        self.past_types = past_types
#        self.species = species
#        self.sprites = sprites
#        self.stats = stats
#        self.types = types
#        self.abilities = abilities
#        self.forms = forms
#        self.url = url
#
#    @classmethod
#    def from_list(self, _list):
#        return [Pokemon(name=item["name"], url=item["url"]) for item in _list]
#
#    def get_detail(self):
#        result = PokemonRequest(self.url).request()
#        return Pokemon(
#            _id=result["id"],
#            name=result["name"],
#            height=result["height"],
#            weight=result["weight"],
#            order=result["order"],
#            base_experience=result["base_experience"],
#            held_items=result["held_items"],
#            is_default=result["is_default"],
#            location_area_encounters=result["location_area_encounters"],
#            moves=result["moves"],
#            past_types=result["past_types"],
#            species=result["species"],
#            sprites=result["sprites"],
#            types=result["types"],
#            abilities=result["abilities"],
#            forms=result["forms"],
#            url=self.url,
#        )
#
#    def render_details(self):
#        text = ""
#        text += "  Id: %s\n" % self._id
#        text += "  Name: %s\n" % self.name
#        text += "  Height: %s (cm)\n" % (self.height * 10)
#        text += "  Weight: %s (gr)\n" % (self.weight * 100)
#        text += "  Order: %s\n" % self.order
#        text += "  Base Experience: %s\n" % self.base_experience
#        text += "  Specie: %s\n" % self.species["name"]
#        print(text)
#
#
# class PokemonPagination:
#    def __init__(self):
#        self.__url = "https://pokeapi.co/api/v2/pokemon"
#        self.__next = None
#        self.__previous = None
#
#        self.count = 0
#        self.results = []
#        self.__response = None
#
#    def get(self):
#        self.__request()
#
#    def __request(self):
#        self.__response = PokemonRequest(self.__url).request()
#        self.__deserialize()
#
#    def __deserialize(self):
#        self.count = self.__response["count"]
#        self.__next = self.__response["next"]
#        self.__previous = self.__response["previous"]
#        self.results = Pokemon.from_list(self.__response["results"])
#
#    def next(self):
#        if not self.__next:
#            return None
#        self.__url = self.__next
#        self.__request()
#        self.__deserialize()
#
#    def previous(self):
#        if not self.__previous:
#            return None
#        self.__url = self.__previous
#        self.__request()
#        self.__deserialize()
#
#
# class Spinner:
#    def __init__(self):
#        self.__spinner = Halo("Loading...")
#
#    def start(self):
#        self.__spinner.start()
#
#    def stop(self):
#        self.__spinner.stop()
#
#
# class PokemonCLI:
#    def __init__(self):
#        self.__page = 0
#        self.__trainer = None
#        self.__spinner = Spinner()
#        self.__options = []
#        self.__input = None
#        self.__select = None
#        self.__request = PokemonPagination()
#
#    def __is_next(self):
#        return self.__select == (len(self.__options) - 2)
#
#    def __is_prev(self):
#        return self.__select == (len(self.__options) - 1)
#
#    def __load_pokemons(self):
#        self.__spinner.start()
#        self.__request.get()
#        self.__spinner.stop()
#
#    def __clear_window(self):
#        os.system("clear")
#
#    def __re_render(self):
#        self.__clear_window()
#        self.__options = []
#        self.__render()
#
#    def __render_header(self, title):
#        print("%s \n" % title)
#
#    def __render_ask_keep_looking_or_catch(self):
#        option = self.__options[self.__select]
#        pokemon = next(item for item in self.__request.results if option == item.name)
#
#        try:
#            self.__spinner.start()
#            __pokemon = pokemon.get_detail()
#            self.__spinner.stop()
#
#            self.__render_header("You selected (%s)" % __pokemon.name)
#            __pokemon.render_details()
#
#            answer = input(
#                "Trainer wants to catch (%s)?, or you want to keep looking: (Y/n): "
#                % __pokemon.name
#            )
#        except KeyboardInterrupt as e:
#            sys.exit()
#
#        print("\n")
#
#        if answer.lower() == "y":
#            # send event
#            pass
#
#        self.__page = 2
#        self.__re_render()
#
#    def __render_ask_trainer_name(self):
#        try:
#            self.__trainer = input("Trainer what's your name?\n")
#            self.__page = 1
#            self.__re_render()
#        except KeyboardInterrupt as e:
#            sys.exit()
#
#    def __render_page_list_pokemon(self):
#        self.__render_header("Welcome to back %s" % (self.__trainer or "Trainer"))
#        self.__load_pokemons()
#        for item in self.__request.results:
#            self.__options.append(item.name)
#        self.__options.append("---------")
#        self.__options.append("Next page")
#        self.__options.append("Prev page")
#        select = TerminalMenu(self.__options)
#        self.__select = select.show()
#
#        if self.__select is None:
#            sys.exit()
#
#        if self.__is_next() or self.__is_prev():
#            if self.__is_next():
#                self.__request.next()
#            if self.__is_prev():
#                self.__request.previous()
#            self.__re_render()
#
#        self.__page = 3
#        self.__clear_window()
#
#    def __render(self):
#        if self.__page == 0:
#            self.__render_ask_trainer_name()
#        if self.__page == 1:
#            self.__render_page_list_pokemon()
#        if self.__page == 2:
#            self.__render_ask_keep_looking_or_catch()
#
#    def run(self):
#        self.__render()


from PokemonCLI import PokemonCLI


def main():
    PokemonCLI().run()


if __name__ == "__main__":
    main()
