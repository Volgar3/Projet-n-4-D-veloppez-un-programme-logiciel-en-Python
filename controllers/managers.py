from abc import ABC
import json
import os
from models.models import Player, Tournement


class Manager(ABC):
    """Classe abstraite pour les gestionnaires."""
    pass


class PlayerManager(Manager):
    """Gestionnaire des joueurs."""

    def __init__(self, filename="players_list.json", directory="data/tournaments"):
        """Création du fichier JSON pour stocker les joueurs."""
        self.directory = directory
        self.filename = os.path.join(self.directory, filename)
        self.players = []

        # Vérifier si le dossier existe, sinon le créer
        os.makedirs(self.directory, exist_ok=True)

    def add_player(self, name, nickname, date_of_birth, point):
        """Ajoute un joueur au fichier players_list.json."""
        os.makedirs(self.directory, exist_ok=True)

        # Vérifier si le fichier existe et le charger
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)  # Chargement du fichier JSON
                except json.JSONDecodeError:  # Gestion du fichier vide ou corrompu
                    data = {"joueurs": []}
        else:
            data = {"joueurs": []}  # Création d'une structure vide si le fichier n'existe pas

        # Création d'une instance de Player (objet)
        player = Player(name, nickname, date_of_birth, point)

        # Transformation de l'objet en dictionnaire
        player_dict = {
            "name": player.name,
            "nickname": player.nickname,
            "date_of_birth": player.date_of_birth,
            "point": player.point,
        }

        # Ajout du joueur dans la liste JSON
        data["joueurs"].append(player_dict)

        # Enregistrement des données mises à jour
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Joueur {player.nickname} a été ajouté à la liste des participants.")

    def get_players(self):
        """Lit le fichier JSON et retourne la liste des joueurs."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)  # Chargement des données JSON

            # Vérification si la clé 'joueurs' existe dans le fichier JSON
            if "joueurs" in data:
                self.players = data["joueurs"]  # Mise à jour de l'attribut `players`
            else:
                print("Aucune clé 'joueurs' n'a été trouvée dans le fichier.")

        except FileNotFoundError:
            print("Le fichier de joueurs n'existe pas.")
            self.players = []  # On initialise une liste vide si le fichier est absent
        except json.JSONDecodeError:
            print("Le fichier de joueurs est corrompu ou mal formaté.")
            self.players = []  # On évite que le programme plante en cas de problème

        return self.players  # Retourne la liste des joueurs


class TournamentManager(Manager):
    """Gestionnaire des tournois (à implémenter)."""
    
    def __init__(self):
        self.tournaments = []
    
    def create_tournament(self, name, location, start_date, end_date, number_of_rounds, current_round, description):
        """Ajout d'un tournoi."""
        tournament = Tournement(name, location, start_date, end_date, number_of_rounds, current_round, description)
        self.tournaments.append(tournament)
        
        return tournament