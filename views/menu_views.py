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
    pass