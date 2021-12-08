class Trainer:
    def __init__(self):
        self.name = None
        self.caught_up = []

    def add_caught_up(self, pokemon):
        self.caught_up.append(pokemon)

    def remove_caught_up(self, pokemon):
        self.caught_up.remove(pokemon)

    def filter_by_name(self, name):
        return next(filter(lambda x: x["name"] == name, self.caught_up), None)
