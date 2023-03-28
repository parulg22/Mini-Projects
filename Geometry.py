#  Description: defines characteristics of 3D shapes and how they interact 

import math
import sys 

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '(' + str(float(self.x)) + ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + ')'
    
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.hypot(self.x - other.x, self.y-other.y, self.z-other.z)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
        tol = 1.0e-6
        return ((abs(self.x-other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z-other.z) < tol))


class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0, radius = 1.0):
    self.center = Point(float(x),float(y),float(z))
    self.radius = float(radius) 
    
  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return "Center: (" + str(float(self.center.x)) + ", " + str(float(self.center.y)) + ", " + str(float(self.center.z)) + "), Radius: " + str(float(self.radius))

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return (4 * math.pi * self.radius**2)

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return ((4/3) * math.pi * self.radius**3)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
        #if distance of point from center is less than radius 
        return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    dist_centers = self.center.distance(other.center) 
    return (dist_centers + other.radius) < self.radius

  # determine if another Sphere is strictly outside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_outside_sphere (self, other):
    dist_centers = self.center.distance(other.center) 
    return (dist_centers > self.radius + other.radius)

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube): #cube_inside_sphere 
    return (self.is_inside_point(a_cube.point1) and self.is_inside_point(a_cube.point2) and 
            self.is_inside_point(a_cube.point3) and self.is_inside_point(a_cube.point4) and
            self.is_inside_point(a_cube.point5) and self.is_inside_point(a_cube.point6) and
            self.is_inside_point(a_cube.point7) and self.is_inside_point(a_cube.point8))

  # determine if a Cube is strictly outside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_outside_cube (self, a_cube): 
    return ((not (self.is_inside_point(a_cube.point1))) and
            (not (self.is_inside_point(a_cube.point2))) and 
            (not (self.is_inside_point(a_cube.point3))) and 
            (not (self.is_inside_point(a_cube.point4))) and
            (not (self.is_inside_point(a_cube.point5))) and 
            (not (self.is_inside_point(a_cube.point6))) and
            (not (self.is_inside_point(a_cube.point7))) and 
            (not (self.is_inside_point(a_cube.point8))))

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    return (not (self.is_inside_sphere(other) or (self.is_outside_sphere(other)) or other.is_inside_sphere(self) or other.is_outside_sphere(self)))
   
  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    return (not (self.is_inside_cube(a_cube) or  self.is_outside_cube(a_cube)))

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    largest_side = (2 * self.radius) / (math.sqrt(3))
    x = self.center.x
    y = self.center.y
    z = self.center.z
    cube = Cube(x, y, z, largest_side)
    return (cube)


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0, side = 1.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.center = Point(self.x, self.y, self.z)
    self.side = float(side) 
    self.points_cube()

  # gather all vertices of a cube object using point object 
  def points_cube (self):
    self.point1 = Point(self.x + (self.side/2), self.y + (self.side)/2, self.z - (self.side/2))
    self.point2 = Point(self.x + (self.side/2), self.y + (self.side)/2, self.z - (self.side/2))
    self.point3 = Point(self.x + (self.side/2), self.y - (self.side)/2, self.z - (self.side/2))
    self.point4 = Point(self.x + (self.side/2), self.y - (self.side)/2, self.z - (self.side/2))
    self.point5 = Point(self.x - (self.side/2), self.y + (self.side)/2, self.z + (self.side/2))
    self.point6 = Point(self.x - (self.side/2), self.y + (self.side)/2, self.z - (self.side/2))
    self.point7 = Point(self.x - (self.side/2), self.y - (self.side)/2, self.z + (self.side/2))
    self.point8 = Point(self.x - (self.side/2), self.y - (self.side)/2, self.z - (self.side/2))

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return ("Center: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), Side: " + str(self.side))

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return (6 * self.side**2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return (self.side**3)

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    # get min and max x values for the cube 
    max_x = max(self.point1.x, self.point2.x, self.point3.x, self.point4.x, self.point5.x, self.point6.x, self.point7.x, self.point8.x) 
    min_x = min(self.point1.x, self.point2.x, self.point3.x, self.point4.x, self.point5.x, self.point6.x, self.point7.x, self.point8.x)
    # get min and max y values for the cube 
    max_y = max(self.point1.y, self.point2.y, self.point3.y, self.point4.y, self.point5.y, self.point6.y, self.point7.y, self.point8.y) 
    min_y = min(self.point1.y, self.point2.y, self.point3.y, self.point4.y, self.point5.y, self.point6.y, self.point7.y, self.point8.y)
    # get min and max z values for the cube 
    max_z = max(self.point1.z, self.point2.z, self.point3.z, self.point4.z, self.point5.z, self.point6.z, self.point7.z, self.point8.z) 
    min_z = min(self.point1.z, self.point2.z, self.point3.z, self.point4.z, self.point5.z, self.point6.z, self.point7.z, self.point8.z) 
    # ensure point is between all of the x y and z values 
    return (min_x < p.x < max_x) and (min_y < p.y < max_y) and (min_z < p.z < max_z)

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    # (distance between center plus radius) less than half the side of the cube 
    cube_center = Point(self.x, self.y, self.z)
    return (cube_center.distance(a_sphere.center) + a_sphere.radius) < (self.side)/2

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    return(self.is_inside_point(other.point1) and 
           self.is_inside_point(other.point2) and 
           self.is_inside_point(other.point3) and 
           self.is_inside_point(other.point4) and 
           self.is_inside_point(other.point5) and 
           self.is_inside_point(other.point6) and 
           self.is_inside_point(other.point7) and 
           self.is_inside_point(other.point8))

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    center = Point(other.x, other.y, other.z)
    return (not (self.is_inside_cube(other))) and ((self.is_inside_point(other.point1) or
         self.is_inside_point(other.point2) or 
         self.is_inside_point(other.point3) or 
         self.is_inside_point(other.point4) or 
         self.is_inside_point(other.point5) or 
         self.is_inside_point(other.point6) or 
         self.is_inside_point(other.point7) or 
         self.is_inside_point(other.point8) or 
         self.is_inside_point(center)) or 
         (other.is_inside_point(self.point1) or 
         other.is_inside_point(self.point2) or 
         other.is_inside_point(self.point3) or 
         other.is_inside_point(self.point4) or 
         other.is_inside_point(self.point5) or 
         other.is_inside_point(self.point6) or 
         other.is_inside_point(self.point7) or 
         other.is_inside_point(self.point8)))

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    # call intersection function from above, if no intersection, return 0
    # else add half the side to self object xyz and other object xyz
    # subtract new other values from new self values 
    if not self.does_intersect_cube(other):
        return 0
    else:
        x = abs((self.x + self.side/2) - (other.x + self.side/2))
        y = abs((self.y + self.side/2) - (other.y + self.side/2))
        z = abs((self.z + self.side/2) - (other.z + self.side/2))
        return(x*y*z)

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    # pass center of cube and half of the side 
    return Sphere(self.x, self.y, self.z, self.side/2)


class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0, radius = 1.0, height = 1.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.center = Point(x,y,z)
    self.radius = float(radius)
    self.height = float(height) 
  
  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return "Center: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), Radius: " + str(self.radius) + ", Height: " + str(self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return ((2 * math.pi * self.radius**2) + (2 * math.pi * self.radius * self.height))

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return (math.pi * self.radius**2 * self.height)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  # map x and y coordinate against radius, z coordinate against height 
  def is_inside_point (self, p):
    return(math.hypot(self.center.x-p.x, self.center.y-p.y) < self.radius) and (abs(self.center.z-p.z) < self.height/2)

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    # distance between two points plus sphere's radius is less than cylinder's
    # radius and is less than cylinder's height 
    return (((self.center.distance(a_sphere.center) + a_sphere.radius) < self.radius) and
            ((self.center.distance(a_sphere.center) + a_sphere.radius) < self.height))


  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    return (self.is_inside_point(a_cube.point1) and self.is_inside_point(a_cube.point2) and  
            self.is_inside_point(a_cube.point3) and self.is_inside_point(a_cube.point4) and
            self.is_inside_point(a_cube.point5) and self.is_inside_point(a_cube.point6) and
            self.is_inside_point(a_cube.point7) and self.is_inside_point(a_cube.point8))

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    # if center + radius and center + height is less than big cylinder's radius and 
    # big cylinder's height 
    return ((other.x + other.radius) < self.radius and (other.y + other.radius) < self.radius 
    and (other.z + other.radius) < self.radius
    and (other.x + other.height) < self.height and (other.y + other.height) < self.height 
    and (other.z + other.height) < self.height)

def main():
  # read data from standard input
  # read the coordinates of the first Point p
  point_p = sys.stdin.readline().strip()
  point_p = point_p.split(' ')

  # create a Point object 
  p = Point(point_p[0], point_p[1], point_p[2])

  # read the coordinates of the second Point q
  point_q = sys.stdin.readline().strip()
  point_q = point_q.split(' ')

  # create a Point object 
  q = Point((point_q[0]), (point_q[1]), (point_q[2]))

  # read the coordinates of the center and radius of sphereA
  line = sys.stdin.readline().strip()
  line = line.split(' ')

  # create a Sphere object 
  sphereA = Sphere(float(line[0]), float(line[1]), float(line[2]), float(line[3]))

  # read the coordinates of the center and radius of sphereB
  line = sys.stdin.readline().strip()
  line = line.split(' ')

  # create a Sphere object
  sphereB = Sphere(line[0], line[1], line[2], line[3])

  # read the coordinates of the center and side of cubeA
  line = sys.stdin.readline().strip()
  line = line.split(' ')
  
  # create a Cube object 
  cubeA = Cube(line[0], line[1], line[2], line[3])

  # read the coordinates of the center and side of cubeB
  line = sys.stdin.readline().strip()
  line = line.split(' ')

  # create a Cube object 
  cubeB = Cube(line[0], line[1], line[2], line[3])

  # read the coordinates of the center, radius and height of cylA
  line = sys.stdin.readline().strip()
  line = line.split(' ')

  # create a Cylinder object 
  cylA = Cylinder(line[0],line[1], line[2], line[3], line[4])

  # read the coordinates of the center, radius and height of cylB
  line = sys.stdin.readline().strip()
  line = line.split(' ') 

  # create a Cylinder object
  cylB = Cylinder(line[0],line[1], line[2], line[3], line[4])

  # print if the distance of p from the origin is greater
  # than the distance of q from the origin
  origin = Point(0.0,0.0,0.0) 
  if p.distance(origin) > q.distance(origin):
    print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
  else:
    print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

  # print if Point p is inside sphereA
  if sphereA.is_inside_point(p):
    print("Point p is inside sphereA")
  else:
    print("Point p is not inside sphereA")

  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB):
    print("sphereB is inside sphereA")
  else:
    print("sphereB is not inside sphereA")

  # print if cubeA is inside sphereA
  if sphereA.is_inside_cube(cubeA):
    print("cubeA is inside sphereA")
  else:
    print("cubeA is not inside sphereA")

  # print if sphereA intersects with sphereB
  if sphereA.does_intersect_sphere(sphereB):
    print("sphereA does intersect sphereB")
  else:
    print("sphereA does not intersect sphereB")

  # print if cubeB intersects with sphereB
  if sphereB.does_intersect_cube(cubeB):
    print("cubeB does intersect sphereB")
  else:
    print("cubeB does not intersect sphereB")

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  cube = sphereA.circumscribe_cube()
  volume = cube.volume()
  if volume > cylA.volume():
    print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
  else:
    print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

  # print if Point p is inside cubeA
  if cubeA.is_inside_point(p):
    print("Point p is inside cubeA")
  else:
    print("Point p is not inside cubeA")

  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA):
    print("sphereA is inside cubeA")
  else:
    print("sphereA is not inside cubeA")

  # print if cubeB is inside cubeA
  if cubeA.is_inside_cube(cubeB):
    print("cubeB is inside cubeA")
  else:
    print("cubeB is not inside cubeA")

  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB):
    print("cubeA does intersect cubeB")
  else:
    print("cubeA does not intersect cubeB")

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cubeA.intersection_volume(cubeB) > sphereA.volume():
    print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
  else:
    print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  s_object = cubeA.inscribe_sphere()
  if s_object.area() > cylA.area():
    print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
  else:
    print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")
  # print if Point p is inside cylA
  if cylA.is_inside_point(p):
    print("Point p is inside cylA")
  else:
    print("Point p is not inside cylA")

  # print if sphereA is inside cylA
  if cylA.is_inside_sphere(sphereA):
    print("sphereA is inside cylA")
  else:
    print("sphereA is not inside cylA")

  # print if cubeA is inside cylA
  if cylA.is_inside_cube(cubeA):
    print("cubeA is inside cylA")
  else:
    print("cubeA is not inside cylA")

if __name__ == "__main__":
  main()