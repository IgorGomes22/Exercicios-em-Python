#desafio 28
import random
print('--Tente advinhar qual numero o computador escolheu  --')

numero_secreto = random.randrange(0,5)
print(numero_secreto)
tentativa = 3

for rodada in range (1, tentativa +1 ):/
    print('Tentativa {} de {} '.format(rodada ,tentativa))
    chute = int(input('Digite aqui seu palpite : '))
    print('Voce chutou o numero  ',chute)

    if (chute <0 or chute >5):
        print('Voce deve escolher um numero entre 0 e 5')
        continue

    acertou = numero_secreto == chute
    maior = chute>numero_secreto
    menor = chute<numero_secreto

    if acertou:
           print('Parabens,Voce acertou !!!!!!!!')
           break
    else:
        if(maior):
            print('Voce errou! Seu chute foi maior que o numero secreto ')
        elif(menor):
            print('Voce errou! Seu chute foi menor que o numero secreto ')

print('----Fim de jogo----')
