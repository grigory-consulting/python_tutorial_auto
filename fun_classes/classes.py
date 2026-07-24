


class Point2D:
    """Point in plane."""
    def __init__(self,xx = 0,yy = 0): # Constructor 
        self.x = xx 
        self.y = yy   

    def __str__(self): # return a string for humans
        return f"({self.x}, {self.y})"

    def __repr__(self): # return a string for everything else
        return f"Point2d({self.x},{self.y})"

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy 

    def movex(self,dx):
        self.x += dx

    def movey(self, dy):
        self.y += dy 

    def distance_0(self): # 
        # Euclidean distance 
        return (self.x**2 + self.y**2)**0.5 
    
p = Point2D(3,5) 
print(p)

q = Point2D(2,6)
r = Point2D()
 
lp = [p,q,r, p+q+r]

print(lp)

print(p.distance_0())


# TODO Task 
# Create 50 random points (-10 <= x <= 10, -10 <= y <= 10)
# with integer coordinates.
# Hint: import random, use random.randint(-10,10)
# Determine all points whose Euclidean distance to origin 
# is less then 6.0 
import random

points = [Point2D(random.randint(-10,10), random.randint(-10, 10)) for i in range(50)]

points = []

for i in range(50): 
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    points.append(Point2D(x,y))

print(points)

points_filtered = [point for point in points if point.distance_0() < 6.0 ] # this is better 
print(len(points_filtered))

points_filtered = list(filter(lambda x: x.distance_0() < 6.0, points)) 
print(len(points_filtered))


# Inheritance 

class Point3D(Point2D): # Point3d ... subclass
    # Point2D ... superclass 

    def __init__(self, xx=0, yy=0, zz=0):
        super().__init__(xx, yy) # construction of Point2D
        self.z = zz # extension 

    # TODO 
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __repr__(self):
        return f"Point3D({self.x},{self.y},{self.z})"

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def move(self, dx, dy, dz):
        super().move(dx,dy)
        self.z += dz 

    def distance_0(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5 

    #def distance_0(self): # not recommended
    #    return (super().distance_0()**2 + self.z**2)**0.5 
 
p3d = Point3D(1,2,3)
print(p3d)

lp = [p3d, p3d+p3d, p3d + p3d + p3d]
print(lp)

p3d.move(-3,2,1)
p3d.movex(1) # by inheritance 
p3d.movey(2) 


print(p3d)


# Multiple Inheritance 

class A:
    def methodA(self):
        print("I am method from A")

class B:
    def methodB(self):
        print("I am method from B")

class C(A,B):
    pass 

obj = C()
obj.methodA()
obj.methodB()

class A:
    def method(self):
        print("I am method from A")

class B:
    def method(self):
        print("I am method from B")

class C(A,B):
    pass 

obj = C()
obj.method()
print(C.mro()) # method resolution order 


# diamond problem 

class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")
        super().show()

class C(A):
    def show(self):
        print("C.show()")
        super().show()

class D(B,C):
    def show(self):
        print("D.show()")
        super().show()

d = D()
d.show() 
print(D.mro())