from abc import ABC
from controllers.managers import PlayerManager


class MenuView(ABC):
    @staticmethod
    def display_options(title, options):
        """Affiche le menu."""
        print(f"\n=== {title} ===")
        for number, (description, _) in options.items():
            print(f"{number}. {description}")
        print()


class MainMenuView(MenuView):
    pass


class PlayerMenuView(MenuView):

    @staticmethod
    def display_add_players():
        """Demande les informations du joueur et les retourne sous forme de dictionnaire."""
        print("\n=== Information du joueur à rentrer ===")
        name = input("Nom du joueur : ")
        nickname = input("Surnom du joueur : ")
        date_of_birth = input("Date de naissance (DD-MM-YYYY) : ")
        point = input("Nombre de points : ")

        data_player = {
            "name": name,
            "nickname": nickname,
            "date_of_birth": date_of_birth,
            "point": point,
        }

        return data_player

    def display_players_list(self):
        """Affichage de la liste des joueurs."""
        print("\n=== Liste des joueurs ===")
        
        player_manager = PlayerManager()  # Instance de PlayerManager
        players = player_manager.players_list()  # Récupération de la liste des joueurs
        
        for player in players:
            print(
                f"Nom: {player['name']}, Surnom: {player['nickname']}, "
                f"Date de naissance: {player['date_of_birth']}, Points: {player['point']}"
            )
