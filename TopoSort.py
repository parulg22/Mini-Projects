#  File: TopoSort.py

#  Description: takes a graph and sorts it in order by its pointers 

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    # label is an identifier
    # concept of weight to vertex (ex: if population or GDP mattered, that would be the piece of data in the class)
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str(self.label)


class Graph (object):
  def __init__ (self):
    # list of vertex objects 
    self.Vertices = []
    # edgdes represented by adjacency matrix 
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (not self.has_vertex(label)):
        self.Vertices.append(Vertex(label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()
    s = set()
    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    s.add(self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        s.add(self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    return s

  # do the breadth first search in a graph
  def bfs (self, v):
    theQueue = Queue()
    # select starting vertex and make current 
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    u = self.get_adj_unvisited_vertex(v)
    if u != -1:
        curr = v
        self.Vertices[u].visited = True
        theQueue.enqueue(u)
        print(self.Vertices[u])
    else:
        return 
    # while queue is not empty or selected vertex has unvisited neighbors 
    while not theQueue.is_empty() or self.get_adj_unvisited_vertex(curr) != -1:
        u = self.get_adj_unvisited_vertex(curr)
        if u == -1:
            curr = theQueue.dequeue()
        else: 
            (self.Vertices[u]).visited = True
            print (self.Vertices[u])
            theQueue.enqueue (u)
    # reset all flags to False 
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    for i in range(len(self.Vertices)):
        if self.Vertices[i].get_label() == fromVertexLabel:
            row = i 
            break
    for i in range(len(self.Vertices)):
        if self.Vertices[i].get_label() == toVertexLabel:
            col = i 
            break
    self.adjMat[row][col] = 0
    self.adjMat[col][row] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    # find index at which label is and remove index from vertices list 
    idx = -1
    for i in range(len(self.Vertices)):
        if self.Vertices[i].get_label() == vertexLabel:
            idx = i 
            self.Vertices.pop(i)
            break
    # delete edges from/to it in adjacency matrix
    # remove col in matrix 
    if idx != -1:
        self.adjMat.pop(idx)
        for i in range(len(self.adjMat)):
            self.adjMat[i].pop(idx)

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
    return len(self.dfs(0)) == len(self.Vertices)

  # get the vert with in degree of 0
  # return list of their labels
  def get_no_in(self, remaining_vert):
    lst = []
    no_incoming = True
    for i in range(len(self.adjMat)):
      for j in range(len(self.adjMat)):
        if(self.adjMat[j][i] > 0):
          no_incoming = False
          break
      # if we haven't already checked the vertex and it has no incoming
      if(no_incoming and self.Vertices[i] in remaining_vert):
        lst.append(self.Vertices[i].get_label())
      no_incoming = True
    return lst
        
  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort (self):
    remaining_vert = self.Vertices[:]
    topo_lst = []
    # while there are still verticies to check
    while(len(remaining_vert) != 0):
      no_in = self.get_no_in(remaining_vert)
      if(len(no_in) == 0):
        break
      no_in.sort()
      topo_lst.extend(no_in)
      for i in range(len(no_in)):
        idx = self.get_index(no_in[i])
        for x in range(len(remaining_vert)):
          if(remaining_vert[x].get_label() == no_in[i]):
            remaining_vert.pop(x)
            break
        # make all the in degrees for the new verticies 0
        for j in range (len(self.adjMat[idx])):
          self.adjMat[idx][j] = 0
    return topo_lst

def main():
  # create a Graph object
  theGraph = Graph()
  line = sys.stdin.readline().strip()
  num_vert = int(line)
  for i in range(num_vert):
    line = sys.stdin.readline().strip()
    theGraph.add_vertex(line)
  
  num_edges = int(sys.stdin.readline().strip())
  theGraph.adjMat = [[0 for x in range(num_vert)] for y in range(num_vert)]
  for i in range(num_edges):
    from_v, to_v = sys.stdin.readline().strip().split()
    theGraph.add_directed_edge(theGraph.get_index(from_v), theGraph.get_index(to_v))

  # test if a directed graph has a cycle
  if (theGraph.has_cycle()):
    print ("The Graph has a cycle.")
  else:
    print ("The Graph does not have a cycle.")

  # test topological sort
  if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print ("\nList of vertices after toposort")
    print (vertex_list)

main()