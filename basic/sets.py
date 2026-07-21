

setA = set(["a", "b", "c", "d"])
setB = set(["c", "d", "e", "f"])
setC = {"x", "y", "z"}
empty_set = set() # not {}, this is a dict 

print("e" in setA) # efficient membership check

print(setA - setB) # Set difference: elements that in setA but not in setB
print(setA | setB) # Set union: elements that are in setA or in setB 
print(setA & setB) # Set intersection: elements that are in both sets
print(setA ^ setB) # Symmetric difference: union - intersection 

l1 = [1,1,2,23,4,4,3,2,1,2,23,32,42,32,32,4,4,4,4,4,4]

l1_no_dup = list(set(l1))
print(l1_no_dup)


for elem in setC:
    print(elem)

# setA[0] = 2 
# TypeError



