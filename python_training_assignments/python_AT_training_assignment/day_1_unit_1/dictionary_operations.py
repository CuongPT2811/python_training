"""Dictionary operations assignment"""

#1. Create a dictionary.
my_dict = {
    "brand": "Ford",
    "model": "Bronco Sport",
    "year": 2022
}
print(f"Original dictionary: {my_dict}")

#2. Get the list of keys
keys_list = my_dict.keys()
print(f"List of keys: {list(keys_list)}")

#3. Add a new item: color: black
my_dict["color"] = "black"
print(f"Dictionary sau khi thêm màu sắc: {my_dict}")

#4. Update 'color' to 'red'
my_dict["color"] = "red"
#Another method: my_dict.update({"color": "red"})
print(f"Dictionary after updating color: {my_dict}")

#5. Remove item with key 'year'. Print the dictionary
del my_dict["year"]
#Another method: my_dict.pop("year")
print(f"Dictionary after removing 'year': {my_dict}")