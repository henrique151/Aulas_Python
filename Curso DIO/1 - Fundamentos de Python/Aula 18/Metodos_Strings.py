curso = "pYtHon"

print(curso.upper()) # Todo masiculo
print(curso.lower()) # Todo minsuculo
print(curso.title()) # No incio maisculo

print("=" * 50)

curso = "   Python " 

print(curso.strip()) # Ele tirar todos os espações
print(curso.lstrip()) # Ele tirar todos os espações no inicio
print(curso.rstrip())  # Ele tirar todos os espações no final

print("=" * 50)

curso = "Python"

print(curso.center(10, "#"))
print(".".join(curso))

print("=" * 50)


text = "  Qual é seu nome     ." 
print(text.strip() + "*") # Ele tirar todos os espações
print(text.lstrip() + "*") # Ele tirar todos os espações no inicio
print(text.rstrip() + "*")  # Ele tirar todos os espações no final

print("=" * 50)

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, ".", end="-"))

for letra in menu:
        print(letra, end="-")
print()






