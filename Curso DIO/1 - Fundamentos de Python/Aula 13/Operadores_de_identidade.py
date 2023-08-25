curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

a = curso is nome_curso
print(a) 

a = curso is not nome_curso
print(a) 

a = saldo is limite
print(a) 

print("=" * 50)

saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)