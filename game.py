################################
# game.py
# Part of homework 8, problem 2
################################

#from slidingpuzzletest import *

from slidingpuzzle import *

def main():
    board = SlidingPuzzle(3,4)
    legal_moves = board.legalMoves()
    board.displayPuzzle()
    #board.move(legal_moves[0][0], legal_moves[0][1])
    #board.displayPuzzle()
    print('\n')
    board.move(legal_moves[0][0], legal_moves[0][1])
    board.displayPuzzle()

    print('\n')
    board.move(legal_moves[1][0], legal_moves[1][1])
    board.displayPuzzle()

    #board.scramble(2)
    #board.displayPuzzle()

main()
