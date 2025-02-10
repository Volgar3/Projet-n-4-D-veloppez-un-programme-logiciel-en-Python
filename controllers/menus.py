from abc import ABC
from views.menu_views import MainMenuView

class Menu(ABC):
    def __init__ (self, title):
        """Initialise le menu avec un titre et une liste d'options."""
        self.title = title
        self.options = {} # Contient la liste des fonction ajouter avec "add_option"

    def add_option(self, number, description, function): #ajout de fonction dans le menu
        """
        Ajoute une option au menu.
        - number : numéro de l'option.
        - description : texte affiché dans le menu.
        - function : fonction associée à l'option.
        """
        self.options[number] = (description, function)


class PlayerMenu(Menu):
    def run(self):
        while True:
            print("\n=== Menu Joueurs ===")
            print("1. Ajouter un joueur")
            print("2. Liste des joueurs")
            print("r. Retour au menu principal")

            choix = input("Entrez votre choix : ")

            if choix == "1":
                 """Ajouter l'option du choix""" # A modifier
             
            elif choix == "2":
                """Ajouter l'option du choix""" # A modifier
            
            elif choix == "r":
                print("Retour au menu principal.")
                break  # Retourne au menu principal
            else:
                print("Choix invalide, veuillez réessayer.")

class MainMenu(Menu):
    def __init__(self, title):
        super().__init__(title)
        self.add_option("1", "Paramètre joueur", self.launch_player_menu)
        self.add_option("2", "Commencer un tournoi", self.option_2)
        self.add_option("3", "Option 3", self.option_3)
        self.add_option("q", "Quitter", self.quit)
        
        self.player_menu = PlayerMenu("Player Menu")

    def execute(self):
        """Boucle principale du menu."""
        while True:
            MainMenuView.display_options("Main Menu", self.options)
            choice = input("Entrez votre choix : ")

            if choice in self.options:
                description, function = self.options[choice]
                print(f"\nVous avez choisi : {description}\n")
                function()  # Exécute la fonction associée
            else:
                print("Choix invalide, veuillez réessayer.\n")
    
    def option_2(self):
        print("Action pour l'option 2.")
    
    def option_3(self):
        print("Action pour l'option 3.")

    def launch_player_menu(self):
        self.player_menu.run()
    
    def quit(self):
        print("A bientôt !")
        exit()
