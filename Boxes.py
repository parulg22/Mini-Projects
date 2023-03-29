#  File: Boxes.py

#  Description: This gets the maximum number of boxes that can nest into one, and the permutations of that number that can nest.


import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  # number of boxes that can fit at an index
  nesting_lst = []
  for i in range(len(box_list)):
    nesting_lst.append(1)
    count = 0
    for j in range(i-1, -1, -1):
      if(does_fit(box_list[j], box_list[i])):
        if(nesting_lst[j] > count):
          count = nesting_lst[j]
    nesting_lst[i] += count

  max_nest = max(nesting_lst)
  num_sets = []
  nesting_combos(box_list, [], 0, max_nest, num_sets)
  num_sets = len(num_sets) 
  return max_nest, num_sets

# Input: 1-D list of boxes that is sorted
#        basket to store subsets
#        max number of boxes that fit into one
#        list that will hold all possible permutations
# Output: gets num_sets -> all of the possible combos
def nesting_combos(box_list, b, idx, max_nest, num_sets):
  hi = len(box_list)
  if(idx == hi or len(b) == max_nest):
      # if the boxes fit inside one another
      var = True
      for i in range(len(b) - 1):
        if(not does_fit(b[i], b[i+1])):
          var = False
      if(var and len(b) == max_nest):
        num_sets.append(b)
      return
  else:
    # make sure boxes are fitting inside one another, else discard the subset
    if(len(b) >= 2):
      var = True
      for i in range(len(b) - 1):
        if(not does_fit(b[i], b[i+1])):
          var = False
      if(not var):
        return
      else:
        c = b[:]
        b.append(box_list[idx])
        nesting_combos(box_list, b, idx + 1, max_nest, num_sets)
        nesting_combos(box_list, c, idx + 1, max_nest, num_sets)
    else:
      c = b[:]
      b.append(box_list[idx])
      nesting_combos(box_list, b, idx + 1, max_nest, num_sets)
      nesting_combos(box_list, c, idx + 1, max_nest, num_sets)

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  """print (box_list)
  print()"""  
  
  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  """print (box_list)
  print()"""

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()