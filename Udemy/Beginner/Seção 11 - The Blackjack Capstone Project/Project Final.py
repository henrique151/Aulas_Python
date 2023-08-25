## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.

import random
##from replit import clear
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_random = random.choice(cards)
    return cards_random

def calculate_score(cards_random):
    if sum(cards_random) == 21 and len(cards_random) == 2:
        return 0

    if 11 in cards_random and sum(cards_random) > 21:
        cards_random.remove(11)
        cards_random.append(1)

    return sum(cards_random)

def compare(computer_score, user_score):
    if computer_score == user_score:
        return "O Jogo deu empate"
    elif computer_score == 0 or user_score > 21:
        return "O Computador venceu"
    elif user_score == 0 or computer_score > 21:
        return "O Usuário venceu"
    elif user_score > computer_score:
        return "O Usuário venceu"
    else:
        return "O Computador venceu"

def play_game():

    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for number in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    
        print(f" Seus cartões: {user_cards}, pontuação atual: {user_score}")
        print(f" Primeira placa do computador: {computer_cards[0]}")
    
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            quest = input(
                "Digite 'Sim ou sim' para obter outro cartão, digite 'Não ou não' para passar: "
            ).lower()
            if quest == "sim" or quest == "Sim":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f" Sua mão final: {user_cards}, pontuação final: {user_score}")
    print(
        f" Mão final do computador: {computer_cards}, pontuação final: {computer_score}"
    )
    print(compare(computer_score, user_score))
    
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Você quer jogar uma partida de Blackjack? Digite 'sim' ou 'não':") == "sim":
    clear()
    play_game()
