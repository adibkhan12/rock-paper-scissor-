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
game_list = [rock, paper, scissors]
my_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if my_choice not in ["0", "1", "2"]:
    print("please choose a valid number!")
else:
    my_choice = int(my_choice)
    print(game_list[my_choice])

    print("Computer chooses")
    computer_chooses = random.randint(0, 2)
    print(game_list[computer_chooses])

    if my_choice == computer_chooses:
        print("draw")
    elif ((my_choice == 0 and computer_chooses == 2) or (my_choice == 1 and computer_chooses == 0) or
          (my_choice == 2 and computer_chooses == 1)):
        print("You Win !")
    else:
        print("you lose")
