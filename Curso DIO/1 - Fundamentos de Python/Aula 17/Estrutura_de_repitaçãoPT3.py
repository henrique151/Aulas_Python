opcao = -1
while opcao != 0:   
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: ")) 
    
    if opcao == 1:        
        print("Sacando...")   
    elif opcao == 2:       
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar o programa")
    
print("=" * 50)

while True: # Isso é loop verdadeira
   opcao = int(input("Informe um número")) 
   if opcao == 10:
    break

   if opcao % 2 != 0:
       continue
   print(f"Seu número é par {opcao}")
    
   