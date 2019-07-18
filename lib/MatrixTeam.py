from lib.MatrixItem import MatrixItem
from lib.MatrixSport import MatrixSport
from lib.MatrixPlayer import MatrixPlayer


class MatrixTeam(MatrixItem):
    def __init__(self, matrix_instance, sport, team_name, town, logo, link='', varsity=False):
        if type(sport) is MatrixSport:
            super().__init__('thing', 'team.' + str(town + " " + team_name).lower().replace(" ", "_"), [], matrix_instance, 'team')
            self.sport = sport
            self.team_name = team_name
            self.name = town + " " + self.team_name
            self.town = town
            self.logo = logo
            self.link = link
            self.varsity = varsity
            self.players = []
        else:
            raise Exception(str(sport) + " must be a Matrix Sport object")

    def __str__(self):
        return "[ MATRIX TEAM <{}>: {}, {} players ]".format(self.name, self.sport, str(len(self.players)))

    def add_player(self, player):
        if type(player) is MatrixPlayer:
            player.add_team(self)
            self.players.append(player)

