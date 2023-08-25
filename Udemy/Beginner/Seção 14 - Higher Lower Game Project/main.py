import random
from art import logo, vs
from game_data import data
import os

Score = 0  # Inicializa a pontuação do jogador
data_person = {}  # Dicionário para armazenar informações sobre as pessoas para comparação
last_wrong_person = None  # Armazena a pessoa que o jogador havia errado na última rodada

def game():
    global Score # Acesso à variável global de pontuação
    global last_wrong_person # Acesso à variável global para lembrar a última pessoa errada
    clear_screen()  # Limpa a tela para a próxima rodada do jogo
    print(logo)  # Imprime o logotipo do jogo
    if Score > 0:
        print(f"You're right! Current score: {Score}.") # Mostra a pontuação atual se não for a primeira rodada
    autors() # Escolhe aleatoriamente as duas pessoas para a comparação
    print_person_info() # Exibe as informações das duas pessoas para a comparação
    Quest = input("Who has more followers? Type 'A' or 'B': ")  # Solicita a entrada do jogador (A ou B)
    pessoa, result = comparador(Quest)  # Compara as opções escolhidas pelo jogador
    clear_screen()  # Limpa a tela para exibir o resultado

    if result: # Se a resposta do jogador estiver correta
        Score += 1  # Incrementa a pontuação
        print(pessoa) # Exibe mensagem de acerto e a pontuação atual
        last_wrong_person = data_person["B"] # Define a pessoa errada como a próxima opção
        game()   # Chama a função do jogo novamente para a próxima rodada
    else:
        clear_screen()
        print(logo)
        print(pessoa)  # Exibe mensagem de erro e a pontuação final

def autors():
    global last_wrong_person  # Acesso à variável global que armazena a pessoa errada da última rodada
    # Escolhe a primeira pessoa com base na pessoa errada da última rodada, se houver
    data_random1 = last_wrong_person if last_wrong_person else random.choice(data) # Ou seja, se a condição (last_wrong_person) for avaliada como verdadeira (ou seja, se last_wrong_person tiver um valor), então data_random1 receberá o valor de last_wrong_person. Caso contrário, se a condição for avaliada como falsa (ou seja, se last_wrong_person for None), então data_random1 receberá um valor aleatório escolhido usando random.choice(data).
    data_person["A"] = data_random1  # Atribui a primeira pessoa aleatória para a opção A

    data_random2 = random.choice(data)
    while data_random2 == data_random1:
        data_random2 = random.choice(data)  # Escolhe aleatoriamente a segunda pessoa, garantindo que seja diferente da primeira
    data_person["B"] = data_random2  # Atribui a segunda pessoa aleatória para a opção B

def clear_screen():
    os.system('clear')  # Utiliza o comando do sistema para limpar a tela (pode variar em sistemas diferentes)

def comparador(Quest):
    one_person = data_person['A']['follower_count']  # Obtém o número de seguidores da primeira pessoa
    two_person = data_person['B']['follower_count']  # Obtém o número de seguidores da segunda pessoa
    
    if Quest == 'A' or Quest == 'a':
        if one_person > two_person:  # Compara o número de seguidores das duas pessoas
            return f"You're right! Current score: {Score}.", True  # Retorna mensagem de acerto e resultado verdadeiro
        else:
            return f"Sorry, that's wrong. Final score: {Score}", False  # Retorna mensagem de erro e resultado falso
    elif Quest == 'B' or Quest == 'b':
        if two_person > one_person:  # Compara o número de seguidores das duas pessoas
            return f"You're right! Current score: {Score}.", True  
        else:
            return f"Sorry, that's wrong. Final score: {Score}", False 
    else:
        return "Invalid input, please type 'A' or 'B'", False  


def print_person_info():
    # Imprime informações sobre a primeira pessoa para comparação (A)
    print(f"Compare A: {data_person['A']['name']}, {data_person['A']['description']}, from {data_person['A']['country']}.") # Imprime as informações da primeira pessoa para comparação (A) usando f-string
    # Inclui o nome, descrição e país da primeira pessoa
    print(vs) # Imprime a arte gráfica de comparação (vs)
    print(f"Against B: {data_person['B']['name']}, {data_person['B']['description']}, from {data_person['B']['country']}.") 

game()  # Inicia o jogo