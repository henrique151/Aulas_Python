# Lê o número de casos de teste
C = int(input())

# Itera pelos casos de teste
for i in range(C):
    # Lê o nível de energia do ser vivo
    N = int(input())
    
    # Verifica se é um inseto ou não
    if N <= 8000:
        print("Inseto!")
    else:
        print("Mais de 8000!")
