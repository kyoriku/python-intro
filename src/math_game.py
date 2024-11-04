import random
from os import system

def start_game():
  system('clear')
  print('Welcome to Math Flashcards!')
  pick = input("Choose your flashcards (add|subtract|multiply|divide): ")
  
  if pick.lower() == "add":
    # print(f"You picked {pick}!")
    add_flashcards()
  elif pick.lower() == "subtract":
    # print(f"You picked {pick}!")
    subtract_flashcards()
  elif pick.lower() == "multiply":
    # print(f"You picked {pick}!")
    multiply_flashcards()
  elif pick.lower() == "divide":
    # print(f"You picked {pick}!")
    divide_flashcards()
  else:
    print(f"Sorry, I don't recognize {pick}.")
    input("Please hit enter to try again.")
    start_game()

def add_flashcards():
  system('clear')
  card_one = random.randint(0, 10)
  card_two = random.randint(0, 10)
  correct = card_one + card_two
  answer = input(f"{card_one} + {card_two}: ")

  if int(answer) == correct:
    print(f"Correct! {card_one} + {card_two} = {answer}")
  else:
    print(f"Wrong! {card_one} + {card_two} = {correct}")
    
  play = input("Would you like another card? (yes|no|restart): ")

  if play.lower() == "yes":
    add_flashcards()
  elif play.lower() == "no":
    print("Thanks for playing!")
  elif play.lower() == "restart":
    start_game()
  else:
    print(f"Sorry, I don't recognize {play}.")
    input("Please hit enter to try again.")
    add_flashcards()

def subtract_flashcards():
  system('clear')
  card_one = random.randint(0, 10)
  card_two = random.randint(0, 10)
  correct = card_one - card_two
  answer = input(f"{card_one} - {card_two}: ")

  if int(answer) == correct:
    print(f"Correct! {card_one} - {card_two} = {answer}")
  else:
    print(f"Wrong! {card_one} - {card_two} = {correct}")

  play = input("Would you like another card? (yes|no|restart): ")

  if play.lower() == "yes":
    subtract_flashcards()
  elif play.lower() == "no":
    print("Thanks for playing!")
  elif play.lower() == "restart":
    start_game()
  else:
    print(f"Sorry, I don't recognize {play}.")
    input("Please hit enter to try again.")
    subtract_flashcards()

def multiply_flashcards():
  system('clear')
  card_one = random.randint(0, 10)
  card_two = random.randint(0, 10)
  correct = card_one * card_two
  answer = input(f"{card_one} * {card_two}: ")

  if int(answer) == correct:
    print(f"Correct! {card_one} * {card_two} = {answer}")
  else:
    print(f"Wrong! {card_one} * {card_two} = {correct}")

  play = input("Would you like another card? (yes|no|restart): ")

  if play.lower() == "yes":
    multiply_flashcards()
  elif play.lower() == "no":
    print("Thanks for playing!")
  elif play.lower() == "restart":
    start_game()
  else:
    print(f"Sorry, I don't recognize {play}.")
    input("Please hit enter to try again.")
    multiply_flashcards()

def divide_flashcards():
  system('clear')
  card_one = random.randint(0, 10)
  card_two = random.randint(1, 10)
  correct = card_one / card_two
  answer = input(f"{card_one} / {card_two}: ")

  if int(answer) == correct:
    print(f"Correct! {card_one} / {card_two} = {answer}")
  else:
    print(f"Wrong! {card_one} / {card_two} = {correct}")

  play = input("Would you like another card? (yes|no|restart): ")

  if play.lower() == "yes":
    divide_flashcards()
  elif play.lower() == "no":
    print("Thanks for playing!")
  elif play.lower() == "restart":
    start_game()
  else:
    print(f"Sorry, I don't recognize {play}.")
    input("Please hit enter to try again.")
    divide_flashcards()

start_game()
