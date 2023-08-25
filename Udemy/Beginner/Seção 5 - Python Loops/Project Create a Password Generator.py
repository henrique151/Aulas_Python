#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = [] # O password_list está sendo delarada com uma lista para ser armazada.

  # O Char seria o nome do for que vai armazana tudo que está sendo usado.
  # A função range seria como um i = 0; i > 10; i++; Ele começar de um número e termina lar, começar pelo o indice então coloque mais +1 para ser numero que você deseja.
for char in range(1, nr_letters + 1):
  # A função password_list.append e de adicinaor o que está dentro do random.choice
  # A função random.choice seria para seleciona um número altenario na lista letters
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  # A função password_list.append e de adicinaor o que está dentro do random.choice
  # A função random.choice seria para seleciona um número altenario na lista letters
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  # A função password_list.append e de adicinaor o que está dentro do random.choice
  # A função random.choice seria para seleciona um número altenario na lista letters
  password_list += random.choice(numbers)

print(password_list)
# A função do random.shuffle serve para troca as posição da varivel password_list que armazou todos os numeros, letras e caratre espicial
random.shuffle(password_list)

print(password_list)

password = ""
for char in password_list:
  password += char
  # Ele está adionador que estáva no password_list e colocado o dentro do char, depois está sendo usada para fazer a junção dos valores armazados e adionado no passwors como no final.

print(f"Your password is: {password}")