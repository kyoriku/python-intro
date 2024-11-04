import random  # Import the random module for generating random numbers
from os import system  # Import the system function from the os module to clear the console

def start_game():
  system('clear')  # Clear the console
  print('Welcome to Math Flashcards!')  # Print welcome message
  pick = input("Choose your flashcards (add|subtract|multiply|divide): ")  # Prompt user to choose a type of flashcards
  
  if pick.lower() == "add":  # Check if user picked addition
    add_flashcards()  # Call the add_flashcards function
  elif pick.lower() == "subtract":  # Check if user picked subtraction
    subtract_flashcards()  # Call the subtract_flashcards function
  elif pick.lower() == "multiply":  # Check if user picked multiplication
    multiply_flashcards()  # Call the multiply_flashcards function
  elif pick.lower() == "divide":  # Check if user picked division
    divide_flashcards()  # Call the divide_flashcards function
  else:
    print(f"Sorry, I don't recognize {pick}.")  # Print error message for unrecognized input
    input("Please hit enter to try again.")  # Prompt user to hit enter to try again
    start_game()  # Restart the game

def add_flashcards():
  system('clear')  # Clear the console
  card_one = random.randint(0, 10)  # Generate a random number between 0 and 10
  card_two = random.randint(0, 10)  # Generate another random number between 0 and 10
  correct = card_one + card_two  # Calculate the correct answer
  answer = input(f"{card_one} + {card_two}: ")  # Prompt user for their answer

  if int(answer) == correct:  # Check if the user's answer is correct
    print(f"Correct! {card_one} + {card_two} = {answer}")  # Print correct message
  else:
    print(f"Wrong! {card_one} + {card_two} = {correct}")  # Print wrong message
    
  play = input("Would you like another card? (yes|no|restart): ")  # Ask user if they want to play again

  if play.lower() == "yes":  # Check if user wants another card
    add_flashcards()  # Call the add_flashcards function again
  elif play.lower() == "no":  # Check if user wants to stop playing
    print("Thanks for playing!")  # Print thank you message
  elif play.lower() == "restart":  # Check if user wants to restart the game
    start_game()  # Restart the game
  else:
    print(f"Sorry, I don't recognize {play}.")  # Print error message for unrecognized input
    input("Please hit enter to try again.")  # Prompt user to hit enter to try again
    add_flashcards()  # Call the add_flashcards function again

def subtract_flashcards():
  system('clear')  # Clear the console
  card_one = random.randint(0, 10)  # Generate a random number between 0 and 10
  card_two = random.randint(0, 10)  # Generate another random number between 0 and 10
  correct = card_one - card_two  # Calculate the correct answer
  answer = input(f"{card_one} - {card_two}: ")  # Prompt user for their answer

  if int(answer) == correct:  # Check if the user's answer is correct
    print(f"Correct! {card_one} - {card_two} = {answer}")  # Print correct message
  else:
    print(f"Wrong! {card_one} - {card_two} = {correct}")  # Print wrong message

  play = input("Would you like another card? (yes|no|restart): ")  # Ask user if they want to play again

  if play.lower() == "yes":  # Check if user wants another card
    subtract_flashcards()  # Call the subtract_flashcards function again
  elif play.lower() == "no":  # Check if user wants to stop playing
    print("Thanks for playing!")  # Print thank you message
  elif play.lower() == "restart":  # Check if user wants to restart the game
    start_game()  # Restart the game
  else:
    print(f"Sorry, I don't recognize {play}.")  # Print error message for unrecognized input
    input("Please hit enter to try again.")  # Prompt user to hit enter to try again
    subtract_flashcards()  # Call the subtract_flashcards function again

def multiply_flashcards():
  system('clear')  # Clear the console
  card_one = random.randint(0, 10)  # Generate a random number between 0 and 10
  card_two = random.randint(0, 10)  # Generate another random number between 0 and 10
  correct = card_one * card_two  # Calculate the correct answer
  answer = input(f"{card_one} * {card_two}: ")  # Prompt user for their answer

  if int(answer) == correct:  # Check if the user's answer is correct
    print(f"Correct! {card_one} * {card_two} = {answer}")  # Print correct message
  else:
    print(f"Wrong! {card_one} * {card_two} = {correct}")  # Print wrong message

  play = input("Would you like another card? (yes|no|restart): ")  # Ask user if they want to play again

  if play.lower() == "yes":  # Check if user wants another card
    multiply_flashcards()  # Call the multiply_flashcards function again
  elif play.lower() == "no":  # Check if user wants to stop playing
    print("Thanks for playing!")  # Print thank you message
  elif play.lower() == "restart":  # Check if user wants to restart the game
    start_game()  # Restart the game
  else:
    print(f"Sorry, I don't recognize {play}.")  # Print error message for unrecognized input
    input("Please hit enter to try again.")  # Prompt user to hit enter to try again
    multiply_flashcards()  # Call the multiply_flashcards function again

def divide_flashcards():
  system('clear')  # Clear the console
  card_one = random.randint(0, 10)  # Generate a random number between 0 and 10
  card_two = random.randint(1, 10)  # Generate another random number between 1 and 10
  correct = card_one / card_two  # Calculate the correct answer
  answer = input(f"{card_one} / {card_two}: ")  # Prompt user for their answer

  if int(answer) == correct:  # Check if the user's answer is correct
    print(f"Correct! {card_one} / {card_two} = {answer}")  # Print correct message
  else:
    print(f"Wrong! {card_one} / {card_two} = {correct}")  # Print wrong message

  play = input("Would you like another card? (yes|no|restart): ")  # Ask user if they want to play again

  if play.lower() == "yes":  # Check if user wants another card
    divide_flashcards()  # Call the divide_flashcards function again
  elif play.lower() == "no":  # Check if user wants to stop playing
    print("Thanks for playing!")  # Print thank you message
  elif play.lower() == "restart":  # Check if user wants to restart the game
    start_game()  # Restart the game
  else:
    print(f"Sorry, I don't recognize {play}.")  # Print error message for unrecognized input
    input("Please hit enter to try again.")  # Prompt user to hit enter to try again
    divide_flashcards()  # Call the divide_flashcards function again

start_game()  # Start the game
