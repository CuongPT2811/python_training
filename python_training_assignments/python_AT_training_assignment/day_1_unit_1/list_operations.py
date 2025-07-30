"""List operations practice assignment"""

#1. Create a list with 10 integer elements
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {my_list}")

#2. Print total number in list
print(f"Total numbers in list: {len(my_list)}")

#3. Print first, second, last element
print(f"First element: {my_list[0]}")
print(f"Second element: {my_list[1]}")
print(f"Last element: {my_list[-1]}")

#4. Print from the second to the rest of the list
print(f"From second to the rest of the list: {my_list[1:]}") #my_list[i:] return from index i element to the rest

#5. Change the element at index 2 (3rd element) to 10
my_list[2] = 10
print(f"The list after changing 3rd element to 10:  {my_list}")

#6. Change the element from 6th to 8th to -5, -6, -7
my_list[5:8] = [-5, -6, -7]
print(f"The list after change element from 6th to 8th to -5, -6, -7:  {my_list}")

#7. Insert new element at index 4 (in this case, 99) and at the end of the list (100)
my_list.insert(4, 99)
my_list.append(100)
print(f"The list after insert at index 4 and at the end: {my_list} ")

#8. Remove element has -6 value, remove element at index 4 (99)
my_list.remove(-6)
del my_list[4]
print(f"After remove elements: {my_list}")

#9. Sort by decreasing order
my_list.sort(reverse=True)
print(f"List after sort in descending order: {my_list}")
