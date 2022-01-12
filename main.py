rock = '''
    _______
---'   ____)
      (_____)
      (_____)           Rock
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)       PAPER
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)   SCISSORS
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

user = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.: "))

if user == 0:
  print(rock)
elif user == 1:
  print(paper)
elif user == 2:
  print(scissors)

com = random.randint(0,2)
print("Computer Chose:")
if com == 0:
  print(rock)
elif com == 1:
  print(paper)
elif com == 2:
  print(scissors)

if user == com :
  print("It's a Draw !!!")
elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com == 0):
  print("You Lose !!!")
else:
  print("You Won !!!")