N = int(input()) 
# A primeira linha lê o valor de N a partir da entrada padrão (o teclado). Esse valor representa a quantidade de casos de teste que serão realizados.

for i in range(N):
    A, B = input().split 
    # O loop for irá executar N vezes. Em cada iteração, a linha lê uma linha da entrada e separa os valores A e B utilizando o método split().
    # Verifica se B é igual aos últimos dígitos de A
    if A.endswith(B): 
        # Essa parte do código verifica se B é igual aos últimos dígitos de A utilizando o método endswith(). 
        # Se a verificação for verdadeira, o programa imprime "encaixa". Caso contrário, imprime "nao encaixa".
        print("encaixa")
    else:
        print("nao encaixa")