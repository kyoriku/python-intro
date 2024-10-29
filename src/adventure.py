# This script demonstrates a simple text-based adventure game in Python.

from os import system  # Import the system function from the os module

system("clear")  # Clear the console
print("Welcome to Choose Your Own Adventure!")  # Greet the player
print("The goal is to find the Python Princess...")  # Explain the goal

name = input("Enter your name: ")  # Ask the player for their name

name = name.lower()  # Convert the name to lowercase
system("clear")  # Clear the console
print("You're standing in front of two doors...")  # Present the first choice
print("Do you want the door on the left or right?")  # Ask for the player's choice

question = input().lower()  # Get the player's choice and convert it to lowercase
if question == "left":  # If the player chooses the left door
  system("clear")  # Clear the console
  print("You fell into a pit and died! GAME OVER")  # Inform the player they lost
elif question == "right":  # If the player chooses the right door
  system("clear")  # Clear the console
  print(f"Contratulations {name.capitalize()} you found")  # Congratulate the player
  print("the Python Princess! YOU WIN!")  # Inform the player they won
else:  # If the player's choice is not recognized
  system("clear")  # Clear the console
  print("Sorry, I don't recongize your response GAME OVER")  # Inform the player they lost
  