import random


class QueensProblem:

    def __init__(self):
        self.queenString = ""

    def setBoard(self, queenString):
        self.queenString = queenString

    def randomizeBoard(self):
        self.queenString = ""
        for i in range(8):
            self.queenString += str(random.randint(1, 8))

    def printBoard(self):
        for i in range(8):
            for k in range(8):
                if int(self.queenString[k]) == i + 1:
                    print("Q  ", end="")
                else:
                    print(".  ", end="")
            print("")

    def fitnessScore(self):  # using number of non-attacking pairs of queens as fitness score. Optimal: 28
        score = 0

        for x1 in range(8):
            y = int(self.queenString[x1])

            for x2 in range(8):

                if x2 == x1:
                    continue
                if int(self.queenString[x2]) == y:
                    continue
                if x2 + int(self.queenString[x2]) == x1 + y:
                    continue
                if x2 - int(self.queenString[x2]) == x1 - y:
                    continue
                score += 1

        return int(score / 2)  # each queen is counted twice per pair


Q = QueensProblem()

Q.randomizeBoard()

Q.printBoard()
