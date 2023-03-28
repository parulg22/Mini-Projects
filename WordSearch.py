# This program determines if a word is in a word search and returns the index of the word

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    line = sys.stdin.readline()
    line = line.strip()
    numLines = int(line)

    grid = []
    wrdlst = []
    lst = []

    for i in range(numLines + 2): #+2 ignores the whitespaces
        line = sys.stdin.readline()
        line = line.strip()
        if(line): #If line is not empty, add to lst
            for x in range(len(line)):
                if(line[x:x+1] != " "):
                    lst.append(line[x:x+1])

            grid.append(lst)
        lst = []
            
    line = sys.stdin.readline()
    line = line.strip()
    numWords = int(line)
    
    for i in range(numWords):
        line = sys.stdin.readline()
        line = line.strip()
        wrdlst.append(line)

    return grid, wrdlst
    
# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid

def checkWord(i,j, word, grid): #if one passes, then we found the word
    return checkR(i,j, word, grid) or checkL(i,j, word, grid) or checkUp(i,j, word, grid) or checkDown(i,j, word, grid) or checkUR(i,j, word, grid) or checkUL(i,j, word, grid) or checkDR(i,j, word, grid) or checkDL(i,j, word, grid)

def checkR(i,j, word, grid): 
    if(len(grid[i]) - j < len(word)): #check for out of bounds error
        return False

    for k in range(1, len(word)):
        if(word[k:k+1] != grid[i][j+k]): #check that each substring matches
            return False
    return True

def checkL(i,j, word, grid):
    if(j +1 < len(word)):
        return False
    for k in range(1, len(word)):
        if(word[k:k+1] != grid[i][j-k]):
            return False
    return True

def checkUp(i,j, word, grid):
    if(i+1 < len(word)):
        return False
    
    for k in range(1, len(word)):
        if(word[k:k+1] != grid[i-k][j]):
            return False
    return True
def checkDown(i,j, word, grid):
    if(len(grid) - i < len(word)):
        return False
    
    for k in range(1, len(word)):
        if(word[k:k+1] != grid[i+k][j]):
            return False
    return True

def checkUR(i,j, word, grid):
    if(i+1 < len(word) or len(grid[i]) - j < len(word)):
        return False
    
    for k in range(1, len(word)):
        if(word[k:k+1] != grid[i-k][j+k]):
            return False
    return True

def checkUL(i,j, word, grid):
    if(i+1 < len(word) or j + 1 < len(word)):
        return False
    
    for k in range(1, len(word)):
        if(word[k:k+1] != grid[i-k][j-k]):
            return False
    return True

def checkDR(i,j, word, grid):
    if(len(grid) -i < len(word) or len(grid[i]) - j < len(word)):
        return False
    
    for k in range(1, len(word)):
        if(word[k:k+1] != grid[i+k][j+k]):
            return False
    return True

def checkDL(i,j, word, grid):
    if(len(grid) -i < len(word) or j + 1 < len(word)):
        return False
    
    for k in range(1, len(word)):
        if(word[k:k+1] != grid[i+k][j-k]):
            return False
    return True


def find_word (grid, word):
    firstLetter = word[:1]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == firstLetter):
                if(checkWord(i, j, word, grid)):
                    return i+1, j+1
    return 0, 0


def main():
  # read the input file from stdin
    word_grid, word_list = read_input()
  # find each word and print its location
    for word in word_list:
        location = find_word (word_grid, word)
        print (word + ": " + str(location))

if __name__ == "__main__":
    main()