################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local Scope

# def drink_potion():
#     potion_strantg = 2 # Local
#     print(potion_strantg)

# drink_potion()
# print(potion_strantg)

# Global Scope

# player_health = 10 # Global

# def game():
#     def drink_potion():
#         potion_strantg = 2 # Local
#         print(player_health)
#     drink_potion()

# print(player_health)

# game_leval = 3

# def create_enemy():
#     enemies = ["Skeleton","Zombie","Alien"]
#     if game_leval < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)
# create_enemy()

# enemies = 1

# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

#Global Constants

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@henrique151"

