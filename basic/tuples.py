

x = (1,2,3) # tuple 
# x[0] = 10 



# shallow immutability 

l = ["a", "b", "c"]


x = (l,) 

print(x)

# issue: lists are mutable 

l[0] = "D"
print(x) 