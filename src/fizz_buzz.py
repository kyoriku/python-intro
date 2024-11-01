# Print out every number between 1 and 100, one number per line, but if the number is divisible by three, print out ʺFIZZʺ; if the number is divisible by five, print out ʺBUZZʺ; and if the number is divisible by both three AND five, print out FIZZ BUZZ.
for x in range(1, 101):
  if x % 3 == 0 and x % 5 == 0:
    print(f"{x} FIZZ BUZZ!")
  elif x % 3 == 0:
    print(f"{x} FIZZ")
  elif x % 5 == 0:
    print(f"{x} BUZZ")
  else:
    print(x)

# 1. Try FIZZ/BUZZ again but do it in less lines of code!
for x in ['FIZZ BUZZ' if x % 15 == 0 else 'FIZZ' if x % 3 == 0 else 'BUZZ' if x % 5 == 0 else x for x in range(1, 101)]:
  print(x)

# 2. Create a multi‐dimensional List with 4 items, and each item is itself a List containing a personʹs name, their address, and phone number (make up the info). Loop through the List and output just each personʹs phone number.
names = [
  ["John", "123 Main St", "555-1234"], 
  ["Tim", "456 Elm St", "555-5678"], 
  ["Mary", "789 Oak St", "555-9012"], 
  ["Beatrice", "101 Pine St", "555-3456"]
  ]  # List with nested lists
for name in names:  # Loop through each nested list
  print(name[2])  # Print the phone number of each person

# 3. Loop through the List from exercise 2 and print out the full information of even items in the List (ie the 2nd and 4th List in your multidimensional List).
for x in range(len(names)):  # Loop through the indexes of the list
  if x % 2 == 1:  # If the index is odd
    print(names[x])  # Print the list
