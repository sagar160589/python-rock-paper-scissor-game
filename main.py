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
import random

game_option = [rock, paper, scissors]
user_option = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
if user_option == 0:
    print(rock)
elif user_option == 1:
    print(paper)
else:
    print(scissors)

computer_random_choice = random.randint(0, 2)
print("Computer chose: \n")
computer_option = computer_random_choice
print(game_option[computer_random_choice])

if computer_option == user_option:
    print("Game Tied. Please play again...")
elif computer_option == 0 and user_option == 2:
    print("Computer won!")
elif computer_option == 2 and user_option == 1:
    print("Computer won!")
elif computer_option == 1 and user_option == 0:
    print("Computer won!")
else:
    print("You won. Well Played!")
