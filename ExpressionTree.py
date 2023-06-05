#  File: ExpressionTree.py

#  Description: Takes an expression and uses binary trees to evaluate it and write in PN and RPN

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

# takes string operands and operator and performs appropriate calculation 
def operate(oper1, oper2, token):
        expr = str(oper1) + token + str(oper2)
        return eval(expr)

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = Node()

    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        expr = expr.split()
        # read through each element in the string 
        s = Stack()
        curr = self.root 
        for item in expr: 
            # keep going if item is a space 
            if item == "(":
                # create left child 
                # push onto stack
                # assign current node to the newly created left child 
                curr.lChild = Node()
                s.push(curr)
                curr = curr.lChild
            elif item in operators: 
                # create right child
                # push onto stack
                # assign current node to newly created right child 
                curr.data = item
                curr.rChild = Node()
                s.push(curr)
                curr = curr.rChild
            elif item == ")":
                curr = s.pop()
            else: 
                if item.isdigit():
                    curr.data = int(item)
                    curr = s.pop()
                else:
                    curr.data = float(item)
                    curr = s.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # base case: two operands
        if aNode.lChild.data not in operators and aNode.rChild.data not in operators:
            return float(operate(aNode.lChild.data, aNode.rChild.data, aNode.data))
        # both of the children are operators
        elif aNode.lChild.data in operators and aNode.rChild.data in operators: 
            return operate(self.evaluate(aNode.lChild), self.evaluate(aNode.rChild), aNode.data)
        # one of the children is an operator
        elif aNode.lChild.data in operators:
            return operate(self.evaluate(aNode.lChild), aNode.rChild.data, aNode.data)
        elif aNode.rChild.data in operators:
            return operate(aNode.lChild.data, self.evaluate(aNode.rChild), aNode.data)
            
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        lst = []
        self.pre_helper(aNode, lst)
        return " ".join(lst)

    def pre_helper(self, aNode, lst):
        lst.append(str(aNode.data))
        if aNode.lChild != None: 
            self.pre_helper(aNode.lChild, lst)
        if aNode.rChild != None:
            self.pre_helper(aNode.rChild, lst)

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        lst = []
        self.post_helper(aNode, lst)
        return " ".join(lst)

    def post_helper(self, aNode, lst = []):
        if aNode.lChild != None: 
            self.post_helper(aNode.lChild, lst)
        if aNode.rChild != None:
            self.post_helper(aNode.rChild, lst)
        lst.append(str(aNode.data))

    
# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()