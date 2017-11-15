################################
# game.py
# Part of homework 8, problem 2
################################

#from slidingpuzzletest import *

from slidingpuzzle import *

def main():
    board = SlidingPuzzle(4,4)
    board.displayPuzzle()
    print('\n')
    board.move(2,3)
    board.displayPuzzle()
    print('\n')
    board.move(3,3)
    board.displayPuzzle()
    print('\n')
    board.move(1,1)
    board.displayPuzzle()
    print('\n')

    #board.scramble(2)
    #board.displayPuzzle()

main()
