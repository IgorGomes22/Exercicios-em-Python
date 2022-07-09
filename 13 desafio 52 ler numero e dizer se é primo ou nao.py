#desafio 52
# ler numero inteiro e dizer se é ou nao um numero primo

n=int(input('Digite um numero :  '))
p =0
for c in range(1, n+1):
    if n % c ==0 :
        p += +1
if p== 2 :
    print('Primo')
else:
    print('Nao é primo')
    
