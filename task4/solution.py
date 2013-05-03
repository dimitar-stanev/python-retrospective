class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard():
    matrix= [[" "]*3 for i in range(3)]
    
    VALID_INDECES = [ "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    
    VALID_VALUES = ["X", "O"]
    
    def restartGame(self):
        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = " "
        self.last_move = None
        
    def __str__(self):
        return ("\n  -------------\n"
        +"3 | "+ self.matrix[0][0] + " | " + self.matrix[0][1] + " | " + self.matrix[0][2] + " |\n"
        +"  -------------\n"
        +"2 | "+ self.matrix[1][0] + " | " + self.matrix[1][1] + " | " + self.matrix[1][2] + " |\n"
        +"  -------------\n"
        +"1 | "+ self.matrix[2][0] + " | " + self.matrix[2][1] + " | " + self.matrix[2][2] + " |\n"
        +"  -------------\n"
        +"    A   B   C  \n")
    
    def __setitem__(self, index, value):

        if index not in self.VALID_INDECES:
            raise InvalidKey

        if value not in self.VALID_VALUES:
            raise InvalidValue

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

        self.matrix = [[" "]*3 for i in range(3)]
        
        self.last_move = None

    def game_status(self):

        winner = False

        for i in range(3):
            if self.matrix[i][0] == self.matrix[i][1] and self.matrix[i][0] == self.matrix[i][2] and self.matrix[i][0] != " ":
                winner = True
                return (self.matrix[i][0] + " wins!")
                break

        for i in range(3):
            if self.matrix[0][i] == self.matrix[1][i] and self.matrix[0][i] == self.matrix[2][i] and self.matrix[0][i] != " ":
                winner = True
                return (self.matrix[0][i] + " wins!")
                break

        if self.matrix[0][0] == self.matrix[1][1] and self.matrix[0][0] == self.matrix[2][2] and self.matrix[0][0] != " ":
            winner = True
            return (self.matrix[1][1] + " wins!")
        
        if self.matrix[0][2] == self.matrix[1][1] and self.matrix[0][2] == self.matrix[2][0] and self.matrix[0][2] != " ":
            winner = True
            return (self.matrix[1][1] + " wins!")

        if winner == False:
            spaceFound = False
            for i in range(3):
                    for j in range(3):
                            if self.matrix[i][j] == " ":
                                    spaceFound = True
                                    
            if spaceFound == False and winner == False:
                    return("Draw!")
                
            elif spaceFound == True and winner == False:
                    return("Game in progress.")
