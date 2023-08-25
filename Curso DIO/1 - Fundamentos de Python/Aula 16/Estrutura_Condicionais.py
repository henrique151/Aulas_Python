saldo = 2000.0
saque = float(input("Inform the valor of saque:"))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficinete")
    
print("=" * 50)

opcao= int(input("Inform uma opcao [1] Sacar \n [2] Extrato"))

if opcao == 1:
    valor = float(input("Inform a quantia of saque:"))

elif opcao == 2:
    print("Exibindo o extrato...")
else: 
    SystemExit.exit("Opção invalida")
    
 