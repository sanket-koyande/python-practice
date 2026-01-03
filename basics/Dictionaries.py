# Creating a Dictionary 
my_dict = { 
"name": "Alice", 
"age": 25, 
"city": "New York" 
} 
print("Original Dictionary:", my_dict) 
# Dictionary Methods 
# Get the value of a key 
age = my_dict.get("age") 
print("Age:", age) 
# Add a new key-value pair 
my_dict["profession"] = "Engineer" 
print("After adding a new key-value pair:", my_dict) 
# Remove a key-value pair 
my_dict.pop("city") 
print("After removing a key-value pair:", my_dict) 
# Get all keys and values 
keys = my_dict.keys() 
values = my_dict.values() 
print("Keys:", keys) 
print("Values:", values) 
# Operations on Dictionaries 
# Merging two dictionaries 
additional_info = {"hobby": "painting", "age": 26} 
my_dict.update(additional_info)  # Updates with new key-value pairs or modifies existing ones 
print("After merging with additional_info:", my_dict) 
# Clearing all elements in the dictionary 
my_dict.clear() 
print("After clearing the dictionary:", my_dict) 
