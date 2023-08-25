# O def sacar(valor) seria como fosso um metodo:

def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado")
    else:
        print("valor erro")
    print("Obrigado por ser cliente")   
    
    
def desposita(valor):
    saldo = 500
    saldo += valor
    
    
sacar(1000)