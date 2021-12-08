from halo import Halo


class Spinner:
    def __init__(self):
        self.__spinner = Halo("Loading...")

    def start(self):
        self.__spinner.start()

    def stop(self):
        self.__spinner.stop()
