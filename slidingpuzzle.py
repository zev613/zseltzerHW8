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
        #print('<DEBUG>', self.current_board, '\n')
        self.solved_board = self.current_board

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
            for r in range(self.row):
                for c in range(self.col):
                    #(this_row,this_col) is the zero's index
                    if self.current_board[r][c] == 0:
                        store_value = self.current_board[row_index][col_index] #temp var to store the original value of the provided box
                        self.current_board[row_index][col_index] = self.current_board[r][c]
                        self.current_board[r][c] = store_value

    def legalMoves(self):
        for r in range(self.row):
            for c in range(self.col):
                #(row,col) is the zero's index
                if self.current_board[r][c] == 0: #if the
                    z_row = r #row of zero
                    z_col = c #col of zero
        moves = [(z_row - 1, z_col)] #start the moves list with this tuple
        moves.append((z_row + 1, z_col)) #add each of the other 3 possible moves to the moves list
        moves.append((z_row, z_col - 1))
        moves.append((z_row, z_col + 1))
        for item in moves: #iterate to remove illegal moves
            if item[0] < 0 or item[1] < 0: #if the tuple is outside of the puzzle
                moves.remove(item) #remove that tuple, it's an illegal move.
            elif item[0] > len(self.current_board) or item[1] > len(self.current_board[0]): #if tuple is outside of the puzzle
                moves.remove(item) #remove that tuple, it's an illegal move
        print('<DEBUG> moves:', moves)
        return moves #returns the moves list, after removing any tuple in it that was outside of the puzzle
