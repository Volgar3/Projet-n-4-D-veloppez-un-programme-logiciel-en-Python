from abc import ABC

class Manager(ABC):
    pass

class PlayerManager(Manager):
    def __init__(self):
        self.players = []

    def add_player(self):
        return

class TournamentManager(Manager):
    pass