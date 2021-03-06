################################
# game.py
# Part of homework 8, problem 2
################################

#from slidingpuzzletest import *

from slidingpuzzle import *

def main():
    print('Welcome to the Sliding Puzzle Game!')
    height = int(input('Please enter a height for the board.'))
    width = int(input('Please enter a width for the board.'))
    board = SlidingPuzzle(height,width)
    print('What difficulty do you want to use?')
    difficulty = input('Type 1 for Easy, 2 for Medium or 3 for Hard.')
    while difficulty not in ['1', '2', '3']:
        difficulty = input('Your input was invalid. Please try again.')
    if difficulty == '1':
        board.scramble(3)
    elif difficulty == '2':
        board.scramble(11)
    elif difficulty == '3':
        board.scramble(19)

    while board.isSolved != True
        board.displayPuzzle()
        print('Select a position to swamp with the zero.')
        userRow = int(input('Select a row to move to.'))
        userCol = int(input('Select a column to move to.'))
        while (userRow, userCol) not in board.legalMoves:
            userRow = input('You selected an illegal row. Please Select a different row.')
            userCol = input('You selected an illegal column. Please Select a different column.')
        if (userRow, userCol) in board.legalMoves:
            board.move(userRow, userCol)

    if board.isSolved() == True:
        board.displayPuzzle()
        print('Congratulations! You solve the puzzle!')
main()
