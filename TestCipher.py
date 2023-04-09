#  Description: This program uses various encoding techniques to encode and decode text that is given to the program

import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    # Create a 2D list of '-'
    lst = [[] for i in range (key)] 
    for i in range(key):
        for j in range(len(strng)):
            lst[i].append("-")
    
    i = 0
    j = 0
    for k in range(len(strng)):
        lst[i][j] = strng[k:k+1]
        if(i == key - 1):
            updown = False
        elif(i == 0):
            updown = True
        # for True we are going downwards
        if(updown):
            i += 1
        # for False we are moving back upwards
        elif(not updown):
            i -= 1
        j += 1
    str = ""
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if(lst[i][j] != "-"):
                str += lst[i][j]

    return str


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    # create a 2D list of '-'
    lst = [[] for i in range (key)] 
    for i in range(key):
        for j in range(len(strng)):
            lst[i].append("-")
    
    # adds hashtags for every space on the diagonal where a letter should be inserted
    i = 0
    j = 0
    for k in range(len(strng)):
        lst[i][j] = "#"
        if(i == key - 1):
            updown = False
        elif(i == 0):
            updown = True
        if(updown):
            i += 1
        elif(not updown):
            i -= 1
        j += 1
    
    # Putting the letters in a 2D list
    counter = 0
    for i in range(key):
        for j in range(len(strng)):
            if(lst[i][j] == "#"):
                lst[i][j] = strng[counter: counter+1]
                counter += 1
    
    # Creating in a new string merging all of the letters diagonally
    i = 0
    j = 0
    newstr = ""
    for k in range(len(strng)):
        newstr += lst[i][j]
        if(i == key - 1):
            updown = False
        elif(i == 0):
            updown = True
        if(updown):
            i += 1
        elif(not updown):
            i -= 1
        j += 1

    return newstr
	# placeholder for the actual return statement

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
    strng = strng.lower()
    newstr = ""
    for i in range(len(strng)):
        if("a" <= strng[i:i+1] <= "z"):
            newstr += strng[i:i+1]

    return newstr	# placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
    # add the difference bw the first letter and 'a' to the second letter
    # we subtract with 'a' bc 'a' is the lowest ascii value 
    shift = ord(p) - ord("a")
    sum = (ord(s) + shift)
    #if the ascii goes beyond 'z' then loop back around to 'a'
    if(sum > ord("z")):
        sum -= ord("z")
        char = chr(96 + sum)
    else:
        char = chr(sum)
    return char

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
    # first letter and 'a' then subtract that from the 2nd letter
    diff = ord(s) - (ord(p) - ord("a"))
    # if the ascii is less than 'a', loop back around to 'z'
    if(diff < ord("a")):
        diff2 = ord("a") - 1 - diff
        char = ord("z") - diff2
        char = chr(char)
    else:
        char = chr(diff)
    return char

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    newstr = ""
    # make sure phrase key is longer than or = to strng
    while(len(phrase) < len(strng)):
        phrase *= 2
    for i in range(len(strng)):
        newstr += encode_character(strng[i:i+1], phrase[i:i+1])
    return newstr	# placeholder for the actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    newstr = ""
    # make sure phrase key is longer than or = strng
    while(len(phrase) < len(strng)):
        phrase *= 2
    for i in range(len(strng)):
        newstr += decode_character(phrase[i:i+1],strng[i:i+1])
    return newstr

def main():

  # read the plain text from stdin
    rail_cipher_text = sys.stdin.readline()
    rail_cipher_text = rail_cipher_text.strip()
  # read the key from stdin
    rfc_key = sys.stdin.readline()
    rfc_key = rfc_key.strip()
  # encrypt and print the encoded text using rail fence cipher
    print(rail_fence_encode(rail_cipher_text, rfc_key))

  # read encoded text from stdin
    encoded_text = sys.stdin.readline()
    encoded_text = encoded_text.strip()
  # read the key from stdin
    encoded_key = sys.stdin.readline()
    encoded_key = encoded_key.strip()
  # decrypt and print the plain text using rail fence cipher
    print(rail_fence_decode(encoded_text, encoded_key))
  
  # read the plain text from stdin
    v_text = sys.stdin.readline()
    v_text = v_text.strip()
  # read the pass phrase from stdin
    v_key = sys.stdin.readline()
    v_key = v_key.strip()
  # encrypt and print the encoded text using Vigenere cipher
    print(vigenere_encode(v_text, v_key))
  
  # read the encoded text from stdin
    v_encoded = sys.stdin.readline()
    v_encoded = v_encoded.strip()
  # read the pass phrase from stdin
    v_phrase = sys.stdin.readline()
    v_phrase = v_phrase.strip()

  # decrypt and print the plain text using Vigenere cipher
    print(vigenere_decode(v_encoded, v_phrase))

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN

if __name__ == "__main__":
    main()
