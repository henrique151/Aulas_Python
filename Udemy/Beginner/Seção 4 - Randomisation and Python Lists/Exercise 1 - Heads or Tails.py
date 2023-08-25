#Remember to use the random module
import random
#Hint: Remember to import the random module here at the top of the file. 🎲

#Write the rest of your code below this line 👇

random_luck = random.randint(0, 1)

if random_luck == 1:
    print("Heads")
else:
    print("Tails")