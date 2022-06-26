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
game_images = [rock,paper,scissors]


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose.")
else:
    print("You choose " + game_images[user_choice])


    computer_choice = random.randint(0,2)
    computer_choice_name = game_images[computer_choice]
    print("Computer chooses" + computer_choice_name)

    if user_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif user_choice == computer_choice:
        print("You tied!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose!")
