#desafio 51
# ler o primeiro termo da razao de uma PA(progressao aritmetica.
#no final mostrar os 10 primeiros termos da PA

p= int(input(' Digite o primeiro termo  :'))
r = int(input('Digite a razao  :'))
a = p
for c in range(0,9):
    a = a+r
    print('resultdo   {}'.format(a))
