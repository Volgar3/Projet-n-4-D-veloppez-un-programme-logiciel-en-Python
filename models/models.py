class Player:
    
    #Les attributs
    def __init__(self, name, nickname, date_of_birth, point):
        self.name = name
        self.nickname = nickname
        self.date_of_birth = date_of_birth
        self.point = point
        
    #Les méthodes 
    

class Tournement:
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.location = kwargs.get('location')
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')
        self.number_of_rounds = kwargs.get('number_of_rounds', 4)
        self.current_round = kwargs.get('current_round', 1)
        self.description = kwargs.get('description')
        self.rounds = [] # Objets Round
        self.players = [] # Objets Round
    
    def next_round(self):
        pass

class Round:
    pass