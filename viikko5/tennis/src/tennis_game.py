class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1

    def is_tie(self):
        return self.m_score1 == self.m_score2

    def get_score_name(self, score):
        score_names = {self.LOVE: "Love", self.FIFTEEN: "Fifteen",
                       self.THIRTY: "Thirty", self.FORTY: "Forty"}
        return score_names.get(score, "")

    def get_score(self):
        if self.is_tie():
            return self.get_tie_score()
        if self.is_endgame():
            return self.get_endgame_score()
        return self.get_regular_score()

    def get_tie_score(self):
        tie_scores = {
            self.LOVE: "Love-All",
            self.FIFTEEN: "Fifteen-All",
            self.THIRTY: "Thirty-All"
        }
        return tie_scores.get(self.m_score1, "Deuce")

    def is_endgame(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4

    def get_endgame_score(self):
        score_difference = self.m_score1 - self.m_score2
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        if score_difference == -1:
            return f"Advantage {self.player2_name}"
        if score_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def get_regular_score(self):
        return f"{self.get_score_name(self.m_score1)}-{self.get_score_name(self.m_score2)}"
