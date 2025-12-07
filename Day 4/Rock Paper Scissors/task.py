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
rps = [rock, paper, scissors]
player_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
if player_pick >= 0 and player_pick <=2:
    player_image = rps[player_pick]
    print(player_image)
else:
    print("Invalid Input")
program_pick = random.randint(0,2)
program_image = rps[program_pick]
print(program_image)

if player_pick == 0 and program_pick == 2:
    print("You win!")
elif player_pick >= 3 or player_pick < 0:
    print("You didn't choose a valid number. You lose!")
elif program_pick == 0 and player_pick == 0:
    print("You loose!")
elif program_pick > player_pick:
    print("You loose!")
elif player_pick > program_pick:
    print ("You win!")
elif player_pick == program_pick:
    print("It's a draw!")
