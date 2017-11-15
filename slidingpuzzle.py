################################
# slidingpuzzle.py
# Part of homework 8, problem 1
################################

import random

class SlidingPuzzle:
    def __init__(self, rows, columns):
        self.row = rows
        self.col = columns
        self.current_board = []
        acc = 0
        for row in range(0, self.row):
            self.current_board.append([])
            for col in range(0, self.col):
                self.current_board[row].append(acc)
                acc += 1
        print('<DEBUG>', self.current_board, '\n')

    def displayPuzzle(self):
        current_line = '' #temp var to add numbers then print as a line
        for row in range(self.row):
            for col in range(self.col):
                if self.current_board[row][col] >= 10: #because the space is after the number, the spaces are shorter after 9 to fit double digits
                    current_line += str(self.current_board[row][col]) + ' '
                else:
                    current_line += str(self.current_board[row][col]) + '  '
            print(current_line.rstrip())
            current_line = ''

    def move(self, row_index, col_index):
            for this_row in range(self.row):
                for this_col in range(self.col):
                    #(row,col) is the zero's index
                    if self.current_board[this_row][this_col] == 0:
                        store_value = self.current_board[row_index][col_index]
                        self.current_board[row_index][col_index] = self.current_board[this_row][this_col]
                        self.current_board[this_row][this_col] = store_value

    def legalMoves(self):
        for this_row in range(self.row):
            for this_col in range(self.col):
                #(row,col) is the zero's index
                if self.current_board[this_row][this_col] == 0:
                    zero_row = this_row
                    zero_col = this_col
                    #TODO: Figure out how to determine which moves are legal and which are not.
                    #Then return a list of the tuple of each such index (rol, col)
