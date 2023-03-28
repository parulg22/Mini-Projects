
#  Description: combines overlapping intervals, removes intervals that are subsets of other intervals, combines adjacent
#               intervals, sorts intervals by ascending order of first index and interval size 

import sys

#Input: reads pairs of intervals in a given file 
#Output: returns a list with all the tuples from the file 
def read_input():
    line = sys.stdin.readline()
    line = line.strip()
    numintervals = int(line)
    tuples_list = []
    for i in range(numintervals):
        line = sys.stdin.readline()
        line = line.strip()
        a,b = line.split(" ") 
        tup = int(a), int(b) #creates tuple 
        tuples_list.append(tup) #adds tuple to list 
    return(tuples_list)


# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):

    # checking for adjacent pairs
    i = 0
    j = i + 1
    while i < (len(tuples_list)-1):
        first_bound = tuples_list[i][0]
        second_bound = tuples_list[i][1]
        while j < len(tuples_list):
            # if first index is within second interval 
            if (first_bound) == tuples_list[j][1]: 
                tuples_list[i] = tuples_list[j][0], tuples_list[i][1]
                tuples_list.pop(j)
                j-=1 
            # if second index is in second interval 
            elif (second_bound) == tuples_list[j][0]:
                tuples_list[i] = tuples_list[i][0], tuples_list[j][1]
                tuples_list.pop(j)
                j-=1 
            j +=1
        i+=1
        j = i+1 
 

    remove_list = [] #tuples to be removed after checking for pairs that are subsets of others
    # checking for susbset pairs 
    i = 0
    j = i + 1
    bool = False
    while i < (len(tuples_list)-1):
        while j < len(tuples_list):
            # if first index is within second interval 
            if (tuples_list[i][0] >= tuples_list[j][0]) and (tuples_list[i][1] <= tuples_list[j][1]): 
                tuples_list.pop(i)
                bool = True
            # if second index is in second interval 
            elif (tuples_list[i][0] <= tuples_list[j][0]) and (tuples_list[i][1] >= tuples_list[j][1]):
                tuples_list.pop(j)
                j=j-1
            j +=1
        if(bool):
                i -= 1
                bool = False
        i+=1
        j = i+1
    
    #remove overlapping intervals
    i = 0
    j = i + 1
    while i < (len(tuples_list)-1):
        while j < len(tuples_list):
            # if first index is within second interval 
            if (tuples_list[i][0] >= tuples_list[j][0]) and (tuples_list[i][0] <= tuples_list[j][1]): 
                tuples_list[i] = tuples_list[j][0], tuples_list[i][1]
                tuples_list.pop(j)
                j=i+1
            # if second index is in second interval 
            elif (tuples_list[i][1] >= tuples_list[j][0]) and (tuples_list[i][1] <= tuples_list[j][1]):
                tuples_list[i] = tuples_list[i][0], tuples_list[j][1]
                tuples_list.pop(j)
                j=i+1
            j +=1
        i+=1
        j = i+1

#remove overlapping intervals
    i = 0
    j = i + 1
    while i < (len(tuples_list)-1):
        while j < len(tuples_list):
            # if first index is within second interval 
            if (tuples_list[i][0] >= tuples_list[j][0]) and (tuples_list[i][0] <= tuples_list[j][1]): 
                tuples_list[i] = tuples_list[j][0], tuples_list[i][1]
                tuples_list.pop(j)
                j=i+1
            # if second index is in second interval 
            elif (tuples_list[i][1] >= tuples_list[j][0]) and (tuples_list[i][1] <= tuples_list[j][1]):
                tuples_list[i] = tuples_list[i][0], tuples_list[j][1]
                tuples_list.pop(j)
                j=i+1
            j +=1
        i+=1
        j = i+1
    

    # checking for susbset pairs 
    i = 0
    j = i + 1
    bool = False
    while i < (len(tuples_list)-1):
        while j < len(tuples_list):
            # if first index is within second interval 
            if (tuples_list[i][0] >= tuples_list[j][0]) and (tuples_list[i][1] <= tuples_list[j][1]): 
                tuples_list.pop(i)
                bool = True
            # if second index is in second interval 
            elif (tuples_list[i][0] <= tuples_list[j][0]) and (tuples_list[i][1] >= tuples_list[j][1]):
                tuples_list.pop(j)
                j=j-1
            j +=1
        if(bool):
                i -= 1
                bool = False
        i+=1
        j = i+1

    # sorts by ascending order in regards to first index of tuple
    for i in range(len(tuples_list)-1): 
        mini = tuples_list[i][0] #stores the first value of the the first pair, keeps updating with subsequent pairs 
        mini_index = i
        for j in range(i+1, len(tuples_list)):
            if mini > tuples_list[j][0]:
                mini = tuples_list[j][0] 
                mini_index = j
        if mini_index != i: 
            tup = tuples_list[mini_index]
            tuples_list[mini_index] = tuples_list[i]
            tuples_list[i] = tup
    return(tuples_list)


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    for i in range(len(tuples_list)-1): 
        mini_len = tuples_list[i][1] - tuples_list[i][0] #stores the first value of the the first pair, keeps updating with subsequent pairs 
        mini_index = i
        for j in range(i+1, len(tuples_list)):
            # if length of second interval is smaller 
            if mini_len > tuples_list[j][1] - tuples_list[j][0]:
                mini_len = tuples_list[j][1] - tuples_list[j][0]
                mini_index = j
        # if index for smallest interval changed 
        if mini_index != i: 
            # swap intervals 
            tup = tuples_list[mini_index]
            tuples_list[mini_index] = tuples_list[i]
            tuples_list[i] = tup
    return(tuples_list)


def main():
  # read the input data and create a list of tuples
  lst = read_input()
  
  # merge the list of tuples
  merged_lst = merge_tuples(lst)

  # print the merged list
  print(merged_lst)

  # sort the list of tuples according to the size of the interval
  sorted_lst = sort_by_interval_size(merged_lst)

  # print the sorted list
  print(sorted_lst)


if __name__ == "__main__":
  main()