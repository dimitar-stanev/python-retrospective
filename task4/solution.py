class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard():

    VALID_INDECES = [ "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    def restartGame(self):
        matrix = [[" "]*3 for i in range(3)]
    def __str__(self):
        return "  -------------\n"
        +"3 | "+ self.matrix[0][0] + " | " + self.matrix[0][1] + " | " + self.matrix[0][2] + " |\n"
        +"  -------------\n"
        +"2 | "+ self.matrix[1][0] + " | " + self.matrix[1][1] + " | " + self.matrix[1][2] + " |\n"
        +"  -------------\n"
        +"1 | "+ self.matrix[2][0] + " | " + self.matrix[2][1] + " | " + self.matrix[2][2] + " |\n"
        +"  -------------\n"
        +"    A   B   C  "
    def __setitem__(self, index, value):

        if index not in self.VALID_INDECES:
            raise InvalidKey

        if value is not "X" or value is not "O":
            raise InvalidValue

        if self.matrix[index] is not " ":
            raise InvalidMove

        if self.last_move == value:
            raise NotYourTurn

        if index[0]=="A" and index[1]=="1":
            self.matrix[2][0] = value
            self.last_move = value
        elif index[0]=="A" and index[1]=="2":
            self.matrix[1][0] = value
            self.last_move = value
        elif index[0]=="A" and index[1]=="3":
            self.matrix[0][0] = value
            self.last_move = value
        elif index[0]=="B" and index[1]=="1":
            self.matrix[2][1] = value
            self.last_move = value
        elif index[0]=="B" and index[1]=="2":
            self.matrix[1][1] = value
            self.last_move = value
        elif index[0]=="B" and index[1]=="3":
            self.matrix[0][1] = value
            self.last_move = value
        elif index[0]=="C" and index[1]=="1":
            self.matrix[2][2] = value
            self.last_move = value
        elif index[0]=="C" and index[1]=="2":
            self.matrix[1][2] = value
            self.last_move = value
        elif index[0]=="C" and index[1]=="3":
            self.matrix[0][2] = value
            self.last_move = value

    def __init__(self):
        matrix = [[" "]*3 for i in range(3)]
        self.last_move = None

    def game_status(self):
            winner = False
            for i in range(3):
                    if self.matrix[i][0] == self.matrix[i][1] and self.matrix[i][0] == self.matrix[i][2]:
                            winner = True
                            return (self.matrix[0][i] + " wins !")
            for i in range(3):
                    if self.matrix[0][i] == self.matrix[1][i] and self.matrix[0][i] == self.matrix[2][i]:
                            winner = True
                            return (self.matrix[0][i] + " wins !")
            if self.matrix[0][0] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][2] or self.matrix[0][2] == self.matrix[1][1] and self.matrix[1][1] == [2][0]:
                    winner = True
                    return (self.matrix[1][1] + " wins !")
            else:
                    spaceFound = False
                    for i in range(3):
                            for j in range(3):
                                    if self.matrix[i][j] == " ":
                                            spaceFound = True
                    if spaceFound == False and winner == False:
                            return("Draw !")
                    elif spaceFound == True and winner == False:
                            return("Game in progress.")