import random


class QueensProblem:

    def __init__(self):
        self.queenString = ""

    def set(self, queenString):
        self.queenString = queenString

    def randomize(self):
        self.queenString = ""
        for i in range(8):
            self.queenString += str(random.randint(1, 8))

    def print(self):
        for i in range(8):
            for k in range(8):
                if int(self.queenString[k]) == i + 1:
                    print("Q  ", end="")
                else:
                    print(".  ", end="")
            print("")
