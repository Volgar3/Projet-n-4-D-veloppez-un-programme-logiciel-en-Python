from abc import ABC
from controllers.managers import PlayerManager, TournamentManager
from controllers.managers import TournamentManager
from models.models import Round

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
        first_name = input("Prénom du joueur : ")
        last_name = input("Nom du joueur : ")
        date_of_birth = input("Date de naissance (DD-MM-YYYY) : ")
        points = input("Nombre de points : ")
        ID = input("ID du joueur : ")

        data_player = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "points": points,
            "ID": ID,
        }

        return data_player

    @staticmethod
    def display_players_list(players):
        """Affichage de la liste des joueurs."""
        print("\n=== Liste des joueurs ===")
        
        for player in players:
            print(
                f"Prénom: {player['first_name']}, Nom: {player['last_name']}, Date de naissance: {player['date_of_birth']} "
                f"Points: {player['points']},ID : {player['ID']}"
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
        
        #Sélection des joueurs
        player_manager = PlayerManager()
        selected_players = player_manager.selected_players()

        data_tournament = {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rounds": number_of_rounds,
            "current_round": current_round,
            "description": description,
            "selected_players": selected_players,
            "round_result": []
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
    def display_matches(matches):
        """Affichage des matchs."""
        print("\n=== Liste des matchs ===")
        for match in matches:
            print(f"Match : {match[0]} contre {match[1]}")
            
            
    @staticmethod
    def display_players_for_tournament(players):
        """Affichage des joueurs pour un tournoi."""
        print("\n=== choisissez les joueurs participants au tournoi ===")
        # TODO: A déplacer dans le controller.
        for player in players:
            print(
                f"Prénom: {player['first_name']}, ID : {player['ID']}"
            )
            
        selected_players = []
        print("\nEntrez les ID des joueurs que vous souhaitez sélectionner (séparés par des virgules) :")
        ids = input("IDs des joueurs : ").split(",")

        for player_id in ids:
            player_id = player_id.strip()  # Supprimer les espaces autour de l'ID
            for player in players:
                if player['ID'] == player_id:
                    selected_players.append(player)
                    break
            else:
                print(f"ID {player_id} non trouvé dans la liste des joueurs.")

        print("\n=== Joueurs sélectionnés ===")
        for player in selected_players:
            print(
                f"Prénom: {player['first_name']}, ID : {player['ID']}"
            )

        return selected_players
            
class ViewMenuRound(MenuView):
    def display_matches(matches):
        """Affichage des matchs."""
        print("\n=== Liste des matchs ===")
        for P1, P2 in matches:
            print(f"Match : {P1[0]} contre {P2[1]}")