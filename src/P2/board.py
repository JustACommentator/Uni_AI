import pygame as pg
import settings


def fileRowToCoordinates(filerow):
    return filerow[0] * FIELD, filerow[1] * FIELD


def drawBoard(board):
    for filerow, field in board.items():
        color = '#DFBF93' if field else '#C5844E'
        pg.draw.rect(SCREEN, color, (*fileRowToCoordinates(filerow), FIELD, FIELD))


pg.init()
WIDTH, HEIGHT = 800, 800
FIELD = WIDTH // settings.QUEEN_COUNT
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
QUEEN = pg.image.load('queen.png')
BOARD = {(s, z): s % 2 == z % 2 for s in range(settings.QUEEN_COUNT) for z in range(settings.QUEEN_COUNT)}


def drawQueens(queenstring):
    scale = 8 / settings.QUEEN_COUNT

    for i in range(len(queenstring)):
        SCREEN.blit(pg.transform.scale(QUEEN, (80 * scale, 80 * scale)), (10 * scale + 100 * scale * i, (int(queenstring[i]) - 1) * 100 * scale + 10 * scale))


def drawQueens_board(board):
    scale = 8 / settings.QUEEN_COUNT

    for i in range(settings.QUEEN_COUNT):
        for k in range(settings.QUEEN_COUNT):
            if board[i][k] == "Q":
                SCREEN.blit(pg.transform.scale(QUEEN, (80 * scale, 80 * scale)), (10 * scale + 100 * scale * k, i * 100 * scale + 10 * scale))


def update(queenString):
    SCREEN.fill((0, 0, 0))
    drawBoard(BOARD)
    drawQueens(queenString)

    pg.display.flip()


def update_board(board):
    SCREEN.fill((0, 0, 0))
    drawBoard(BOARD)
    drawQueens_board(board)

    pg.display.flip()
