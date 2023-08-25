import random
from art import logo, vs
from game_data import data

Score = 0
data_person = {}
def autors():
    data_random = random.choice(data)
    return data_random

data_new = autors()
print(data_new)
for key, value in data_new.items():
    data_person[key] = value
    print(value)

def game():
    print(logo)
    print(f"Compare A:{data_new[name]}")
    print(vs)
    print(f"Compare B:")

game()
    