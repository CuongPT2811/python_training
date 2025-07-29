my_list = [1, 2, 3, 4, 5, 6]

#print even numbers in new list

#basic for loop
"""
even_num = []
for num in my_list:
    if num % 2 == 0:
        even_num.append(num) #Append: add to the end of the list
"""

#List comprehension
even_num = [num for num in my_list if num % 2 == 0]
#even_num = list(filter(lambda num: num % 2 == 0, my_list)) : Using filter and lambda function

#Dictionary comprehension
even_num_2= {f'Number{number}': number for number in my_list if number % 2 != 0}




print("Even numbers:", even_num)
print("Odd numbers:", even_num_2)