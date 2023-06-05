#  File: Reducible.py

#  Description: Reduces a word by removing a letter and seeing if that's a 
# word all the way down to one letter.

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True


# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  num = hash_word(s, const)
  return const - num % const
   

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  # only add the word if 'a' 'i' or 'o' is in it because that will make it reducible
  if("a" not in s and "i" not in s and "o" not in s):
    return
  idx = hash_word(s, len(hash_table))
  # if hash table at idx is empty
  if(not hash_table[idx]):
    hash_table[idx] = s
  else:
    count = 1
    step = step_size(s, 3)
    while(True):
      # find which index we are checking next - if available, insert at that index
      ind = (idx + step*count) % len(hash_table)
      if(not hash_table[ind]):
        hash_table[ind] = s
        break
      count += 1
      

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  idx = hash_word(s, len(hash_table))
  if(hash_table[idx] == s):
    return True
  elif(not hash_table[idx]):
    return False
  # use step size to check the next idx for this word
  else:
    count = 1
    step = step_size(s, 3)
    while(True):
      ind = (idx + step*count) % len(hash_table)
      if(not hash_table[ind]):
        return False
      elif(hash_table[ind] == s):
        return True
      count += 1


# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    # if the last letter is reducible, return true
    if(s == "a" or s == "i" or s == "o"):
      return True
    # if the current string is not a word
    elif(not find_word(s, hash_table)):
        return False
    else:
      # if we already found the word to be reducible, return true
      if(find_word(s, hash_memo)):
        return True
      else:
        # check if the word is reducible by removing one letter at a time
        for i in range(len(s)):
          if(is_reducible(s[:i] + s[i+1:], hash_table, hash_memo)):
            if(not find_word(s, hash_memo)):
              insert_word(s, hash_memo)
            return True
        return False


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  lst = []
  len_lst = [len(x) for x in string_list]
  longest = max(len_lst)
  for i in range(len(string_list)):
    if(len(string_list[i]) == longest):
      lst.append(string_list[i])
  return lst
      

def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  length = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  curr_num = 2*length
  while(not is_prime(curr_num)):
    curr_num += 1
  
  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  hash_list = ["" for i in range(curr_num)]

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for i in range(length):
    insert_word(word_list[i], hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []

  # populate the hash_memo with M blank strings
  new_num = int(.2 * length)
  while(not is_prime(new_num)):
    new_num += 1
  hash_memo = ["" for i in range(new_num)]

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for i in range(length):
    if(is_reducible(word_list[i], hash_list, hash_memo)):
      reducible_words.append(word_list[i])

  # find the largest reducible words in reducible_words
  longest_lst = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  # one word per line
  longest_lst.sort()
  for i in range(len(longest_lst)):
    print(longest_lst[i])

if __name__ == "__main__":
  main()