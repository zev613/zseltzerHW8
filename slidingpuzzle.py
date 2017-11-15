################################
# slidingpuzzle.py
# Part of homework 8, problem 1
################################

import pdb

class SlidingPuzzle:
    def __init__(self, rows, cols):
        #pdb.set_trace()
        self.r = rows
        self.c = cols
        self.current_board = []
        acc = 0
        for r in range(1, self.r + 1):
            print('r:', r)
            self.current_board.append([])
            for c in range(1, self.c + 1):
                print('c:', c)
                self.current_board[r].append(acc)
                acc += 1

    def displayPuzzle(self):
        pass
