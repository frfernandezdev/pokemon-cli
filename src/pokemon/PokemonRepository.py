import requests
from .PokemonPagination import PokemonPagination
from .ClientRequestFactory import ClientRequestFactory


class PokemonRepository:
    def __init__(self, request: ClientRequestFactory):
        self.__request = request
        self.__pagination = PokemonPagination(request)

    def pagination(self):
        self.__pagination.get()
        return self.__pagination

    def filterPaginationByName(self, name):
        return next(item for item in self.__pagination.items if item["name"] == name)

    def findOne(self, url):
        return self.__request.request("get", url)
