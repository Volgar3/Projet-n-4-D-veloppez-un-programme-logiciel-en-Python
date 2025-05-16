from random import shuffle


class Player:
    def __init__(self, first_name, last_name, date_of_birth, ID,
                 ID_played=None, points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.points = points
        self.ID = ID
        self.ID_played = ID_played or []

    def player_to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "points": self.points,
            "ID": self.ID,
            "ID_played": self.ID_played
        }

    @classmethod
    def player_from_dict(cls, data):
        return cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            date_of_birth=data.get("date_of_birth"),
            points=float(data.get("points", 0)),
            ID=data.get("ID"),
            ID_played=data.get("ID_played")
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
    def __init__(self, current_round, players=None):
        self.current_round = current_round
        self.players = players
        self.matches = []

    def create_matches(self, players):
        """Création des matchs."""
        if self.current_round == 1:  # Shuffle aléatoire pour le 1er round
            shuffle(self.players)
            self.matches = [
                (self.players[i], self.players[i + 1])
                for i in range(0, len(self.players) - 1, 2)
            ]
            for p1, p2 in self.matches:
                p1.ID_played.append(p2.ID)
                p2.ID_played.append(p1.ID)
        else:
            players_sorted = {}
            for player in self.players:
                if player.points not in players_sorted:
                    players_sorted[player.points] = []
                players_sorted[player.points].append(player)

            print("=== DEBUG players_sorted ===")
            for points, group in sorted(players_sorted.items(), reverse=True):
                print(f"Points: {points}")
                for player in group:
                    print(f"  - {player.first_name} {player.last_name} "
                          f"(ID: {player.ID})")

            for group in players_sorted.values():
                shuffle(group)

            unpaired_players = []
            for group in players_sorted.values():
                i = 0
                while i < len(group) - 1:
                    p1 = group[i]
                    found = False
                    for j in range(i + 1, len(group)):
                        p2 = group[j]
                        if (p2.ID not in p1.ID_played and
                                p1.ID not in p2.ID_played):
                            self.matches.append((p1, p2))
                            p1.ID_played.append(p2.ID)
                            p2.ID_played.append(p1.ID)
                            group.pop(j)
                            group.pop(i)
                            found = True
                            break
                    if not found:
                        i += 1
                unpaired_players.extend(group)

            i = 0  # Indexation dans unpaired_players
            while i < len(unpaired_players) - 1:
                p1 = unpaired_players[i]
                found = False
                for j in range(i + 1, len(unpaired_players)):
                    p2 = unpaired_players[j]
                    if (p2.ID not in p1.ID_played and
                            p1.ID not in p2.ID_played):
                        self.matches.append((p1, p2))
                        p1.ID_played.append(p2.ID)
                        p2.ID_played.append(p1.ID)
                        unpaired_players.pop(j)
                        unpaired_players.pop(i)
                        found = True
                        break
                if found is True:
                    p1 = i + 1
                else:
                    p2 = unpaired_players[i + 1]
                    self.matches.append((p1, p2))
                    p1.ID_played.append(p2.ID)
                    p2.ID_played.append(p1.ID)
                    i += 2

        return self.matches

    def result_round(self):
        """Mise à jour des points après le round."""
        print("\nListe des matchs :")
        print("")
        for i, match in enumerate(self.matches, start=1):
            p1, p2 = match
            print(f"{i}. {p1.first_name} vs {p2.first_name}")

        print(f"\n--- Résultats du Round {self.current_round + 1} ---")
        print("")
        for match in self.matches:
            player1, player2 = match
            print(f"{player1.first_name} {player1.last_name} vs "
                  f"{player2.first_name} {player2.last_name}")
            result = input(
                "Qui a gagné ? (1 = joueur 1, 2 = joueur 2 : "
            )

            if result == "1":
                player1.points += 1
                print(player1.first_name)
            elif result == "2":
                player2.points += 1
                print(player2.first_name)
            else:
                print("Entrée invalide. Aucun point attribué.")

    def to_result_dict(self):
        result_data = {}
        for i, (p1, p2) in enumerate(self.matches, start=1):
            if p1.points > p2.points:
                result = f"{p1.first_name} win - {p2.first_name} lose"
            else:
                p2.points > p1.points
                result = f"{p1.first_name} lose - {p2.first_name} win"

            result_data[f"match {i}"] = result

        return {f"round {self.current_round}": result_data}

    def to_dict(self):
        return {
            "current_round": self.current_round,
            "matches": [
                (p1.ID, p2.ID) for p1, p2 in self.matches
            ],
            "players": [
                (player.ID, player.ID_played) for player in self.players
            ]
        }
