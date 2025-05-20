import json
import os
from models.models import Player, Tournament


class PlayerManager:
    """Gestionnaire des joueurs."""

    def __init__(self, filename_players="players_list.json",
                 directory_players="data/players"):
        """Création du fichier JSON pour stocker les joueurs."""
        self.directory_players = directory_players
        self.filename_players = os.path.join(
            self.directory_players,
            filename_players
        )
        self.players = []
        os.makedirs(self.directory_players, exist_ok=True)

    def add_player(self, first_name, last_name, date_of_birth,
                   points, ID, ID_played):
        """Ajoute un joueur au fichier players_list.json."""
        os.makedirs(self.directory_players, exist_ok=True)

        if os.path.exists(self.filename_players):
            with open(self.filename_players, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {"joueurs": []}
        else:
            data = {"joueurs": []}

        player = Player(first_name, last_name, date_of_birth, points, ID)
        player_dict = player.player_to_dict()
        data["joueurs"].append(player_dict)

        with open(self.filename_players, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(
            f"Joueur {player.last_name} a été ajouté à la liste des "
            "participants."
        )

    def get_players(self):
        """Lit le fichier JSON et retourne la liste des joueurs."""
        try:
            with open(self.filename_players, "r", encoding="utf-8") as file:
                data = json.load(file)

            players_to_convert = []
            if "joueurs" in data:
                for player_dict in data["joueurs"]:
                    player = Player.player_from_dict(player_dict)
                    players_to_convert.append(player)
                players_to_convert.sort(
                    key=lambda player: player.first_name
                )
                self.players = players_to_convert
            else:
                print("Aucune clé 'joueurs' trouvée dans le fichier.")
        except FileNotFoundError:
            print("Le fichier de joueurs n'existe pas.")
            self.players = []
        except json.JSONDecodeError:
            print("Le fichier de joueurs est corrompu ou mal formaté.")
            self.players = []

        return self.players

    def selected_players(self):
        """Permet de sélectionner les joueurs pour un tournoi."""
        print("\n=== Liste des joueurs disponibles ===")
        self.get_players()

        player_to_dict = []
        for player in self.players:
            player = player.player_to_dict()
            player_to_dict.append(player)
        self.players = player_to_dict

        for index, player in enumerate(self.players):
            print(f"{index + 1}. {player['first_name']} {player['last_name']} "
                  f"(ID: {player['ID']}, Points: {player['points']})")

        selected_players = []
        print(
            "\nEntrez les numéros des joueurs à sélectionner "
            "(séparés par des virgules) :"
        )
        choices = input("ID des joueurs : ").split(",")

        for choice in choices:
            try:
                index = int(choice.strip()) - 1
                if 0 <= index < len(self.players):
                    selected_players.append(self.players[index])
                else:
                    print(f"Numéro {choice} invalide (hors liste).")
            except ValueError:
                print(f"Entrée invalide : {choice} n’est pas un nombre.")

        print("\n=== Joueurs sélectionnés ===")
        for player in selected_players:
            print(f"{player['first_name']} {player['last_name']}")

        return selected_players


class TournamentManager:
    """Gestionnaire des tournois."""

    def __init__(self, filename_tournament="tournament_list.json",
                 directory_tournaments="data/tournaments"):
        """Création du fichier JSON pour stocker les tournois."""
        self.directory_tournaments = directory_tournaments
        self.filename_tournament = os.path.join(
            directory_tournaments,
            filename_tournament
        )
        self.tournaments = []
        self.selected_players_list = []
        os.makedirs(directory_tournaments, exist_ok=True)
        print(
            f"Répertoire des tournois : {self.directory_tournaments}"
        )

    def add_tournament(self, name, location, start_date, end_date,
                       number_of_rounds, current_round, description,
                       round_result, players):
        """Création d'un tournoi."""
        os.makedirs(self.directory_tournaments, exist_ok=True)

        if os.path.exists(self.filename_tournament):
            with open(self.filename_tournament, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {"tournaments": []}
        else:
            data = {"tournaments": []}

        number_of_rounds = int(number_of_rounds)
        current_round = int(current_round)

        tournament = Tournament(
            name=name,
            location=location,
            start_date=start_date,
            end_date=end_date,
            number_of_rounds=number_of_rounds,
            current_round=current_round,
            round_result=round_result,
            description=description,
            selected_players=players
        )

        tournament_dict = tournament.tournament_to_dict()
        data["tournaments"].append(tournament_dict)

        with open(self.filename_tournament, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Le tournoi {tournament.name} a été créé.")

    def get_tournaments(self):
        """Lit le fichier JSON et retourne la liste des tournois."""
        try:
            with open(self.filename_tournament, 'r', encoding="utf-8") as file:
                data = json.load(file)

            if "tournaments" in data:
                self.tournaments = [
                    Tournament.tournament_from_dict(t)
                    for t in data["tournaments"]
                ]
            else:
                print("Aucune clé 'tournaments' trouvée dans le fichier.")
        except FileNotFoundError:
            print("Le fichier de tournois n'existe pas.")
            self.tournaments = []
        except json.JSONDecodeError:
            print("Le fichier de tournois est corrompu ou mal formaté.")
            self.tournaments = []

        return self.tournaments

    def save_tournament(self, updated_tournament):
        """Met à jour un tournoi existant dans le fichier JSON."""
        try:
            with open(self.filename_tournament, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"tournaments": []}

        for i, t in enumerate(data["tournaments"]):
            updated_tournament["rounds"] = [
                round.to_dict() for round in updated_tournament["rounds"]
            ]
            if t["name"] == updated_tournament["name"]:
                data["tournaments"][i] = updated_tournament
                break
            else:
                data["tournaments"].append(updated_tournament)

        with open(self.filename_tournament, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(
            f'Tournoi "{updated_tournament["name"]}" sauvegardé avec succès.'
        )
