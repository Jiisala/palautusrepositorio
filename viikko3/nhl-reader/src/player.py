
class Player:
    def __init__(self, name, assists, goals, team, nationality):
        self.name = name
        self.assists = assists
        self.goals = goals
        self.team = team
        self.nationality = nationality
    
    def __str__(self):
        return f"{self.name:20} {self.team:2} {self.goals:2} + {self.assists:2} = {self.goals +self.assists}"
