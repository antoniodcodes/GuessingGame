"""A number-guessing game."""

# Put your code here
from random import randint # imports randint

def greeting():
  print("""
  Welcome to the number-guessing game!\n
  Instructions: I will think of a number between 1 and 100 and you have to guess it.
  """)

def get_user_name():
  username = input("What's your name? ")
  return username

def check_guess(guess, choice):
  if guess > choice:
    return 1
  elif guess < choice:
    return -1
  else:
    return 0
  

def main():
  choice = randint(1, 101)
  greeting()
  username = get_user_name()
  sentinel = input("Would you like tp play a game? (yes/no) ").lower()
  try:
    while sentinel == 'yes' or sentinel == 'y':
      guess = int(input("What's your guess? "))
      number_of_guesses += 1
      result = check_guess(guess, choice)
      if result == -1:
        print("Your guess was too low.")
      elif result == 1:
        print("Your guess was too high.")
      else:
        print(f"You guessed correctly, {username}. You completed it in {number_of_guesses} guesses.")
        sentinel = input("Would you like to play again? (yes/no) ").lower()
  except ValueError:
    print("Please provide a valid number. ")
    main()



main()