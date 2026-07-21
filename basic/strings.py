

print("Hello, World!")

my_string1 = "hello"
my_string2 = "WorlD"

print(my_string1 + "_" + my_string2) # String concatenation 

print(len(my_string1)) # Length of the string (integer) = Number of characters 

# Accessing

print(my_string1[0]) # first element 
print(my_string1[1]) # second element 

# Negative accessing 
print(my_string1[-1]) # last element
print(my_string1[-2]) # before last element

string1 = "Honey Bee"


print(string1.startswith("ho")) # False 

# string normalization 
print(string1.lower())
print(string1.upper())

print(string1.lower().startswith("ho")) # True  

# Parsing 

my_string_type1 = "6"
my_string_type2 = "7"


print(my_string_type1 + my_string_type2) # 67 

print(int(my_string_type1) + int(my_string_type2)) # 13


my_float1 = 6. # 6.0 
my_float2 = 7.2 # 7.2
my_float3 = .8 # 0.8 
my_float4 = 1e-7 # scientific notation 


print(float(my_string_type1) + float(my_string_type2)) # 13.0 

print(0.1 + 0.2)


name = "" # empty is False in if-statement
if name:
    print("Name is not empty")
if len(name) > 3:
    print("Name is longer than 3 characters")




total = 0
count = 0
print("0 to stop")
num = int(input("Enter a number: "))
while num != 0:
    total += num
    count += 1
    print("0 to stop")
    num = int(input("Enter a number: "))
print("Count:", count)
print("Sum:", total)


