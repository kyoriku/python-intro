# This script demonstrates basic user input in Python.

name = input("What's your name? ")  # Prompt user for their name
print(f"Hello {name}")  # Greet the user

num1 = input("Enter a number: ")  # Prompt user for the first number
num2 = input("Enter another number: ")  # Prompt user for the second number
print(f"{num1} + {num2} = {int(num1)+int(num2)}")  # Calculate and display the sum

# Write some code that outputs your name to the screen
name = "Austin"  # Assign the name "Austin" to the variable
print(f"Hello {name}")  # Print the name

# Write some code that outputs your name to the screen 10 times using math
name = "Austin"  # Assign the name "Austin" to the variable
print(name * 10)  # Print the name 10 times

# Write some code that asks how many Apples you'd like to purchase and then outputs the response
apples = input("How many apples would you like to purchase? ")  # Prompt user for the number of apples
print(f"You would like to purchase {apples} apples.")  # Display the number of apples

# Write some code that asks for a person's first name on one line, then after they type it in, asks for their last name. Then tells them "Hello first last name"
first_name = input("What is your first name? ")  # Prompt user for their first name
last_name = input("What is your last name? ")  # Prompt user for their last name
print(f"Hello {first_name} {last_name}")  # Greet the user with their full name

# Write some code that asks (one line at a time) what your name is, where you live, what your phone number is, and what your Favourite colour is; then outputs all that info to the screen one item per line.
name = input("What is your name? ")  # Prompt user for their name
location = input("Where do you live? ")  # Prompt user for their location
phone_number = input("What is your phone number? ")  # Prompt user for their phone number
Favourite_colour = input("What is your Favourite colour? ")  # Prompt user for their Favourite colour
print(f"Name: {name}\nLocation: {location}\nPhone Number: {phone_number}\nFavourite colour: {Favourite_colour}")  # Display all the collected information
