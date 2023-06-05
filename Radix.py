
#  File: Radix.py

#  Description: sorts strings that have a mix of lower case letters and digits

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    # Create a list and keep your Queue objects there
    q_lst = [Queue() for i in range (37)]
    
    # dictionary where the key is a character (either a digit or a lower case letter) 
    # value is an index in the above list
    # first add to the dictionary a character not in the list with index 0 
    c_dict = {'#':0}

    # add keys and values to c_dict
    for i in range(1,37):
        # 0 has an ASCII value of 48 
        # digits come before letters 
        # append to the dict a value for each digit and letter 
        # in a sequential order 
        if i <= 10:
            c_dict[chr(47 + i)] = i 
        # a has ASCII of 97
        else: 
            c_dict[chr(86 + i)] = i  

    # get length of longest string in list a
    len_lst = [len(x) for x in a]
    idx_long = max(len_lst)

    # add space holder # to items shorter than length of longest item in list
    for i in range (len(a)): 
        if len(a[i]) < idx_long:
            a[i] = a[i] + '#'*(idx_long-len(a[i]))

    # start off with original list passed 
    ordered = a
    for i in range(-1, -(idx_long + 1), -1):
        # add to queue 
        # if item we are looking at is shorter than longest one, ignore the respective
        # index and just bring it to the front, hence the additional # 
        for item in ordered: 
            q_lst[c_dict[item[i]]].enqueue(item)
    
    # after adding to queue, reset ordered to deqeue
        ordered = []
        for item in q_lst: 
            while not item.is_empty():
                ordered.append(item.dequeue())
   
    # get rid of all # placeholders 
    for i in range(len(ordered)):
        ordered[i] = ordered[i].replace('#', '')
    return ordered 


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    