import random


class QueensProblem:
    def __init__(self):
        self.board = [["+" for i in range(8)] for k in range(8)]

    def setBoard(self, queenString):
        for i in range(8):
            self.board[i][int(queenString[i])-1] = "Q"

    def randomizeBoard(self):
        queenString = ""
        for i in range(8):
            queenString += str(random.randint(1, 8))
        self.setBoard(queenString)

    def printBoard(self):
        for i in range(len(self.board)):
            for k in range(len(self.board[0])):
                print(self.board[k][i] + "  ", end="")
            print("")



Q = QueensProblem()
Q.randomizeBoard()
Q.printBoard()