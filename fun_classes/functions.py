import random 


def cube(num): # one parameter
    cube_num = num**3
    return cube_num # one return value 

print([cube(x) for x in range(10)])


def greeting(name="World"): # one parameter with default value 
    print(f"Hello, {name}!") # no return value 

greeting()
greeting("Sriram")

def randomdigit(): #, no parameters 
    """random integer between 0 and 9"""
    return random.randint(0,9) 

print(randomdigit())

help(randomdigit)


def add_three_numbers(a,b,c=1):
    print("a =", a, "b =", b, "c =", c)
    print(a+b+c)



# this is allowed

add_three_numbers(1,2)
add_three_numbers(2,1)
add_three_numbers(1,2,3)
add_three_numbers(c=4,b=2,a=1)
add_three_numbers(1, c=5, b=2)


# add_three_numbers(c=5, b=2, 1) # SyntaxError


#def add_three_numbers(a=1,b,c):
#   print("a =", a, "b =", b, "c =", c)
#    print(a+b+c)

def my_print(*args): # arbitrary number of arguments
    print("(", end="")
    print(*args, sep=" | ", end = "")
    print(")")

my_print(1,2,2,3,5,25,25,4,3,4,325,23,4,235,32,523,4,23,423,5,325,2)



def dictentry(**kwargs):
    print(kwargs)

dictentry(age = 50, name = "Prof. Klug", city="Wuppertal", country="Germany")

def everything(a, b=1, *args, **kwargs):
    print("a", a)
    print("b", b)
    print("args", args)
    print("kwargs", kwargs)

everything(3,70,9,424,235,434,234,532, name="Anna", street="Street", y = [])


# Scope 

count = 0 

def increase():
    global count 
    count += 1 

increase()
print(count)


def outer():
    x = "outer value"
    def inner():
        nonlocal x 
        x = "x was changed"
    inner()
    print(x)

outer()