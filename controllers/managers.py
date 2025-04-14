from abc import ABC
import json
import os
import random
from models.models import Player, Tournament


class Manager(ABC):
    """Classe abstraite pour les gestionnaires."""
    pass


class PlayerManager(Manager):
    """Gestionnaire des joueurs."""

    def __init__(self, filename_players="players_list.json", directory_players="data/players"):
        """Création du fichier JSON pour stocker les joueurs."""
        self.directory_players = directory_players
        self.filename_players = os.path.join(self.directory_players, filename_players)
        self.players = []

        # Vérifier si le dossier existe, sinon le créer
        os.makedirs(self.directory_players, exist_ok=True)

    def add_player(self, first_name, last_name, date_of_birth, points, ID ):
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
        player = Player(first_name, last_name, date_of_birth, points, ID)

        # Transformation de l'objet en dictionnaire
        player_dict = {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "date_of_birth": player.date_of_birth,
            "points": player.points,
            "ID": player.ID
        }

        # Ajout du joueur dans la liste JSON
        data["joueurs"].append(player_dict)

        # Enregistrement des données mises à jour
        with open(self.filename_players, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Joueur {player.last_name} a été ajouté à la liste des participants.")

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
        
    def selected_players(self):
        """Permet de sélectionner les joueurs pour un tournoi."""
        print("\n=== Liste des joueurs disponibles ===")
        # Chargement de la liste des joueurs
        self.get_players()
        for index, player in enumerate(self.players):
            print(f"{index + 1}. {player['first_name']} {player['last_name']} (ID: {player['ID']}, Points: {player['points']})")

        selected_players = []
        print("\nEntrez les ID des joueurs que vous souhaitez sélectionner (séparés par des virgules) :")
        choices = input("ID des joueurs : ").split(",")

        for choice in choices:
            try:
                index = int(choice.strip()) - 1  # On ajuste pour l'index réel
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
    
class TournamentManager(Manager):
    """Gestionnaire des tournois."""
    
    def __init__(self, filename_tournament= "tournament_list.json", directory_tournaments="data/tournaments"):
        """Création du fichier JSON pour stocker les tournois."""
        self.directory_tournaments = directory_tournaments
        self.filename_tournament = filename_tournament
        self.filename_tournament = os.path.join(directory_tournaments, filename_tournament)
        self.tournaments = []
        self.selected_players_list = []
        #Vérifier si le dossier existe, sinon le créer
        os.makedirs(directory_tournaments, exist_ok=True)   
        print(f"Répertoire des tournois : {self.directory_tournaments}")      
           
    def add_tournament(self, name, location, start_date, end_date, number_of_rounds, current_round, description, round_result, players):
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
        tournament = Tournament(
            name = name,
            location = location,
            start_date = start_date,
            end_date = end_date,
            number_of_rounds = number_of_rounds,
            current_round = current_round,
            round_result = round_result,
            description = description,
            selected_players = players
        )
        
        tournament_dict = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "number_of_rounds": tournament.number_of_rounds,
            "current_round": tournament.current_round,
            "round_result": tournament.round_result,
            "description": tournament.description,
            "selected_players": tournament.selected_players
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

    def save_tournament(self, updated_tournament):
        """Met à jour un tournoi existant dans le fichier JSON."""
        # Charger le fichier existant
        try:
            with open(self.filename_tournament, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"tournaments": []}

        # Remplacer le tournoi qui a le même nom
        for i, t in enumerate(data["tournaments"]):
            if t["name"] == updated_tournament["name"]:
                data["tournaments"][i] = updated_tournament
                break
        else:
            # Si non trouvé, l'ajouter (sécurité)
            data["tournaments"].append(updated_tournament)

        # Réécrire dans le fichier JSON
        with open(self.filename_tournament, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Tournoi \"{updated_tournament['name']}\" sauvegardé avec succès.")
    