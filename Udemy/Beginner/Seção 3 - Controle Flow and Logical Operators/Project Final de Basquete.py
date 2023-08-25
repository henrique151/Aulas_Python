print('''
*******************************************************************************
                           .
                         ,-; . ,
                ________i_,',//
          _odHHHHHHHHHHHHHHHHbo_
        dP^'         ;.| ||,; `^?b
       |H           ))`'||/';    H|
        ?bo.     .=;'   |||.' ,odP
          `?oo.-','     ||'oodP'
            /'  /      / |/
           |   |    _-'  ||
          ||  |   ,'     J|
          | \ |   |     / |
           |_\ L  L  .-' |
            \.)`-.;-;__./
              "-._;_.-"
*******************************************************************************
''')
print("Bem-vindo ao final de uma partida de basquete.")
print("Sua missão é ganhar um jogo de basquete")

choice1 = input(
    """Você estiver no meio da quadra de basquete, terá algumas opções. Você pode:

B - Passe a bola para um companheiro de equipe.
D - Drible passando pela defesa.
R - Recuar ou recuar para reavaliar a situação.

Por favor, digite a letra correspondente para indicar sua escolha.""").lower()
if choice1 == "d":
    choice2 = input(
        """Você conseguiu driblar a defesa e se encontra na zona de três pontos, você tem algumas opções. Você pode:

T - Dê uma chance para uma cesta de três pontos.
P - Passe a bola por trás para o seu companheiro de equipe.
D - Drible novamente.

Por favor, digite a letra correspondente para indicar sua escolha.""").lower()
    if choice2 == "p":
        choice3 = input(
            """Depois do passe bem-sucedido que você fez, agora você vai encontra em uma posição muito favorável após receber um passe bem-sucedido e a defesa está focada em seu companheiro de equipe, você tem algumas opções. Você pode:

D - Dribla a defesa até a cesta e faça uma enterrada.
Z - Vá para a zona de três pontos e faça uma cesta de campo.
L - Lançar um lance livre.

Por favor, digite a letra correspondente para indicar sua escolha.""").lower()
        if choice3 == "z":
            print(
                "Infelizmente, não deu certo. A equipe adversária conseguiu interceptar antes de chegar à zona de três pontos e recuperar a posse de bola. Em seguida, eles marcaram uma cesta decisiva, e é fim de jogo."
            )
        elif choice3 == "d":
            print(
                "Você driblou a defesa novamente e está livre para executar uma enterrada, replicando o icônico movimento de Michael Jordan. Parabéns por conquistar a melhor partida da sua vida! Você venceu a partida."
            )
        elif choice3 == "l":
            print(
                "Infelizmente, o seu arremesso foi interceptado por um jogador adversário, resultando em um contra-ataque rápido. Eles conseguiram recuperar a posse de bola e marcar uma cesta decisiva, encerrando o jogo."
            )
        else:
            print(
                "Sua jogada não deu certo e a equipe adversária aproveitou para fazer um contra-ataque rápido. Eles conseguiram recuperar a posse de bola e marcar uma cesta decisiva, encerrando o jogo."
            )
    else:
        print(
            "Sua jogada não deu certo e a equipe adversária aproveitou para fazer um contra-ataque rápido. Eles conseguiram recuperar a posse de bola e marcar uma cesta decisiva, encerrando o jogo."
        )
else:
    print(
        "Sua jogada não deu certo e a equipe adversária aproveitou para fazer um contra-ataque rápido. Eles conseguiram recuperar a posse de bola e marcar uma cesta decisiva, encerrando o jogo."
    )
