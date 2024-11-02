def wisdom():
  print("You have to know when to hold em")

wisdom()

def fizz_buzz(x):
  if x % 3 == 0 and x % 5 == 0:
    print(f"{x} FIZZ BUZZ!")
  elif x % 3 == 0:
    print(f"{x} FIZZ")
  elif x % 5 == 0:
    print(f"{x} BUZZ")
  else:
    print(f"{x} is boring")
  
fizz_buzz(97)

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
  
print(is_even(99))

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
  
my_variable = is_even(99)
print(my_variable)

def namer(first, last):
  print(f"Hello, {first} {last}, nice to meet you!")

namer("John", "Doe")

def namer(first = "John", last = "Doe"):
  print(f"First name: {first}")
  print(f"Last name: {last}")

namer()

def fizz_buzz():
  x = int(input("Enter a number: "))
  if x % 3 == 0 and x % 5 == 0:
    print(f"{x} FIZZ BUZZ!")
  elif x % 3 == 0:
    print(f"{x} FIZZ")
  elif x % 5 == 0:
    print(f"{x} BUZZ")
  else:
    print(f"{x} is boring")

fizz_buzz()

def seven_things(a, b, c, d, e, f, g):
  print(a, b, c, d, e, f, g)

seven_things(1, 2, 3, 4, 5, 6, 7)

def welcome():
  name = input("What is your name? ")
  print(f"Hello, {name}, welcome!")

welcome()
