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
        self.add_option(
            "2", "Paramétrer un tournoi", self.launch_tournament_menu
        )
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
        self.player_manager.add_player(
            data_player['first_name'],
            data_player['last_name'],
            data_player['date_of_birth'],
            0,  # points par défaut
            data_player['ID'],
            []  # ID_played vide
        )

    def player_list(self):
        """lance la méthode du listage des joueurs"""
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
        """Lance la méthode d'ajout de tournoi"""
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
            data_tournament['selected_players']
        )

    def tournament_list(self):
        """Lance la méthode du listage des tournois"""
        tournaments = self.tournament_manager.get_tournaments()
        TournamentMenuView.display_tournaments_list(tournaments)

    def start_tournament(self):
        """Permet la sélection du tournoi et le lance"""
        tournaments = self.tournament_manager.get_tournaments()
        if not tournaments:
            print("Aucun tournoi disponible.")
            return None

        TournamentMenuView.display_tournaments_list(tournaments)
        choice_name = input(
            "Entrez le nom du tournoi que vous souhaitez sélectionner : "
        ).strip()

        tournament = None
        for tournament_obj in tournaments:
            if tournament_obj.name.lower() == choice_name.lower():
                tournament = tournament_obj
                break

        if tournament is None:
            print("Tournoi non trouvé.")
            return None
        print(f"Le tournoi {tournament.name} commence !")

        players_data = tournament.selected_players
        if not players_data:
            print("Aucun joueur trouvé dans ce tournoi.")
            return None

        while tournament.current_round < tournament.number_of_rounds:
            players = [
                p if isinstance(p, Player) else Player.player_from_dict(p)
                for p in tournament.selected_players
            ]
            print(f"\n--- Round {tournament.current_round + 1} ---")
            round = Round(tournament.current_round, players=players)
            round.create_matches(tournament.rounds)
            round.result_round()
            tournament.selected_players = [
                p.player_to_dict() for p in players
            ]
            tournament.round_result.append(round.to_result_dict())
            tournament.rounds.append(round)

            updated_tournament = tournament.tournament_to_dict()
            self.tournament_manager.save_tournament(updated_tournament)

            print(
                f"Le round {tournament.current_round + 1}"
                "a été créé avec succès."
            )
            tournament.current_round += 1

        print(f"Le tournoi {tournament.name} est terminé !")
        return tournament

    def launch_main_menu(self):
        TournamentMenuView.display_return_message()
