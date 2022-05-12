import backtracking
import board
import queens_problem
import settings
import time
from pygame import display

backtracking.start()
Q = queens_problem.QueensProblem()
solution_count = len(backtracking.BOARDLIST)
print(f"Number of solutions found: {solution_count}")

if solution_count > 0:
    while True:
        for i in range(len(backtracking.BOARDLIST)):
            display.set_caption(f"Solutions found: {solution_count}; Solution: {i + 1}")
            board.update_board(backtracking.BOARDLIST[i])
            time.sleep(1)
else:
    display.set_caption("No solutions!")
    board.update_board([["."] * settings.QUEEN_COUNT] * settings.QUEEN_COUNT)
    input()
