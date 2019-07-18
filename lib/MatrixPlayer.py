class MatrixPlayer:
    def __init__(self, position_symbol, number, link=''):
        self.position_symbol = position_symbol
        self.number = number
        self.link = link
        self.team = None
        self.sport = None

    def add_team(self, team):
        self.team = team
        self.sport = team.sport

    def __str__(self):
        return "[ MATRIX PLAYER {} on <{}> ]".format(self.position_symbol, str(self.team))

    @property
    def position(self):
        if self.team:
            if len(self.team.sport.positions) > 0:
                return self.team.sport.positions.get(self.position_symbol, "")
            return ""
