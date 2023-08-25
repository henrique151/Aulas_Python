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

game_images = [rock, paper, scissors]
usuario = [rock, paper, scissors]

usuario_num = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
    ))

if usuario_num >= 3 or usuario_num < 0:
    print("You typed an invalid number, you lose!")
else:
    print(usuario[usuario_num])
    random_num = random.randint(0, 2)
    print("Computer chose.")
    print(game_images[random_num])
    if usuario_num == 0 and random_num == 2:
      print("You win!")
    elif random_num == 0 and usuario_num == 2:
      print("You lose")
    elif usuario_num > random_num:
      print("You win.")
    elif random_num > usuario_num:
      print("You lose.")
    elif random_num == usuario_num:
      print("It's a draw")
