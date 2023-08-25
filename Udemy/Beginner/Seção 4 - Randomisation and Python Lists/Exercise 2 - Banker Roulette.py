import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇
A = len(names)
random_num = random.randint(0, A - 1)
names_new = names[random_num]

# Or

#names_new = random.choice(names)
print(f"{names_new} is going to buy the meal today!")