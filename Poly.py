#  Description: This program uses linked lists to take two polynomials in 
# (coeff, exp) form and adds them and multiplies them
import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    if(self.first == None):
      self.first = Link(coeff, exp)
      return
    
    # get to where the exp is greater than the next one
    prev = self.first
    curr = self.first
    while(curr != None and curr.exp >= exp):
        prev = curr
        curr = curr.next

    new_link = Link(coeff, exp)
    if(curr == self.first):
       new_link.next = curr
       self.first = new_link
       return 

    prev.next = new_link
    new_link.next = curr

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    new_list = LinkedList()

    # add all of the original polynomial to the new list
    curr_self = self.first
    while(curr_self):
      new_list.insert_in_order(curr_self.coeff, curr_self.exp)
      curr_self = curr_self.next
    
    # add  the new polynomial without simplifying
    curr_p = p.first
    while(curr_p):
      new_list.insert_in_order(curr_p.coeff, curr_p.exp)
      curr_p = curr_p.next
    new_list.simplify()
    return new_list
  
  # delete a link from the list
  def delete_link (self, coeff, exp):
    prev = self.first
    curr = self.first
    if(not curr):
      return None
    
    while(curr.coeff != coeff or curr.exp != exp):
      if(curr.next == None):
        return None
      prev = curr
      curr = curr.next

    if (curr == self.first):
      self.first = curr.next
    # delete the node by reassinging previous' pointer
    else:
      prev.next = curr.next
    return curr
  
  # combine like terms
  def simplify(self):
    curr1 = self.first
    if(curr1.coeff == 0):
      self.delete_link(curr1.coeff, curr1.exp)
    if(self.first == None):
      return
    while(curr1.next != None):
      curr2 = curr1.next
      while(curr2 != None):
        # if the exponents are the same, delete the 2nd one in the sum and add the coeff to the first one
        if(curr1.exp == curr2.exp or curr2.coeff == 0):
          curr1.coeff += curr2.coeff
          prev = curr2
          curr2 = curr2.next
          self.delete_link(prev.coeff, prev.exp)
        else:
          curr2 = curr2.next
      if(curr1.next):
        curr1 = curr1.next
  
  # put the list in order of exponents
  def sort(self): 
    if (self.first == None):
        return
    
    curr1 = self.first
    
    while(curr1.next != None):
      curr2 = curr1.next
      while(curr2):
        # if a link is out of order, delete it and insert it in order
        if(curr2.exp > curr1.exp):
          self.delete_link(curr2.coeff, curr2.exp)
          self.insert_in_order(curr2.coeff, curr2.exp)
          curr1 = self.first
          break
        curr2 = curr2.next
      curr1 = curr1.next

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    new_list = LinkedList()
    curr_self = self.first
    curr_p = p.first 
    # multiply every term in both polynomials
    while(curr_self): 
      while(curr_p): 
        new_link = Link(curr_self.coeff * curr_p.coeff, curr_self.exp + curr_p.exp)
        if(new_list.first == None):
          new_list.first = new_link
          new_curr = new_list.first
        else:
          new_curr.next = new_link
          new_curr = new_curr.next
        curr_p = curr_p.next
      curr_p = p.first
      curr_self = curr_self.next
    new_list.simplify()
    new_list.sort()

    return new_list
    
  # create a string representation of the polynomial
  def __str__ (self):
    s = ''
    self.simplify()
    curr = self.first
    while(curr):
      s += str(curr)
      if(curr.next):
            s += ' + '
      curr = curr.next

    return s

def main():
  # read data from file poly.in from stdin
  num = int(sys.stdin.readline().strip())

  # create polynomial p
  p = LinkedList()
  for i in range(num):
    line = sys.stdin.readline().strip()
    coeff, exp = line.split()
    p.insert_in_order(int(coeff), int(exp))

  line = sys.stdin.readline()

  
  # create polynomial q
  num = int(sys.stdin.readline().strip())

  q = LinkedList()
  for i in range(num):
    line = sys.stdin.readline().strip()
    coeff, exp = line.split()
    q.insert_in_order(int(coeff), int(exp))

  # get sum of p and q and print sum
  total = p.add(q)
  print(total)
  
  # get product of p and q and print product
  prod = p.mult(q)
  print(prod)

if __name__ == "__main__":
  main(