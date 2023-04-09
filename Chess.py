#  File: Chess.py

#  Description: prints the number of possible combinations to place n number of queens on a given size board

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    # make a list to store solutions 
    self.sol = []
    # make a board of n by n dimensions
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def solve(self, col):
    if col == self.n:   
      # once we've reached the final column, store that board's output/solution
      # in a list 
      self.sol.append([self.board[i][j] for i in range(self.n) for j in range(self.n)])
    else:
      for i in range(self.n):
        if(self.is_valid(i, col)):
          # place queen on board (safe spot)
          self.board[i][col] = "Q"
          # move onto the next column and repeat process 
          self.solve(col + 1)
          self.board[i][col] = "*"


def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)

  # place the queens on the board and count the solutions
  game.solve(0)
  
  # print the number of solutions
  print(len(game.sol))
 
if __name__ == "__main__":
  main()