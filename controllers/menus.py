from abc import ABC
from views.menu_views import MainMenuView
from views.menu_views import PlayerMenuView
from controllers.managers import PlayerManager

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
      
class MainMenu(Menu):
    def __init__(self, title):
        super().__init__(title)
        self.add_option("1", "Paramètre joueur", self.launch_player_menu)
        self.add_option("2", "Commencer un tournoi", self.start_tournament)
        self.add_option("3", "Option 3", self.option_3)
        self.add_option("q", "Quitter", self.quit)
        
        self.player_menu = PlayerMenu("Player Menu", self)

    def run(self):
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
    
    def start_tournament(self):
        print("Action pour l'option 2.")
    
    def option_3(self):
        print("Action pour l'option 3.")

    def launch_player_menu(self):
        self.player_menu.run()
    
    def quit(self):
        print("A bientôt !")
        exit()


class PlayerMenu(Menu):
    
    #Les attributs 
    def __init__(self,title, main_menu): 
        super().__init__(title)   
        self.add_option("1", "Ajouter un joueur",self.add_player) # rename l'option
        self.add_option("2", "Liste des joueurs", self.player_list) # rename l'option
        self.add_option("3", "Supprimer un joueur", self.delete_player) # rename l'option
        self.add_option("r","Retour au menu principal",self.launch_main_menu) # rename l'option
        self.main_menu = main_menu
        self.player_manager = PlayerManager()

    def run(self):
        """Boucle MenuPlayer."""
        while True:
            PlayerMenuView.display_options("Player Menu", self.options)
            choice = input("Entrez votre choix : ")

            if choice in self.options:
                description, function = self.options[choice]
                print(f"\nVous avez choisi : {description}\n")
                function()  # Exécute la fonction associée
            else:
                print("Choix invalide, veuillez réessayer.\n")
    
    #Les méthodes
    def add_player(self):
        
        data_player = PlayerMenuView.display_add_players()
             
        # Vérifier que le nombre de points est un entier
        try:
            data_player['point'] = int(data_player['point'])
        except ValueError:
            print("Erreur : Le nombre de points doit être un entier.")
            return  # Retour  au Playermenu
        
        # Ajouter le joueur
        self.player_manager.add_player(
            data_player['name'], 
            data_player['nickname'], 
            data_player['date_of_birth'], 
            data_player['point']
        )
    
    def player_list(self):
        pass
    
    def delete_player(self):
        pass
    
    def launch_main_menu(self):
        self.main_menu.run()