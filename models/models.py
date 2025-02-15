class Player:
    
    #Les attributs
    def __init__(self, name, nickname, date_of_birth, point):
        self.name = name
        self.nickname = nickname
        self.date_of_birth = date_of_birth
        self.point = point
        
    #Les méthodes 
    

class Tournement:
    
    def __init__(self, name, location, start_date, end_date, number_of_rounds, current_round, description):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds # Valeur par défaut : 4 / a faire
        self.current_round = current_round
        self.rounds = []
        self.players = []
        self.description = description

class Round:
    pass