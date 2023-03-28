#This program prints out the longest common sequence(s) for any two strands of DNA passed.

import sys
# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

#function to test other functions
def test_cases():
  #test all_substrings
  assert all_substrings ("a") == ["a"]
  assert all_substrings("abc") == ["abc", "ab", "bc", "a", "b", "c"]
  assert all_substrings("") == []

  # test longest_subsequence()
  
  #assert longest_subsequence("a", "a") == ["a"]
  assert longest_subsequence("abcd", "bc") == ["bc"]
  assert longest_subsequence("abcd", "xyz") == []


  return "all test cases passed"

#get all substrings of s1 and s2
#Input: s a string
#Output: A lst of all substrings of s
def all_substrings(s):
  #a list of all substrings of s
  result = []

  #define a window
  wnd = len(s)

  #get all substrings
  while(wnd > 0):
    idx = 0
    while(idx + wnd) <= len(s):
      sub_str = s[idx:idx+wnd]
      result.append(sub_str)
      idx += 1
    wnd -= 1
  return result
"""
longestLen = 2
longestSeq = ""
"""
def longest_subsequence (s1, s2):
  """
    Get all the substr of s1
    Check if those substr are in s2
    Only add the longest one
    Once added, set the length of the longest substring
      Only add more if it's longer than that length or equal
      sort the list
      return
    """
  subsequences = []  
  subStr = all_substrings(s1)
  maxLen = 2
  for item in subStr:
    if(len(item) >= maxLen):
      if(item in s2):
        maxLen = len(item)
        subsequences.append(item)
  subsequences.sort()
  return subsequences

def main():
  #test all functions
  test_cases()

  # read the data
  line = sys.stdin.readline()
  line = line.strip()
  numPairs = int(line)
    
  # for each pair call longest_subsequence
  for i in range(numPairs):
    line = sys.stdin.readline()
    s1 = line.strip()

    line = sys.stdin.readline()
    s2 = line.strip()

    #convert to uppercase
    s1 = s1.upper()
    s2 = s2.upper()

    #get the longest subsequences 
    result = longest_subsequence(s1, s2)
        
    # write out result(s)
    if(len(result) == 0):
      print("No Common Sequence Found")
    else:
      for item in result:
        print(item)
        

    
	# insert blank line
    print()

if __name__ == "__main__":
  main()
