# This script demonstrates basic if-else statements in Python.

# If / else statements
x = 41
if x == 41:  # Check if x equals 41
  print("x does in fact equal 41!")  # Print message if condition is true

x = 41
if x == 42:  # Check if x equals 42
  print("x does in fact equal 41!")  # This will not print because x is not 42

x = 41
if x == 41:  # Check if x equals 41
  print("x does in fact equal 41!")  # Print message if condition is true
else:
  print("x does not equal 41!")  # This will not execute because x is 41

x = 411
if x == 41:  # Check if x equals 41
  print("x does in fact equal 41!")  # This will not print because x is not 41
else:
  print("x does not equal 41!")  # Print message if condition is false

# If / elif
name = "Austin"
if name == "Austin":  # Check if name is Austin
  print("Hi there Austin!")  # Print message if condition is true
elif name == "John":  # Check if name is John
  print("What's up John!")  # This will not execute because name is Austin
else:
  print("I dont know who you are!")  # This will not execute because name is Austin

name = "John"
if name == "Austin":  # Check if name is Austin
  print("Hi there Austin!")  # This will not print because name is John
elif name == "John":  # Check if name is John
  print("What's up John!")  # Print message if condition is true
else:
  print("I dont know who you are!")  # This will not execute because name is John

name = "Bob"
if name == "Austin":  # Check if name is Austin
  print("Hi there Austin!")  # This will not print because name is Bob
elif name == "John":  # Check if name is John
  print("What's up John!")  # This will not print because name is Bob
else:
  print("I dont know who you are!")  # Print message if none of the above conditions are true

# Multiple conditions
name = "Austin"
if name == "Austin" or name == "Bob":  # Check if name is Austin or Bob
  print("Hi there Austin or Bob!")  # Print message if any condition is true

# And / or
name = input("Enter your name: ")  # Prompt user for their name
if name == "Austin" or name == "Bob":  # Check if name is Austin or Bob
  print(f"Hi there {name}!")  # Print personalized message if condition is true
else:
  print(f"Hi there stranger!")  # Print message if condition is false

# String manipulation
'''
lower()         Convert to all lowercase
upper()         Convert to all uppercase
capitalize()    Capitalize just first letter
title()         Capitalizes first letter of each word
swapcase()      Switches capitalized to lowercase & vice versa
len()           Returns character length
rstrip()        Removes trailing spaces
'''

name = input("Enter your name: ")  # Prompt user for their name
print(f"Hi there {name.lower()}")  # Print name in lowercase

name = input("Enter your name: ")  # Prompt user for their name
name = name.lower()  # Convert name to lowercase
print(name)  # Print the lowercase name

name = input("Enter your name: ")  # Prompt user for their name
print(f"The name {name} has {len(name)} characters.")  # Print the length of the name

# 1. Create a simple math flashcard game that asks a user what two numbers added together equal and tell them whether or not they got the answer correct.
num1 = 5  # Set the first number
num2 = 7  # Set the second number
answer = num1 + num2  # Calculate the correct answer
guess = int(input(f"What is {num1} + {num2}? "))  # Prompt user for their guess
if guess == answer:  # Check if the guess is correct
  print("Correct!")  # Print message if the guess is correct  
else:
  print("Incorrect!")  # Print message if the guess is incorrect

# 2. Write some code that asks for a personʹs full name (first and last name) and then output their name with both first and last name capitalized
name = input("Enter your full name: ")  # Prompt user for their full name
name = name.title()  # Capitalize the first letter of each word
print(name)  # Print the capitalized

# 3. Write some code that asks for a personʹs name and then tell that person how many characters are in their name (added them up manually yourself to see if the answer is correct!)
name = input("What's your name? ")  # Prompt user for their name
length_of_name = len(name)  # Calculate the length of the name
print(f"Hello {name}! Your name has {length_of_name} characters.")  # Print the length of the name
