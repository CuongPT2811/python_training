"""Tuple operations practice assignment"""

#1. Create a tuple
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "apple", "cherry")
print(f"Original tuple: {my_tuple}")

#2. Count tuple's element
print(f"Count tuple's element: {len(my_tuple)}")

#3. Get the first, second, last element
print(f"Tuple's first element: {my_tuple[0]}")
print(f"Tuple's second element: {my_tuple[1]}")
print(f"Tuple's last element: {my_tuple[-1]}")

#4. Print the list from first to before kiwi
kiwi_index = my_tuple.index('kiwi')
print(f"Tuple elements from first to before kiwi: {my_tuple[:kiwi_index]}")

#5. Change 'kiwi' to 'grape'
temp_list = list(my_tuple)
temp_list[temp_list.index('kiwi')] = 'grape'
my_tuple = tuple(temp_list)
print(f"Tuple after change 'kiwi' to 'grape': {my_tuple}")

#6. Add kumquat to tuple
temp_list = list(my_tuple)
temp_list.append("kumquat")
my_tuple = tuple(temp_list)
print(f"Tuple after adding 'kumquat': {my_tuple}")

#7. Remove mango from tuple
temp_list = list(my_tuple)
temp_list.remove("mango")
my_tuple = tuple(temp_list)
print(f"Tuple after removing 'mango': {my_tuple}")