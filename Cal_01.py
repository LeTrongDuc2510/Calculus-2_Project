import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#define class point
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        outstr = "Point( " + str(round(self.x,4))+ ", " + str(round(self.y,4))+ ", " + str(round(self.z,4)) + " )"
        return outstr

    def __sub__(self, other):  
        if isinstance(other, Vector):
            return Point(self.x - other.x,
                         self.y - other.y,
                         self.z - other.z)

        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)
    
    def __add__(self, other):  
        if isinstance(other, Vector):
            return Point(self.x + other.x,
                         self.y + other.y,
                         self.z + other.z)

        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def dis(self,other):
        d = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
        return d
#define class vector
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        outstr = "Vector( " + str(round(self.x,4))+ ", " + str(round(self.y,4))+ ", " + str(round(self.z,4)) + " )"
        return outstr
        
    def norm(self):   
        d = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return Vector(self.x / d, self.y / d, self.z / d)

    def __mul__(self, other):
        if isinstance(other, Vector):        
            return (self.x * other.x + self.y * other.y + self.z * other.z)
            
        return Vector(self.x * other, self.y * other, self.z * other)

a = int(14) 
#set data to skecth the graph
x_data = np.linspace(-25, 25, 15)
y_data = np.linspace(-25, 25, 15)
x, y = np.meshgrid(x_data, y_data)
z = ((a - x + 3*y)/2)
# set the limit for the axis
ax = plt.axes(projection="3d")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim([-40, 40])
ax.set_ylim([-40, 40])
ax.set_zlim([-40, 40])
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

#finding the projection point
s = Point(0, 1, 1)

plane = (
    Point(a, 0 ,0),
    Point(0, -a/3, 0),
    Point(0, 0, a/2)
)

n = Vector(1, -3, 2).norm()
s1 = s - plane[0]
re = (n*s1)/(n*n)
d = n*re
pp = s - d
ax.quiver(s.x,s.y,s.z,pp.x,pp.y,pp.z)

#print the ouput
print("The shortest distance from S the point (0, 1, 1) is: " + str(round(s.dis(pp),4)))
print("And the point we need to find is " + str(pp))
plt.show()

