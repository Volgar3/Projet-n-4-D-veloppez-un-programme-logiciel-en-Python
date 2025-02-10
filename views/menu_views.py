from abc import ABC

class MenuView(ABC):
    @staticmethod
    def display_options(title, options): # Affichage du menu
        """Affiche le menu."""
        print(f"\n=== {title} ===")
        for number, (description, _) in options.items():
            print(f"{number}. {description}")
        print()

class MainMenuView(MenuView):
    pass

class PlayerMenuView(MenuView):
    
    def display_add_players():
        # Demander les infos au joueur
        print(f"\n===Information du joueur à rentrer===")
        name = input("Nom du joueur : ")
        nickname = input("Surnom du joueur : ")
        date_of_birth = input("Date de naissance (YYYY-MM-DD) : ")
        point = input("Nombre de points : ")
        
        # Créer un dictionnaire avec les données
        data_player = {
            'name': name,
            'nickname': nickname,
            'date_of_birth': date_of_birth,
            'point': point
        }

        return data_player