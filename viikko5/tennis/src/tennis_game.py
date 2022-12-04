from entities.player import Player
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.terms = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
            }

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1.add_point()
        else:
            self.player2.add_point()
    
    def scores_are_even(self, score):        
        if score > 3:
            return "Deuce"
 
        return f"{self.terms[score]}-All"

    def someone_has_over_four_points(self):
        score_difference = self.player1.score - self.player2.score
        
        if score_difference > 0:
            if score_difference == 1:
                return "Advantage player1"
            else:
                return "Win for player1"
        if score_difference < 0:
            if score_difference == -1:
                return "Advantage player2"
            else:
                return "Win for player2"
        
    def both_have_under_four_points(self):
        return f"{self.terms[self.player1.score]}-{self.terms[self.player2.score]}"

    def get_score(self):
        
        if self.player1.score == self.player2.score:
            return self.scores_are_even(self.player1.score)

        elif self.player1.score >= 4 or self.player2.score >= 4:
            return self.someone_has_over_four_points()
            
        return self.both_have_under_four_points()
