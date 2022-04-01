import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("ROCK PAPER SCISSORS\n\n")
player1 = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors  ")
player = int(player1)

if player == 1:
  print(paper)
elif player == 0:
  print(rock)
elif player == 2:
  print(scissors)
  
  
  hands = [rock, paper, scissors]
  x = len(hands)
  random_hands = random.randint(0, x - 1)
  computer = hands[random_hands]
  print(f"Computer chose \n {computer}")
  
  if player == 0:
    if computer == scissors:
      print("You win")
    elif computer == rock:
      print("You draw")
    else:
      print("You Lose")
  if player == 1:
    if computer == rock:
      print("You win")
    elif computer == paper:
      print("You draw")
    else:
      print("You Lose")
  if player == 2:
    if computer == paper:
      print("You win")
    elif computer == scissors:
      print("You draw")
    else:
      print("You Lose")
  
else:
  print("You chose an invalid number, You Lose")