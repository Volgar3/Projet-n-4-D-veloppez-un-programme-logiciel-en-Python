from random import shuffle


class Player:
    def __init__(self, first_name, last_name, date_of_birth, points, ID):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.points = points
        self.ID = ID

    def player_to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "points": self.points,
            "ID": self.ID
        }
    @classmethod
    def player_from_dict(cls, data):
        return cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            date_of_birth=data.get("date_of_birth"),
            points=float(data.get("points", 0)),
            ID=data.get("ID")
        )


class Tournament:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.location = kwargs.get("location")
        self.start_date = kwargs.get("start_date")
        self.end_date = kwargs.get("end_date")
        self.number_of_rounds = int(kwargs.get("number_of_rounds", 4))
        self.current_round = int(kwargs.get("current_round", 0))
        self.description = kwargs.get("description")
        self.rounds = []  # Objets Round
        self.players = []  # Objets Player
        self.matches = []  # Objets Match
        self.selected_players = kwargs.get("selected_players")
        self.round_result = kwargs.get("round_result", [])

    def tournament_to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "selected_players": self.selected_players,
            "round_result": self.round_result,
            "rounds": self.rounds,
            "matches": self.matches
        }
        
    @classmethod
    def tournament_from_dict(cls, data):
        return cls(**data)
    
class Round:
    def __init__(self, current_round, already_played_matches=[], players=None):
        self.current_round = current_round
        self.players = players or []
        self.matches = []
        self.already_played_matches = already_played_matches

    def create_matches(self, previous_rounds):
        print(self.already_played_matches)
        """Création des matchs."""
        if not self.players:
            print("Aucun joueur dans le round, impossible de créer les matchs.")
            return []
        
        if self.current_round == 1:
            shuffle(self.players)
        else:
            # Trier les joueurs par score décroissant
            self.players.sort(key=lambda x: x.points, reverse=True)

            # Enregistrer les IDs des matchs déjà joués
            played_pairs = set(
                (min(p1.ID, p2.ID), max(p1.ID, p2.ID))
                for round in previous_rounds
                for p1, p2 in round.matches
            )

            self.matches = []
            i = 0
            while i < len(self.players) - 1:
                p1, p2 = self.players[i], self.players[i + 1]
                pair = (min(p1.ID, p2.ID), max(p1.ID, p2.ID))

                if pair not in played_pairs:
                    self.matches.append((p1, p2))
                    i += 2
                else:
                    # Tenter un swap pour éviter un doublon
                    if i + 2 < len(self.players):
                        self.players[i + 1], self.players[i + 2] = self.players[i + 2], self.players[i + 1]
                    else:
                        # Si pas possible, on valide quand même le match
                        self.matches.append((p1, p2))
                        i += 2

        return self.matches

    def result_round(self):
        """Mise à jour des points après le round."""
        print("\nListe des matchs :")
        for i, match in enumerate(self.matches, start=1):
            p1, p2 = match
            print(f"{i}. {p1.first_name} vs {p2.first_name}")

        print(f"\n--- Résultats du Round {self.current_round} ---")
        for match in self.matches:
            player1, player2 = match
            print(f"{player1.first_name} {player1.last_name} vs "
                  f"{player2.first_name} {player2.last_name}")
            result = input(
                "Qui a gagné ? (1 = joueur 1, 2 = joueur 2, 0 = match nul) : "
            )

            if result == "1":
                player1.points += 1
            elif result == "2":
                player2.points += 1
            else:
                print("Entrée invalide. Aucun point attribué.")
            

    def to_result_dict(self):
        result_data = {}
        for i, (p1, p2) in enumerate(self.matches, start=1):
            if p1.points > p2.points:
                result = f"{p1.first_name} win - {p2.first_name} lose"
            elif p2.points > p1.points:
                result = f"{p1.first_name} lose - {p2.first_name} win"
            else:
                result = f"{p1.first_name} draw - {p2.first_name} draw"

            result_data[f"match {i}"] = result

        return {f"round {self.current_round}": result_data}
    
    def to_dict(self):
        return {
            "current_round": self.current_round,
            "matches": [
                (p1.ID, p2.ID) for p1, p2 in self.matches
            ],
            "players": [player.ID for player in self.players]
        }