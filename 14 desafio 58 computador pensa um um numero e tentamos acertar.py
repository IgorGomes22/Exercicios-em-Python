#desafio 58
#computador pensa em um numero de 0 a 10.
# e a gente tenta acertar,mostrando quantos palpites foi necessario

import random

tentativa = 0
computador = random.randrange(1,10)
set = 1
while  set == 1 :
    
    print('===='*11)
    jogador=int(input('Escolha um numero de 0 a 10  :'))
    tentativa += 1
    if jogador == computador :
         print('Parabéns voce acertou ,voce precisou de {} tentativas '.format(tentativa))
         tentativa = 0
         computador = random.randrange(0,10)
    else :
         print('Não foi dessa vez,tente novamente')






 
