from random import shuffle

class Player:
    def __init__(self, first_name, last_name, date_of_birth, points, ID):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.points = points
        self.ID = ID

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
    
    def __init__(self, current_round, players=None):
        self.current_round = current_round
        self.players = players or []
        self.matches = []
        self.already_played_matches = {}
        
    def create_matches(self, player_manager=None):
        """Création des matchs."""
        
        if not self.players:
            print("Aucun joueur dans le round, impossible de créer les matchs.")
            return []

        if self.current_round == 1:
            shuffle(self.players)
        else:
            self.players.sort(key=lambda x: x.points, reverse=True)

        self.matches = [
            (self.players[i], self.players[i + 1])
            for i in range(0, len(self.players) - 1, 2)
        ]

        return self.matches

        # TODO: Update already played matches after round winner attribution

    def result_round(self):
        """Update points after round."""
    
        print(f"\n--- Résultats du Round {self.current_round} ---")
        for match in self.matches:
            player1, player2 = match
            print(f"{player1.first_name} {player1.last_name} vs {player2.first_name} {player2.last_name}")
            result = input("Qui a gagné ? (1 = joueur 1, 2 = joueur 2, 0 = match nul) : ")

            if result == "1":
                player1.points += 1
            elif result == "2":
                player2.points += 1
            elif result == "0":
                player1.points += 0.5
                player2.points += 0.5
            else:
                print("Entrée invalide. Aucun point attribué.")