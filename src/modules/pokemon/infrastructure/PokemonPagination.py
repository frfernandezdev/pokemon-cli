from .ClientRequestFactory import ClientRequestFactory


class PokemonPagination:
    def __init__(self, client: ClientRequestFactory):
        self.__client = client
        self.__url = "https://pokeapi.co/api/v2/pokemon"
        self.__next = None
        self.__previous = None

        self.count = 0
        self.items = []

    def get(self):
        response = self.__client.request("get", self.__url)
        self.__next = response["next"]
        self.__prev = response["previous"]
        self.count = response["count"]
        self.items = response["results"]

    def next(self):
        if not self.__next:
            return
        self.__url = self.__next
        self.get()

    def prev(self):
        if not self.__prev:
            return
        self.__url = self.__prev
        self.get()
