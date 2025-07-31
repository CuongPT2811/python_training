"""Set operations assignment"""

#1. Create a set, then get the number of elements
my_set = {"apple", "banana", "cherry"}
print(f"Original set: {my_set}")
print(f"Number of elements: {len(my_set)}")

#2. Add 'orange' to set
my_set.add("orange")
print(f"Set after adding 'orange': {my_set}")

#3. Add a list of items to set
items_to_add = ["kiwi", "kumquat"]
my_set.update(items_to_add)
print(f"Set after adding a list of items: {my_set}")

#4. Remove 'banana' from set
my_set.remove("banana") #If 'banana' not found => remove() will return Error. discard() will return no error
print(f"Set after removing 'banana': {my_set}")

#5. Create another set {"apple", "banana", "orange"}
another_set = {"apple", "banana", "orange"}
print(f"Set thứ hai: {another_set}")

#Join two sets together
union_set = my_set.union(another_set) #Or use another operator: 

print(f"Set after joining: {union_set}")
print(f"Number of elements in new set: {len(union_set)}")