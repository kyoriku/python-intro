from os import system

system("clear")
print("Welcome to Choose Your Own Adventure!")
print("The goal is to find the Python Princess...")

name = input("Enter your name: ")

name = name.lower()
system("clear")
print("You're standing in front of two doors...")
print("Do you want the door on the left or right?")

question = input().lower()
if question == "left":
  system("clear")
  print("You fell into a pit and died! GAME OVER")
elif question == "right":
  system("clear")
  print(f"Contratulations {name.capitalize()} you found")
  print("the Python Princess! YOU WIN!")
else:
  system("clear")
  print("Sorry, I don't recongize your response GAME OVER")
