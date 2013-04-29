class TicTacToeBoard():

    matrix = [[" "]*3 for i in range(3)]

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
        if index[0]=="A" and index[1]=="1":
            self.matrix[2][0] = value
        elif index[0]=="A" and index[1]=="2":
            self.matrix[1][0] = value
        elif index[0]=="A" and index[1]=="3":
            self.matrix[0][0] = value
        elif index[0]=="B" and index[1]=="1":
            self.matrix[2][1] = value
        elif index[0]=="B" and index[1]=="2":
            self.matrix[1][1] = value
        elif index[0]=="B" and index[1]=="3":
            self.matrix[0][1] = value
        elif index[0]=="A" and index[1]=="1":
            self.matrix[2][2] = value
        elif index[0]=="A" and index[1]=="2":
            self.matrix[1][2] = value
        elif index[0]=="A" and index[1]=="3":
            self.matrix[0][2] = value
    def __init__(self):
        print("NEW GAME STARTED !")
    def game_status(self):
            winner = False
            for i in range(3):
                    if matrix[i][0] == matrix[i][1] and matrix[i][0] == matrix[i][2]:
                            winner = True
                            print ("Player " + matrix[0][i] + " wins !")
            for i in range(3):
                    if matrix[0][i] == matrix[1][i] and matrix[0][i] == matrix[2][i]:
                            winner = true
                            print ("Player " + matrix[0][i] + " wins !")
            if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] and matrix[1][1] == [2][0]:
                    winner = True
                    print ("Player " + matrix[1][1] + " wins !")
            else:
                    spaceFound = False
                    for i in range(3):
                            for j in range(3):
                                    if matrix[i][j] == " ":
                                            spaceFound = True
                    if spaceFound == False and winner == False:
                            print("Game is draw !")
                    elif spaceFound == True and winner == False:
                            print("Game in progress !")