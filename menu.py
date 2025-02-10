class Menu: 
    
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


    def display(self): # Affichage du menu
        """Affiche le menu."""
        print(f"\n=== {self.title} ===")
        for number, (description, _) in self.options.items():
            print(f"{number}. {description}")
        print()

    def execute(self):
        """Boucle principale du menu."""
        while True:
            self.display()
            choice = input("Entrez votre choix : ")

            if choice in self.options:
                description, function = self.options[choice]
                print(f"\nVous avez choisi : {description}\n")
                function()  # Exécute la fonction associée
            else:
                print("Choix invalide, veuillez réessayer.\n") 

# === Exemple d'utilisation === Ici je vais pouvoir appeller les class aux besoin, donc player, Tournement, Round

def player():
    """Affichage menu Player"""
    
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
            
            
def option_2():
    print("Action pour l'option 2.")
    
def option_3():
    print("Action pour l'option 3.")
    
def quit():
    print("A bientôt !")
    exit()
    
# Création du menu

menu_principal = Menu("Menu principal")
menu_principal.add_option("1", "Paramètre joueur", player)
menu_principal.add_option("2", "Commencer un tournoi", option_2)
menu_principal.add_option("3", "Option 3", option_3)
menu_principal.add_option("q", "Quitter", quit)

# Lancement du menu principal

menu_principal.execute()

class Player:

        def __init__(self):
            
            self.player_list = []
            
        def info_player(self, name, nickname, date_of_birth, point):  # class Player 
        
            self.name = name
            self.nickname = nickname
            self.date_of_birth = date_of_birth
            self.point = point
            
            return
        
        def add_player(self): # class Player
        
            self.player_list = [] # A réfléchir si ce n'est pas un attribut de la class Player
            
            return
        
class Tournement:
    pass

class Round:
    pass