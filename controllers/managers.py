from abc import ABC
import json
import os
from models.models import Player, Tournement


class Manager(ABC):
    """Classe abstraite pour les gestionnaires."""
    pass


class PlayerManager(Manager):
    """Gestionnaire des joueurs."""

    def __init__(self, filename_players="players_list.json", directory_players="data/tournaments"):
        """Création du fichier JSON pour stocker les joueurs."""
        self.directory_players = directory_players
        self.filename_players = os.path.join(self.directory_players, filename_players)
        self.players = []

        # Vérifier si le dossier existe, sinon le créer
        os.makedirs(self.directory_players, exist_ok=True)

    def add_player(self, name, nickname, date_of_birth, point):
        """Ajoute un joueur au fichier players_list.json."""
        os.makedirs(self.directory_players, exist_ok=True)

        # Vérifier si le fichier existe et le charger
        if os.path.exists(self.filename_players):
            with open(self.filename_players, "r", encoding="utf-8") as file:
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
        with open(self.filename_players, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Joueur {player.nickname} a été ajouté à la liste des participants.")

    def get_players(self):
        """Lit le fichier JSON et retourne la liste des joueurs."""
        try:
            with open(self.filename_players, "r", encoding="utf-8") as file:
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
    """Gestionnaire des tournois."""
    
    def __init__(self,filename_tournament= "tournament_list.json", directory_tournaments="data/tournaments" ):
        """Création du fichier JSON pour stocker les tournois."""
        self.directory_tournaments = directory_tournaments
        self.filename_tournament = filename_tournament
        filename_tournament = os.path.join(directory_tournaments, filename_tournament)
        self.tournaments = []
        
        #Vérifier si le dossier existe, sinon le créer
        os.makedirs(directory_tournaments, exist_ok=True)
        
        
    def add_tournament(self, name, location, start_date, end_date, number_of_rounds, current_round, description):
        """Création d'un tournoi."""
        os.makedirs(self.directory_tournaments, exist_ok=True)
        
        #Vérifier si le fichier existe et le charger
        if os.path.exists(self.filename_tournament):
            with open(self.filename_tournament, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file) # Chargement du fichier JSON
                except json.JSONDecodeError: # Gestion du fichier vide ou corrompu
                    data = {"tournaments": []}
        else:
            data = {"tournaments": []}
            
        #Création d'une instance de Tournament
        tournament = Tournement(name, location, start_date, end_date, number_of_rounds, current_round, description)
        
        tournament_dict = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "number_of_rounds": tournament.number_of_rounds,
            "current_round": tournament.current_round,
            "description": tournament.description,
        }
        data["tournaments"].append(tournament_dict)
        
        #Enregistrement des données mises à jour
        with open(self.filename_tournament, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        
        print(f"Le tournoi {tournament.name} a été créé.")
        
    def get_tournaments(self):
        """Lit le fichier JSON et retourne la liste des tournois."""
        try:
            with open(self.filename_tournament, 'r', encoding="utf-8") as file:
                data = json.load(file)
            if "tournaments" in data:
                self.tournaments = data["tournaments"]
            else:
                print("Aucune clé 'tournaments' n'a été trouvée dans le fichier.")
        except FileNotFoundError:
            print("Le fichier de tournois n'existe pas.")
            self.tournaments = []
        except json.JSONDecodeError:
            print("Le fichier de tournois est corrompu ou mal formaté.")
            self.tournaments = []

        return self.tournaments # Retourne la liste des tournois
    
    def get_player_from_list(self): # A utiliser dans create_tournament
        """Sélectionne les joueurs de la liste."""
        pass