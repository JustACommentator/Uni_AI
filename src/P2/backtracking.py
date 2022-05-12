from copy import deepcopy as deep
import pygame.display
import settings
import board

BOARDLIST = []


def safeY(checkerboard, y):
    for i in range(settings.QUEEN_COUNT):
        if checkerboard[i][y] == "Q":
            return False
    return True


def safeX(checkerboard, x):
    for i in range(settings.QUEEN_COUNT):
        if checkerboard[x][i] == "Q":
            return False
    return True


def safeDiag(checkerboard, x, y):
    diagsum = x + y
    diff = x - y
    for i in range(settings.QUEEN_COUNT):
        for k in range(settings.QUEEN_COUNT):
            if i + k == diagsum or i - k == diff:
                if checkerboard[i][k] == "Q":
                    return False
    return True


def safe(x, y, checkerboard):
    return safeX(checkerboard, x) and safeY(checkerboard, y) and safeDiag(checkerboard, x, y)


def backtrack(x, checkerboard):
    if settings.SHOW_PROCESS:
        board.update_board(checkerboard)
    if x >= settings.QUEEN_COUNT:
        BOARDLIST.append(deep(checkerboard))
        return
    for i in range(settings.QUEEN_COUNT):
        if safe(x, i, checkerboard):
            checkerboard[x][i] = "Q"
            backtrack(x + 1, checkerboard)
            checkerboard[x][i] = "."


def start():
    pygame.display.set_caption("Solving...")
    checkerboard = []
    for i in range(settings.QUEEN_COUNT):
        col = []
        for k in range(settings.QUEEN_COUNT):
            col.append(".")
        checkerboard.append(col)
    backtrack(0, checkerboard)