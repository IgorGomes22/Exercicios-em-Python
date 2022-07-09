#desafio 48
#calcular soma entre numeros impar que sao multiplos de 3 etre 1 a 500
s =0
for c in range(1,500):
    if c %3 ==0 :
        s+=c
        print('O somatorio dos multiplos de 3 é  : {}',format(s))
        
print('####FIM####')
