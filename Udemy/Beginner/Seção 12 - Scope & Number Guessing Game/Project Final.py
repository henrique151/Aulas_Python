import random
from art import logo

print(logo)

luck = random.randint(1, 100)
print(f"Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. \nPssst, the correct answer is {luck}")
quest = input("Choose a difficulty. Type 'easy' or 'hard':")

def easy_game(): 
    live_easy = 10
    Gamer_over = False
    while not Gamer_over:
        if live_easy == 0:
            Gamer_over = True
        else:
            print(f"You have {live_easy} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))           
            if guess == luck:
                print(f"You got it! The answer was {luck}")
                Gamer_over = True
            elif guess > luck:
                print("Too high.\nGuess again.")
                live_easy -= 1
            elif guess < luck:
                print("Too low.\nGuess again.")
                live_easy -= 1

def hard_game():
    live_hard = 5
    Gamer_over = False
    while not Gamer_over:
        if live_hard == 0:
            Gamer_over = True
        else:
            print(f"You have {live_hard} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))             
            if guess == luck:
                print(f"You got it! The answer was {luck}")
                Gamer_over = True
            elif guess > luck:
                print("Too high.\nGuess again.")
                live_hard -= 1
            elif guess < luck:
                print("Too low.\nGuess again.")
                live_hard -= 1


if quest.lower() == "easy":
    easy_game()
elif quest.lower() == "hard":
    hard_game()


        
    

    


