Maior_Age = 18
idade_special  = 12

idade = int(input("Inform your age"))

if idade >= Maior_Age:
    print("Maior de idade, pode tirar a CNH")
    
if idade < Maior_Age:
    print("Ainda não pode tirar a CNH")
    
print("=" * 50)   
    
if idade >= Maior_Age:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")
    
print("=" * 50)   

if idade >= Maior_Age:
    print("Maior de idade, pode tirar a CNH")
elif idade == idade_special: 
    print("Você pode tirar so com oritatação com do resposavel")
else:
    print("Ainda não pode tirar a CNH")
    
print("=" * 50)   

conta_normal = True
conta_universitaria = False
conta_special = True

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:	
    if saldo >= saque:	
        print("Saque realizado com sucesso!")	
    elif saque <= (saldo + cheque_especial):		
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel fazer o saque")
elif conta_universitaria:	
    if saldo >= saque:	
        print("Saque realizado com sucesso!")
    else:		
        print("Saldo insuficiente!")
elif conta_special:
    print("Conta escpial selecionado!")
else:
    print("Sistema não foi")

print("=" * 50)  

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao relizar o saque")
    