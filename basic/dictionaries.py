


d = {"one": 1, "two": [2], "three": "THREE", 4: "four",  (5,2): "Five" } # keys immutable, values any type

print(d)


# Accessing a key

print(d["three"]) 
#print(d["six"]) # KeyError 
print(d.get("efsfesfsewesf", "key_not_found")) # no error

## Removing elements

del d["one"]
print(d)

value = d.pop("three")

print(value)

for key in d: 
    print(key)  # key
    print(d[key])  # value 

# special methods 

print(list(d.keys())) # list of keys
print(list(d.values())) # list of values
print(list(d.items())) # list of key,value - tuple 
