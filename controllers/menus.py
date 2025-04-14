from abc import ABC
from views.menu_views import MainMenuView, PlayerMenuView, TournamentMenuView
from controllers.managers import PlayerManager, TournamentManager
from models.models import Round, Player


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
        self.add_option("q", "Quitter", self.quit)

        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.player_menu = PlayerMenu("Player Menu", self.player_manager)
        self.tournament_menu = TournamentMenu(
            "Tournament Menu", self.tournament_manager, self.player_manager
        )

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

    def launch_player_menu(self):
        self.player_menu.run()

    def quit(self):
        print("À bientôt !")


class PlayerMenu(Menu):
    def __init__(self, title, player_manager):
        super().__init__(title)
        self.add_option("1", "Ajouter un joueur", self.add_player)
        self.add_option("2", "Liste des joueurs", self.player_list)
        self.add_option("r", "Retour au menu principal", self.launch_main_menu)
        self.player_manager = player_manager

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
            data_player['points'] = int(data_player['points'])
        except ValueError:
            print("Erreur : Le nombre de points doit être un entier.")
            return

        self.player_manager.add_player(
            data_player['first_name'],
            data_player['last_name'],
            data_player['date_of_birth'],
            data_player['points'],
            data_player['ID']
        )

    def player_list(self):
        PlayerMenuView.display_players_list(self.player_manager.get_players())

    def launch_main_menu(self):
        PlayerMenuView.display_return_message()


class TournamentMenu(Menu):
    def __init__(self, title, tournament_manager, player_manager):
        super().__init__(title)
        self.add_option("1", "Créer un tournoi", self.add_tournament)
        self.add_option("2", "Liste des tournois", self.tournament_list)
        self.add_option("3", "Commencer un tournoi", self.start_tournament)
        self.add_option("r", "Retour au menu principal", self.launch_main_menu)

        self.tournament_manager = tournament_manager
        self.player_manager = player_manager

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
            data_tournament['number_of_rounds'] = int(
                data_tournament['number_of_rounds']
            )
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
            data_tournament['description'],
            data_tournament['round_result'],
            data_tournament['selected_players'],
        )

    def tournament_list(self):
        tournaments = self.tournament_manager.get_tournaments()
        TournamentMenuView.display_tournaments_list(tournaments)

    def start_tournament(self):
        """Permet de choisir un tournoi et de lancer le premier round."""
        tournaments = self.tournament_manager.get_tournaments()
        if not tournaments:
            print("Aucun tournoi disponible.")
            return None

        TournamentMenuView.display_tournaments_list(tournaments)
        choice_name = input(
            "Entrez le nom du tournoi que vous souhaitez sélectionner : "
        ).strip()

        for tournament in tournaments:
            if tournament["name"].lower() == choice_name.lower():
                print(f"Le tournoi {tournament['name']} commence !")

                players_data = tournament.get("selected_players")
                if not players_data:
                    print("Aucun joueur trouvé dans ce tournoi.")
                    return None

                players = [
                    Player(**p) if isinstance(p, dict) else p
                    for p in players_data
                ]

                if "rounds" not in tournament:
                    tournament["rounds"] = []

                round_number = len(tournament["rounds"]) + 1
                round = Round(round_number, players)
                round.create_matches()
                round.result_round()

                tournament["selected_players"] = [
                    {
                        "first_name": p.first_name,
                        "last_name": p.last_name,
                        "date_of_birth": p.date_of_birth,
                        "points": p.points,
                        "ID": p.ID
                    }
                    for p in players
                ]

                tournament["rounds"].append(round)
                self.tournament_manager.save_tournament(tournament)

                print(f"Le round {round_number} a été créé avec succès.")
                return tournament

        print("Tournoi non trouvé.")
        return None

    def launch_main_menu(self):
        TournamentMenuView.display_return_message()