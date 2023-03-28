
#  Explores four different algorithms to find greatest sum path in a triangle 

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    # create a list that stores sum of every possible path 
    sums_lst = []
    brute_helper(grid, 0, 0, 0, sums_lst)
    # return largest value in list as greatest sum 
    return max(sums_lst)


def brute_helper (grid, sums, i, j, sums_lst):
    if i == len(grid):
        # add final sums value to the list 
        sums_lst.append(sums)
    else: 
        # add value to sums, move down or move down right 
        brute_helper(grid, sums + grid[i][j], i + 1, j, sums_lst)
        brute_helper(grid, sums + grid[i][j], i + 1, j + 1, sums_lst)


# returns the greatest path sum using greedy approach
def greedy (grid):
    total_sum = 0
    j = 0
    for i in range(len(grid)):
        # find the max value between one down and one down right
        total_sum += max(grid[i][j], grid[i][j+1])
        # reassigns value of j to one that holds max 
        if grid[i][j+1] > grid[i][j]:
            j += 1
    return total_sum 


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    return dc_helper(grid, 0, 0, 0)

def dc_helper(grid, sums, i, j):
    if i == len(grid):
        return sums
    else: 
        return max((dc_helper(grid, sums + grid[i][j], i + 1, j)), (dc_helper(grid, sums + grid[i][j], i + 1, j + 1)))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    # create a copy of original grid 
    new_grid = grid[:]
    # start at second to last row
    for i in range(len(grid)-2, -1, -1):
        for j in range(len(grid[i])):
            # if adding empty value, break and move to next index 
            if grid[i][j] == 0:
                break
            # add to the copied grid the max of one down and one down right 
            new_grid[i][j] += max(new_grid[i+1][j], new_grid[i+1][j+1])
    # return the greatest sum, which is stored at first index 
    return new_grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  print(divide_conquer(grid))
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()
