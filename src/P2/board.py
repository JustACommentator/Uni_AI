import pygame as pg


def fileRowToCoordinates(filerow):
    return filerow[0] * FIELD, filerow[1] * FIELD


def drawBoard(board):
    for filerow, field in board.items():
        color = '#DFBF93' if field else '#C5844E'
        pg.draw.rect(SCREEN, color, (*fileRowToCoordinates(filerow), FIELD, FIELD))


pg.init()
WIDTH, HEIGHT = 800, 800
FIELD = WIDTH // 8
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
QUEEN = pg.image.load('queen.png')
BOARD = {(s, z): s % 2 == z % 2 for s in range(8) for z in range(8)}


def drawQueens(queenstring):
    for i in range(len(queenstring)):
        SCREEN.blit(QUEEN, (10 + 100 * i, (int(queenstring[i]) - 1) * 100 + 10))


def update(queenString):
    SCREEN.fill((0, 0, 0))
    drawBoard(BOARD)
    drawQueens(queenString)

    pg.display.flip()
