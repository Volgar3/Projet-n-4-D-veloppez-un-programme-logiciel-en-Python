from abc import ABC
from views.menu_views import MainMenuView, PlayerMenuView, TournamentMenuView
from controllers.managers import PlayerManager, TournamentManager


class Menu(ABC):
    def __init__(self, title):
        """Initialise le menu avec un titre et une liste d'options."""
        self.title = title
        self.options = {}

    def add_option(self, number, description, function):
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
        self.add_option("2", "Paramétrer un tournoi", self.launch_tournament_menu)
        self.add_option("3", "Option 3", self.option_3)
        self.add_option("q", "Quitter", self.quit)

        self.player_menu = PlayerMenu("Player Menu", self)
        self.tournament_menu = TournamentMenu("Tournament Menu", self)
        
    def run(self):
        """Boucle principale du menu."""
        choice = None
        while choice != "q":
            MainMenuView.display_options("Main Menu", self.options)
            choice = input("Entrez votre choix : ")

            if choice in self.options:
                description, function = self.options[choice]
                print(f"\nVous avez choisi : {description}\n")
                function()
            else:
                print("Choix invalide, veuillez réessayer.\n")

    def launch_tournament_menu(self):
        self.tournament_menu.run()

    def option_3(self):
        print("Action pour l'option 3.")

    def launch_player_menu(self):
        self.player_menu.run()

    def quit(self):
        print("A bientôt !")


class PlayerMenu(Menu):
    def __init__(self, title, main_menu):
        super().__init__(title)
        self.add_option("1", "Ajouter un joueur", self.add_player)
        self.add_option("2", "Liste des joueurs", self.player_list)
        self.add_option("3", "Supprimer un joueur", self.delete_player)
        self.add_option("r", "Retour au menu principal", self.launch_main_menu)
        self.main_menu = main_menu
        self.player_manager = PlayerManager()

    def run(self):
        """Boucle du menu joueur."""
        choice = None
        while choice != "r":
            PlayerMenuView.display_options("Player Menu", self.options)
            choice = input("Entrez votre choix : ")

            if choice in self.options:
                description, function = self.options[choice]
                print(f"\nVous avez choisi : {description}\n")
                function()
            else:
                print("Choix invalide, veuillez réessayer.\n")

    def add_player(self):
        data_player = PlayerMenuView.display_add_players()
        try:
            data_player['point'] = int(data_player['point'])
        except ValueError:
            print("Erreur : Le nombre de points doit être un entier.")
            return

        self.player_manager.add_player(
            data_player['name'],
            data_player['nickname'],
            data_player['date_of_birth'],
            data_player['point']
        )

    def player_list(self):
        PlayerMenuView.display_players_list(self.player_manager.get_players())

    def delete_player(self):
        pass

    def launch_main_menu(self):
        PlayerMenuView.display_return_message()
        
        
class TournamentMenu(Menu): 
    
    def __init__(self, title, main_menu):
        super().__init__(title)
        self.add_option("1", "Créer un tournoi", self.add_tournament)
        self.add_option("2", "Liste des tournois", self.tournament_list)
        self.add_option("3", "Option 3", self.start_tournament)
        self.add_option("r", "Retour au menu principal", self.launch_main_menu)
        self.main_menu = main_menu
        self.tournament_manager = TournamentManager()
        
    def run(self):
        """Boucle du menu tournoi."""
        choice = None
        while choice != "r":
            TournamentMenuView.display_options("Tournament Menu", self.options)
            choice = input("Entrez votre choix : ")

            if choice in self.options:
                description, function = self.options[choice]
                print(f"\nVous avez choisi : {description}\n")
                function()
            else:
                print("Choix invalide, veuillez réessayer.\n")
                
    def add_tournament(self):
        data_tournament = TournamentMenuView.display_add_tournament()
        try:
            data_tournament['number_of_rounds'] = int(data_tournament['number_of_rounds'])
        except ValueError:
            print("Erreur : Le nombre de rounds doit être un entier.")
            return
        
        self.tournament_manager.add_tournament(
            data_tournament['name'],
            data_tournament['location'],
            data_tournament['start_date'],
            data_tournament['end_date'],
            data_tournament['number_of_rounds'],
            data_tournament['current_round'],
            data_tournament['description']
        )
        
    def tournament_list(self):
        TournamentMenuView.display_tournaments_list(self.tournament_manager.get_tournaments())
        
    def start_tournament(self):
        """Lancement d'un tournoi."""  # Permet de choisir un tournoie déjà créé ou de le créer
        pass
    
    def launch_main_menu(self):
        TournamentMenuView.display_return_message()