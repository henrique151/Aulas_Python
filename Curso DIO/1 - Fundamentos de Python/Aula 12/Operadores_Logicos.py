print("=" * 50)
saldo = 1000
saque = 200
limite = 100

saldo >= saque
# >>> True
saque <= limite
# >>> False


print("=" * 50)

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
# >>> False

saldo >= saque or saque <= limite
# >>> True

print("=" * 50)

contatos_emergencia = []

not 1000 > 1500
# >>> True

not contatos_emergencia 
# >>> True

not "saque 1500;"
# >>> False

not ""
# >>> True


print("=" * 50)

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

print("=" * 50)

balance = 1000
withdraw = 250
limit = 200
special_account =  True

exm1 = balance >= withdraw and withdraw <= limit or special_account and balance >= withdraw
print(exm1)

exm2 = (balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw)
print(exm2)

print("=" * 50)

conta_normal_com_saldo = (balance >= withdraw and withdraw <= limit)
conta_special_com_saldo = (special_account and balance >= withdraw)

exm3 = conta_normal_com_saldo or conta_special_com_saldo
print(exm3)