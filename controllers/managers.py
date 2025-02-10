from abc import ABC
import json 
import os
from models.models import Player

class Manager(ABC):
    pass

class PlayerManager(Manager):

    #Les attributs       
    def __init__(self, filename="players_list.json", directory="data/tournaments"):
        """Création JSON"""
        
        self.directory = directory
        self.filename = os.path.join(self.directory, filename)
        self.players = [] # La liste n'est toujours pas créer ! a faire !
        
        # Vérifier si le dossier existe, sinon le créer
        os.makedirs(self.directory, exist_ok=True)
        
    def add_player(self, name, nickname, date_of_birth, point):
        # Charger ou créer la base de données JSON
        os.makedirs(self.directory, exist_ok=True)
        if os.path.exists(self.filename):
            with open(self.filename, self.directory, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:  # Fichier vide ou corrompu
                    data = {"joueurs": []}
        else:
            data = {"joueurs": []}

        # Instance (création d'objet)
        
        player = Player(name, nickname, date_of_birth, point)

        player_dict = {
            "name": player.name,
            "nickname": player.nickname,
            "date_of_birth": player.date_of_birth,
            "point": player.point
        }

        # Ajout d'un joueur
        data["joueurs"].append(player_dict)
        
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Joueur {player.nickname} a été ajouté dans la liste des participants")
        
        

class TournamentManager(Manager):
    pass