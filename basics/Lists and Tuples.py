#Lists 
my_list = [1, 2, 3, 4, 5] 
print("Original List:", my_list) 
# List Functions and Methods 
my_list.append(6)  # Adds an element to the list 
print("After append:", my_list) 
my_list.remove(2)  # Removes the first occurrence of an element 
print("After remove:", my_list) 
my_list.reverse()  # Reverses the list 
print("After reverse:", my_list) 
# List Operations 
list1 = [1, 2, 3] 
list2 = [4, 5, 6] 
concatenated_list = list1 + list2  # Concatenation of lists 
print("Concatenated List:", concatenated_list) 
repeated_list = list1 * 3  # Repetition of elements 
print("Repeated List:", repeated_list) 
# Tuples 
my_tuple = (10, 20, 30, 40, 50) 
print("Original Tuple:", my_tuple) 
# Functions in Tuple 
def tuple_sum(t): 
return sum(t) 
def tuple_max(t): 
return max(t) 
print("Sum of tuple:", tuple_sum(my_tuple)) 
print("Max of tuple:", tuple_max(my_tuple)) 
