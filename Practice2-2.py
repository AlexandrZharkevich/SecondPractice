# Классы – Море, Континент, Государство, Остров, Суша;


class Sea:
    def __init__(self, title):
        self.__title = title
        self.__islands = []

    def get_title(self):
        return self.__title

    def add_island(self, island):
        self.__islands.append(island)

    def show_islands(self):
        for i in range(len(self.__islands)):
            self.__islands[i].show_title()


class Land:
    def __init__(self):
        self.__states = []

    def add_state(self, state):
        self.__states.append(state)

    def show_states(self):
        for i in range(len(self.__states)):
            self.__states[i].show_title()


class Island(Land):
    def __init__(self, title):
        Land.__init__(self)
        self.__title = title

    def show_title(self):
        print(self.__title)

    def show_states(self):
        Land.show_states(self)


class State:
    def __init__(self, title):
        self.__title = title

    def show_title(self):
        print(self.__title)


belarus = State("Belarus")
madagascar = Island("Madagascar")
madagascar.add_state(belarus)
madagascar.show_title()
madagascar.show_states()
