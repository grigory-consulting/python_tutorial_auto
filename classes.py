class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to_origin(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def __str__(self):
        return f"P({self.x},{self.y})"

p = Point(3, 4)
print(p.distance_to_origin()) 
print(p)