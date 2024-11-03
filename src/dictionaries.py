favourite_pizza = {
  "John": "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": "Supreme"
}

print(favourite_pizza["John"])

favourite_pizza = {
  "John": "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": "Supreme"
}

favourite_pizza["Bob"] = "Tuna"
print(favourite_pizza["Bob"])

favourite_pizza = {
  "John": "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": "Supreme"
}

favourite_pizza.pop("Tim")
print(favourite_pizza)

user_name = "John"

favourite_pizza = {
  user_name: "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": 41
}

print(favourite_pizza)

favourite_pizza = {"John": "Pepperoni", "Tim": "Mushroom", 
"Mary": "Cheese", "Beatrice": "Ham and Onion", 
"Bluto": "Supreme"}

print(favourite_pizza)

favourite_pizza = {
  "John": "Pepperoni",
  "Tim": "Mushroom",
  "Mary": "Cheese",
  "Beatrice": "Ham and Onion",
  "Bluto": "Supreme"
}

for x, y in favourite_pizza.items():
  print(f"Key:{x}  Value:{y}")

favourite_pizza = {
  1: "Pepperoni",
  2: "Mushroom",
  3: "Cheese",
  4: "Ham and Onion",
  5: "Supreme"
}

print(favourite_pizza)

friends = {
  "John": 1234567890,
  "Tim": 2345678901,
  "Mary": 3456789012,
  "Beatrice": 4567890123,
  "Bluto": 5678901234
}

name = input("Enter a name: ")
print(friends[name])

action = input("Add or delete a name: ")
if action == "add":
  name = input("Enter a name: ")
  number = int(input("Enter a number: "))
  friends[name] = number
elif action == "delete":
  name = input("Enter a name: ")
  friends.pop(name)

print(friends)

for x, y in friends.items():
  print(f"My friend {x}'s phone number is: {y}")
