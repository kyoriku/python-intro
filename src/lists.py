# This script demonstrates basic list operations in Python.

# Creating a list
names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]  # List of names

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]  # List of names
print(names[2])  # Print the third name

# Putting different things into lists
variable_1 = "Tim"  # Assign a name to variable_1
names = ["John", variable_1, "Mary", 41, "Bluto"]  # List with mixed types
print(names[1])  # Print the second item

# Another way to create a list
names = []  # Create an empty list

names = ["John", "April"]  # List with two names
print(len(names))  # Print the length of the list

# Adding things to a list later on
names = ["John", "April"]  # List with two names
names.append("Bob")  # Add "Bob" to the list
print(names)  # Print the updated list

names = ["John", "April"]  # List with two names
names.insert(0, "Bob")  # Insert "Bob" at the beginning
print(names)  # Print the updated list

# Adding multiple items to a list
names = ["John", "April"]  # List with two names
names.extend(["Tim", "Bob"])  # Add multiple names to the list
print(names)  # Print the updated list

# Removing items from a list
names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]  # List of names
names.remove("Bluto")  # Remove "Bluto" from the list
print(names)  # Print the updated list

# Remove a specific index number
names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]  # List of names
names.pop(0)  # Remove the first item
print(names)  # Print the updated list

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]  # List of names
names.pop(1)  # Remove the second item
print(names)  # Print the updated list

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]  # List of names
names.remove("Mary")  # Remove "Mary" from the list
print(names)  # Print the updated list

# Multi-dimensional lists
names = ["John", "Mary", "Beatrice", "Bluto", [1,2,3,4]]  # List with a nested list
print(names)  # Print the list

names = ["John", "Mary", "Beatrice", "Bluto", [1,2,3,4]]  # List with a nested list
print(names[4][2])  # Print the third item of the nested list

numbers = [1,2,3,4]  # List of numbers
names = ["John", "Mary", "Beatrice", "Bluto", numbers]  # List with a nested list
print(names[4][2])  # Print the third item of the nested list

# 1. Create a List with the names of five people you know and output the second name to the screen.
names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]  # List of names
print(names[1])  # Print the second name

# 2. Create a List where the first item in the List is a math problem, like 1 + 1 and the rest of the items are names. Output the first item to the screen. 
math_problem = ["1 + 1", "John", "Tim", "Mary", "Beatrice", "Bluto"]  # List with a math problem and names
print(math_problem[0])  # Print the math problem

# 3. Create a multi‐dimensional List with 4 items, and each item is itself a List containing a personʹs name, their address, and phone number (make up the info). Output the second item in your multidimensional List.
info = [  # Multi-dimensional list with names, addresses, and phone numbers
  ["John", "123 Main St", "555-1234"],  # First person's info
  ["Tim", "456 Elm St", "555-5678"],  # Second person's info
  ["Mary", "789 Oak St", "555-9012"],  # Third person's info
  ["Beatrice", "101 Pine St", "555-3456"]  # Fourth person's info
]
print(info[1])  # Print the second item

# 4. Output just the phone number of the third item in your List from the last question.
print(info[2][2])  # Print the phone number of the third item
