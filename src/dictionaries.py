favourite_pizza = {
  "John": "Pepperoni",  # John's favorite pizza
  "Tim": "Mushroom",  # Tim's favorite pizza
  "Mary": "Cheese",  # Mary's favorite pizza
  "Beatrice": "Ham and Onion",  # Beatrice's favorite pizza
  "Bluto": "Supreme"  # Bluto's favorite pizza
}

print(favourite_pizza["John"])  # Print John's favorite pizza

favourite_pizza = {
  "John": "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": "Supreme"
}

favourite_pizza["Bob"] = "Tuna"  # Add Bob's favorite pizza
print(favourite_pizza["Bob"])  # Print Bob's favorite pizza

favourite_pizza = {
  "John": "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": "Supreme"
}

favourite_pizza.pop("Tim")  # Remove Tim from the dictionary
print(favourite_pizza)  # Print the updated dictionary

user_name = "John"

favourite_pizza = {
  user_name: "Pepperoni",  # Use variable for key
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": 41  # Invalid value type for pizza
}

print(favourite_pizza)  # Print the dictionary with invalid value

favourite_pizza = {
  "John": "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": "Supreme"
}

print(favourite_pizza)  # Print the dictionary

favourite_pizza = {
  "John": "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": "Supreme"
}

for x, y in favourite_pizza.items():
  print(f"Key:{x}  Value:{y}")  # Print each key-value pair

favourite_pizza = {
  1: "Pepperoni",  # Numeric key
  2: "Mushroom",
  3: "Cheese",
  4: "Ham and Onion",
  5: "Supreme"
}

print(favourite_pizza)  # Print the dictionary with numeric keys

# 1. Create your own Dictionary, with five of your friends' names and their phone numbers.
friends = {
  "John": 1234567890,  # John's phone number
  "Tim": 2345678901,  # Tim's phone number
  "Mary": 3456789012,  # Mary's phone number
  "Beatrice": 4567890123,  # Beatrice's phone number
  "Bluto": 5678901234  # Bluto's phone number
}

# 2. Create a program using your answer to exercise 1 that prompts a user to enter a name from your list your five friends, and then returns the phone number for that specific friend.
name = input("Enter a name: ")  # Prompt user for a name
print(friends[name])  # Print the phone number for the entered name

# 3. Add a feature to your code from exercise 2 that allows people to add or delete a name from the Dictionary, then return the updated Dictionary to the screen.
action = input("Add or delete a name: ")  # Prompt user for action
if action == "add":
  name = input("Enter a name: ")  # Prompt for name to add
  number = int(input("Enter a number: "))  # Prompt for number to add
  friends[name] = number  # Add name and number to dictionary
elif action == "delete":
  name = input("Enter a name: ")  # Prompt for name to delete
  friends.pop(name)  # Remove name from dictionary

print(friends)  # Print the updated dictionary

# 4. Create a loop that cycles through your Dictionary from exercise 1 and outputs (one per line) "My friend X's phone number is: xxx-xxx-xxxx" replacing the x's with the persons actual name and phone number.
for x, y in friends.items():
  print(f"My friend {x}'s phone number is: {y}")  # Print each friend's name and phone number
