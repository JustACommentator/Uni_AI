import random


class QueensProblem:


    def __init__(self):
        self.board = [["+" for i in range(8)] for k in range(8)]


    def setBoard(self, queenString):
        for i in range(8):
            self.board[i][int(queenString[i]) - 1] = "Q"


    def randomizeBoard(self):
        queenString = ""
        for i in range(8):
            queenString += str(random.randint(1, 8))
        self.setBoard(queenString)


    def generateQueenString(self):
        queenString = ""
        for i in range(8):
            queenString += str(self.board[i].index("Q") + 1)
        return queenString


    def printBoard(self):
        for i in range(len(self.board)):
            for k in range(len(self.board[0])):
                print(self.board[k][i] + "  ", end="")
            print("")


def fitnessScore(queenString):  # using number of non-attacking pairs of queens as fitness score. Optimal: 28
    score = 0

    for x1 in range(8):
        y = int(queenString[x1])

        for x2 in range(8):

            if x2 == x1:
                continue
            if int(queenString[x2]) == y:
                continue
            if x2 + int(queenString[x2]) == x1 + y:
                continue
            if x2 - int(queenString[x2]) == x1 - y:
                continue
            score += 1

    return score / 2  # each queen is counted twice per pair


Q = QueensProblem()

Q.setBoard("83742516")

Q.printBoard()

print(fitnessScore(Q.generateQueenString()))