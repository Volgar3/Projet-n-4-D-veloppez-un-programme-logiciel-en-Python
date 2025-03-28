from random import shuffle

class Player:
    def __init__(self, first_name, last_name, date_of_birth, points, matricule):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.points = points
        self.matricule = matricule

class Tournement:
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.location = kwargs.get('location')
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')
        self.number_of_rounds = kwargs.get('number_of_rounds', 4)
        self.current_round = kwargs.get('current_round', 0)
        self.description = kwargs.get('description')
        self.rounds = [] # Objets Round
        self.players = [] # Objets Match
        self.matches = [] # Objets Match
        self.selected_players = kwargs.get('selected_players')
class Round:
    
    def __init__(self, current_round):
        self.matches = []
        self.already_played_matches = {}
        self.current_round = current_round
        
        self.players = []
        self.matches = []
        self.already_played_matches = {}
        
    def create_matches(self, player_manager):
        """Création des matchs."""

        # Chargement des joueurs
        self.players = player_manager.selected_players()
        self.already_played_matches = {}
        matches = []
        if self.current_round == 0:
            shuffle(self.players)

            matches = [self.players[i:i+2] for i in range(int(round(len(self.players) / 2)))]
            print(matches)
        else:
            self.players.sort(key=lambda x: x[1], reverse=True)
            matches = [self.players[i:i+2] for i in range(int(round(len(self.players) / 2)))]
            # TODO: Use already played matches to avoid two players playing together multiples times in tournament
            # A completer à la fin du projet

        # TODO: Update already played matches after round winner attribution
        return self.matches

            