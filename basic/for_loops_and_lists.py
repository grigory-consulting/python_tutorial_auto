
import time 

for i in range(10): 
    print(i, end = " ")

print("\nNext print statement") # \n newline

for var in range(2,6):
    y = var * var
    print(y, end = " ")
print() # print() ... prints newline 

for i in range(10,0,-2):
    print(i, end = " ")
print()

# lists 

l1 = [1,2,3]
print(l1)

l2 = list(range(0,int(10)))
print(l2)

l3 = [1.0, 2, "3"]
print(l3)

l4 = [1., 2, "3", l3]
print(l4)

for each in l4: # sometimes people love to write for each (PHP-like)
    print(each)



numbers = list(range(10)) # [1, 2,..., 10]
#print(numbers)
start = time.time()
squares = [number**2 for number in numbers] # List comprehension
end = time.time()
#print(squares)

print(f"{end-start} seconds")


# equivalent as a for loop

squares2 = []

start = time.time()
for num in numbers:
    squares2.append(num**2)
end = time.time()

print(f"{end-start} seconds")

#print(squares2 == squares)

# cumulatively (not recommended)
# DONE time it

start = time.time()
squares3 = []
for num in numbers:
    squares3 += [num**2] # list concatenation 
end = time.time()

print(f"{end-start} seconds")


#print(squares3 == squares)



food = ["rice", "beans", "bread"]

food.append("broccoli") # appending "broccoli" to the end of the list
food += ["pizza", "hotdog"] # concatenating two lists 

print(food)

# List slices 
print(food[0]) # first element
print(food[-1]) # last element 
print(food[2:]) # from third to last 
print(food[:2]) # upto second 
print(food[2:5]) # from third to fifth 

# very important 
# Mutability

food[0] = "apple juice"
print(food)