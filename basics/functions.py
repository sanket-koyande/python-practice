#functions.py
#Basic Python functions for practice

#1. Function to add two numbers
def add_numbers(a, b):
  return a + b

#2. Function to check even or odd
def check_even_odd(num):
  if num % 2 == 0:
    return "Even"
  else:
    return "Odd"

#3. Funtion to find square of a number
def square(num):
  return num * num

#4. Function to calculate factorial
def factorial(n):
  fact = 1
  for i in range(1, n+1):
    fact *= i
    return fact

#5. Function to calculate average of a list
def calculate_average(numbers):
  total = sum(numbers)

#Testing the functions
print("Addition:", add_numbers(5, 3))
print("Even or Odd:", check_even_odd(7))
print("Square:", square(4))
print("Factorial:", factorial(5))
print("Average:", calculate_average([10, 20, 30, 40]))

  return total / len(numbers)
