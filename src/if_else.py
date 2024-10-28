x = 41
if x == 41:
  print("x does in fact equal 41!")

x = 41
if x == 42:
  print("x does in fact equal 41!")

x = 41
if x == 41:
  print("x does in fact equal 41!")
else:
  print("x does not equal 41!")

x = 411
if x == 41:
  print("x does in fact equal 41!")
else:
  print("x does not equal 41!")

name = "Austin"
if name == "Austin":
  print("Hi there Austin!")
elif name == "John":
  print("What's up John!")
else:
  print("I dont know who you are!")

name = "John"
if name == "Austin":
  print("Hi there Austin!")
elif name == "John":
  print("What's up John!")
else:
  print("I dont know who you are!")

name = "Bob"
if name == "Austin":
  print("Hi there Austin!")
elif name == "John":
  print("What's up John!")
else:
  print("I dont know who you are!")

name = "Austin"
if name =="Austin" or name =="Bob":
  print("Hi there Austin or Bob!")

name = input("Enter your name: ")
if name == "Austin" or name == "Bob":
  print(f"Hi there {name}!")
else:
  print(f"Hi there stranger!")

name = input("Enter your name: ")
print(f"Hi there {name.lower()}")

name = input("Enter your name: ")
name = name.lower()
print(name)

name = input("Enter your name: ")
print(f"The name {name} has {len(name)} characters.")
