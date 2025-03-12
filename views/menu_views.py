from abc import ABC
from controllers.managers import PlayerManager, TournamentManager


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
        matricules = input("Matricules ID : ")

        data_player = {
            "name": name,
            "nickname": nickname,
            "date_of_birth": date_of_birth,
            "point": point,
            "Matricules ID": matricules,
        }

        return data_player

    @staticmethod
    def display_players_list(players):
        """Affichage de la liste des joueurs."""
        print("\n=== Liste des joueurs ===")
        
        for player in players:
            print(
                f"Nom: {player['name']}, Surnom: {player['nickname']}, Date de naissance: {player['date_of_birth']} "
                f"Points: {player['point']}, Matricules ID: {player['matricules']}"
            )

    @staticmethod
    def display_return_message():
        print("-> Retour au menu principal")
        
class TournamentMenuView(MenuView):
    @staticmethod
    def display_add_tournament():
        """Affichage des informations du tournoi à rentrer."""
        print("\n=== Information du tournoi à rentrer ===")
        name = input("Nom du tournoi : ")
        location = input("Lieu du tournoi : ")
        start_date = input("Date de début (DD-MM-YYYY) : ")
        end_date = input("Date de fin (DD-MM-YYYY) : ")
        number_of_rounds = input("Nombre de rounds : ")
        current_round = input("Round actuel : ")
        description = input("Description : ")

        data_tournament = {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rounds": number_of_rounds,
            "current_round": current_round,
            "description": description,
        }
        return data_tournament

    @staticmethod
    def display_tournaments_list(tournaments):
        """Affichage de la liste des tournois."""
        print("\n=== Liste des tournois ===")
        for tournament in tournaments:
            print(
                f"Nom: {tournament['name']}, Lieu: {tournament['location']}, "
                f"Date de début: {tournament['start_date']}, Date de fin: {tournament['end_date']}, "
                f"Nombre de rounds: {tournament['number_of_rounds']}, Round actuel: {tournament['current_round']}, "
                f"Description: {tournament['description']}"
            )
            
    @staticmethod
    def display_matches(matches): # A FAIRE OMG J'AI TOUT COMPRIS
        """Affichage des matchs."""
        print("\n=== Liste des matchs ===")
        for match in matches:
            print(f"Match : {match[0]} contre {match[1]}")