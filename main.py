#Number Guessing Game Objectives:
# Include an ASCII art logo.
from art import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_answer(guess, answer, turns):
  #check the answer against the guess
  if guess > answer:
    print("Too High")
    return turns - 1
  elif guess < answer:
    print("Too Low")
    return turns - 1
  else:
    print(f"You got it! The answer is {answer}.")

# This function will set the difficulty of the game
def difficulty():
  level = input("Choose difficulty, type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL

# The game function itself
def game():
  print(logo)
  print("Welcome to the number guess game.")
  print("I am thinking of a number between 1 and 100.")
  answer = random.randint(1,100)
  #print(f"Psst, the answer is {answer}")
  turns = difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts left to guess the number.")
    guess = int(input("Make a guess\n"))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have run out of guess. You lose")
      return
    elif guess != answer:
      print("Guess again")
game()