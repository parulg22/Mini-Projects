# use Graham's scan algorithm to find coordinates of points that would define the edges of the largest possible convex polygon 
import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  return p.x*q.y + q.x*r.y + r.x*p.y - p.y*q.x - q.y*r.x - r.y*p.x

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  upper_hull = [] 
  # append first two points p_1 and p_2
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  for i in range(2, len(sorted_points)):
    upper_hull.append(sorted_points[i])
    while len(upper_hull) >= 3 and det(upper_hull[-1], upper_hull[-2], upper_hull[-3]) <= 0:
        upper_hull.pop(-2)
  
  lower_hull = []
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])

  for i in range(len(sorted_points) - 2 , -1, -1):
    lower_hull.append(sorted_points[i])
    while len(lower_hull) >= 3 and det(lower_hull[-1], lower_hull[-2], lower_hull[-3]) <= 0:
        lower_hull.pop(-2) 

  # remove duplicates from lower hull that are in upper hull
  lower_hull.pop(0)
  lower_hull.pop(-1)

  # Combine lists
  upper_hull.extend(lower_hull)

  return upper_hull

# get determinant for all points
def area_det(convex_poly):
  # add all of the components that will be added
    add_det = 0
    for i in range(len(convex_poly) - 1):
        add_det += convex_poly[i].x * convex_poly[i+1].y
    add_det += convex_poly[-1].x * convex_poly[0].y
  # add all the components that will be subtracted
    sub_det = 0
    for i in range(len(convex_poly) - 1):
        sub_det += convex_poly[i].y * convex_poly[i+1].x
    sub_det += convex_poly[-1].y * convex_poly[0].x
    return add_det - sub_det

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  poly_det = area_det(convex_poly)
  return abs(poly_det) / 2
  
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  # print the sorted list of Point objects
  """for p in sorted_points:
    print (str(p))"""

  # get the convex hull
  convex_lst = convex_hull(sorted_points)

  # run your test cases
  #print(test_cases())

  # print your results to standard output
  # print the convex hull
  print("Convex Hull")
  for i in range(len(convex_lst)):
    print(convex_lst[i])
  print()

  # get the area of the convex hull
  # print the area of the convex hull
  convex_area = area_poly(convex_lst)
  print(f'Area of Convex Hull = {convex_area}')


if __name__ == "__main__":
  main()
