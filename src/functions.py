def wisdom():  # Define a function named wisdom
  print("You have to know when to hold em")  # Print a quote

wisdom()  # Call the wisdom function

def fizz_buzz(x):  # Define a function named fizz_buzz that takes one argument x
  if x % 3 == 0 and x % 5 == 0:  # Check if x is divisible by both 3 and 5
    print(f"{x} FIZZ BUZZ!")  # Print FIZZ BUZZ if true
  elif x % 3 == 0:  # Check if x is divisible by 3
    print(f"{x} FIZZ")  # Print FIZZ if true
  elif x % 5 == 0:  # Check if x is divisible by 5
    print(f"{x} BUZZ")  # Print BUZZ if true
  else:
    print(f"{x} is boring")  # Print is boring if none of the above conditions are met
  
fizz_buzz(97)  # Call the fizz_buzz function with 97

def is_even(x):  # Define a function named is_even that takes one argument x
  if x % 2 == 0:  # Check if x is even
    return True  # Return True if x is even
  else:
    return False  # Return False if x is odd
  
print(is_even(99))  # Print the result of is_even function with 99

def is_even(x):  # Define a function named is_even that takes one argument x
  if x % 2 == 0:  # Check if x is even
    return True  # Return True if x is even
  else:
    return False  # Return False if x is odd
  
my_variable = is_even(99)  # Assign the result of is_even function with 99 to my_variable
print(my_variable)  # Print my_variable

def namer(first, last):  # Define a function named namer that takes two arguments first and last
  print(f"Hello, {first} {last}, nice to meet you!")  # Print a greeting message

namer("John", "Doe")  # Call the namer function with "John" and "Doe"

def namer(first = "John", last = "Doe"):  # Define a function named namer with default arguments
  print(f"First name: {first}")  # Print the first name
  print(f"Last name: {last}")  # Print the last name

namer()  # Call the namer function with default arguments

# 1. Re‐write the fizz_buzz function to prompt a user to enter a number and then return the function result.
def fizz_buzz():  # Define a function named fizz_buzz
  x = int(input("Enter a number: "))  # Prompt the user to enter a number and convert it to an integer
  if x % 3 == 0 and x % 5 == 0:  # Check if x is divisible by both 3 and 5
    print(f"{x} FIZZ BUZZ!")  # Print FIZZ BUZZ if true
  elif x % 3 == 0:  # Check if x is divisible by 3
    print(f"{x} FIZZ")  # Print FIZZ if true
  elif x % 5 == 0:  # Check if x is divisible by 5
    print(f"{x} BUZZ")  # Print BUZZ if true
  else:
    print(f"{x} is boring")  # Print is boring if none of the above conditions are met

fizz_buzz()  # Call the fizz_buzz function

# 2. Write some code using the same fizz_buzz function but have it print out all numbers between 1 and 100 by calling the function 100 times.
# for x in range(1, 101):  # Loop through numbers 1 to 100
#   fizz_buzz()  # Call the fizz_buzz function

# 3. Create a function that has 7 things passed to it.
def seven_things(a, b, c, d, e, f, g):  # Define a function named seven_things that takes seven arguments
  print(a, b, c, d, e, f, g)  # Print all seven arguments

seven_things(1, 2, 3, 4, 5, 6, 7)  # Call the seven_things function with seven arguments

# 4. Create a function that asks a persons name, allows them to enter the name, and then prints out a welcome message with that name.
def welcome():  # Define a function named welcome
  name = input("What is your name? ")  # Prompt the user to enter their name
  print(f"Hello, {name}, welcome!")  # Print a welcome message with the entered name

welcome()  # Call the welcome function
