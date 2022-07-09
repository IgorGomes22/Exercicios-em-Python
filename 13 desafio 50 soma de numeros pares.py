#desafio 50
# ler seis numeros inteiros mlsgra a soma dos que forem pares

from time import sleep

s=0
for c in range(1,7):
    n = int(input('Digite o  {}°  numero :  '.format(c)))
    if n %2 == 0:
         s += n
sleep(1)
print('A soma dos numeros pares é  :{}'.format(s))

