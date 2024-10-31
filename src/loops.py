# This script demonstrates basic loops in Python.

# While loops
num = 0
while num < 10:  # Loop while num is less than 10
  print(num)  # Print the current value of num
  num += 1  # Increment num by 1

# Break / Continue
num = 0
while num < 10:  # Loop while num is less than 10
  num += 1  # Increment num by 1
  if num == 5:  # If num equals 5
    break  # Exit the loop
  print(num)  # Print the current value of num

num = 0
while num < 10:  # Loop while num is less than 10
  num += 1  # Increment num by 1
  if num == 5:  # If num equals 5
    continue  # Skip the rest of the loop iteration
  print(num)  # Print the current value of num

# For loops
for num in range(6):  # Loop from 0 to 5
  print(num)  # Print the current value of num

for num in range(6):  # Loop from 0 to 5
  print("I LOVE CHEESE!")  # Print "I LOVE CHEESE!"

names = ["John", "Mary", "Tim"] # List of names
for name in names:  # Loop through each name in the list
  print(name)  # Print the current name

name = "John Doe" # String with a name
for x in name:  # Loop through each character in the string
  print(x)  # Print the current character

# Using else with for
for x in range(3):  # Loop from 0 to 2
  print(x)  # Print the current value of x
else:  # When the loop is done
  print("All Done!")  # Print "All Done!"

for x in range(3):  # Loop from 0 to 2
  print(x)  # Print the current value of x
print("All Done!")  # Print "All Done!" after the loop

# Pass statement
for x in range(3):  # Loop from 0 to 2
  pass  # Do nothing
