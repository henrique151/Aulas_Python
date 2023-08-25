
# Elá não é mais tanto usanda o Foramto %

print("=" * 50)

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#%s Trabalha com String
#%d Trabalha com Inteira
#$f Trabalha com Float 

 
print("=" * 50)

# O metódo de format ele e banstante usado.

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

pessoa = {"nome": "Guilherme", "idade": 28, "profissao": "Progamador", "linguagem": "Python" }

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("=" * 50)

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("=" * 50)

print("Olá, me chamo {nome} {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))


# O metódo de f{} ele e banstante usado.

print("=" * 50)

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 350.000

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. E ganhho {saldo:.3f}")
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. E ganhho {saldo:10.3f}")

print("=" * 50)

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")





