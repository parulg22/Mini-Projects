#Uses linear and binary search algorithms to find minimum lines Vyasa must write 


import sys, time

# Input: int v, minimum lines of code 
#        int k an integer representing the productivity factor
# Output: computes and returns the sum of the series 

def sums (v, k):
    # exponent (starts off with 0)
    e = 0
    # sum
    total_sum = 0
    # initialize current term for sum of series 
    current_term = v
    while current_term > 0: 
        current_term = v // (k ** e)   
        total_sum += current_term   
        e += 1 
    return total_sum

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  # use linear search here
  # uses an imaginary list with length of n
  # when the sum of values starting with i equals n, return that value 
    i = 1
    while sums(i,k) < n: 
        i += 1
    return i
    
# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
  # mid is first n divided by 2, then adjusts 
    lo = 0
    hi = n
    while (lo <= hi):
        mid = (lo + hi) // 2 
        temp_sum=sums(mid,k)
        if temp_sum == n:
            break 
        elif temp_sum < n:
            lo = mid + 1
        elif temp_sum > n: 
            hi = mid - 1
    return mid


# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
