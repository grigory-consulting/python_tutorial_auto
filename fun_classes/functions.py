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

#help(randomdigit)


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


# Higher-order functions 

def add_five(x):
    return x + 5 

def do_twice(func, arg): # function is given by the parameter 
    return func(func(arg)) # apply given function twice 

print(do_twice(add_five, 3))

# Closure (return value is a function, factory function)


def multiplier(factor):
    def multiply(number):
        return number*factor
    return multiply # return function 

double = multiplier(2)
print(double(14))

# Following function was generated be multiplier(2)
# def double(number):
#     return number*2

triple = multiplier(3)
print(triple(4))


# Anomymous function (lambda)

square = lambda x: x*x # function without name = name is optional 
print(square(5))

mul = lambda x,y:x*y # multiple parameters

double_x = lambda x: (x,x) # multiple return values 

# usually you need only list comprehension 

nums = [1,2,3,4,5,6]
res = list(map(lambda x: x+x, nums)) # map ... apply a function to each element of the list 

print(res)

# TODO represent list(map(lambda x: x+x, nums)) as a list comprehension 

res = [x+x for x in nums] 
print(res)

nums = [1,2,3,4,5,6]
nums2 = [10,20,30,40,50,60]
res = list(map(lambda x,y: x+y, nums, nums2)) 
print(res)

# filter ... filter the list according to some condition 

evens = list(filter(lambda x : x%2 == 0, nums))
print(evens)

# List comprehension 

evens = [x for x in nums if x%2==0]
print(evens)

from functools import reduce 

prod = reduce(lambda x,y: x*y, nums)
print(prod) # 1*2*3*4*5*6