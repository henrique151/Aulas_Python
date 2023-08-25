name = "Santader"
lastname = "Water"

print(name, lastname)
print(name, lastname, end="...\n")
print(name, lastname, sep="#")

print("=" * 50)

name = input("Inform the your name: ")
age = input("Inform the your age: ")
print(name, age)
print(name, age, end="...\n")
print(name, age, end="...\n", sep="#")

print("=" * 50)

num1=int(input('Digite o Primeiro Número: '))
num2=int(input('Digite o Segundo Número: '))
num3 = (num1 + num2)

print('A soma do', num1 , ' + ', num2 , ' = ' , num3)

print("=" * 50)

print('Outra versão')

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1+n2
print(f'A soma entre {n1} e {n2} vale {s}')