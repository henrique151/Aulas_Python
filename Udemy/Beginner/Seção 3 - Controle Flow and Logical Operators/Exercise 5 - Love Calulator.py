# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_name1 = name1.lower()
new_name2 = name2.lower()

name_t = new_name1.count('t') + new_name2.count('t')
name_r = new_name1.count('r') + new_name2.count('r')
name_u = new_name1.count('u') + new_name2.count('u')
name_e = new_name1.count('e') + new_name2.count('e')

name_true_total = name_t + name_r + name_u + name_e

name_l = new_name1.count('l') + new_name2.count('l')
name_o = new_name1.count('o') + new_name2.count('o')
name_v = new_name1.count('v') + new_name2.count('v')

name_love_total = name_l + name_o + name_v + name_e

love_score = int(f"{name_true_total}{name_love_total} ")
# Or love_score = int(str(name_true_total) + str(name_love_total))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

