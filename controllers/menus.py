from abc import ABC
from views.menu_views import MainMenuView, PlayerMenuView
from controllers.managers import PlayerManager


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
                function()
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
        while True:
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
        player_menu_view = PlayerMenuView()
        player_menu_view.display_players_list()

    def delete_player(self):
        pass

    def launch_main_menu(self):
        self.main_menu.run()
