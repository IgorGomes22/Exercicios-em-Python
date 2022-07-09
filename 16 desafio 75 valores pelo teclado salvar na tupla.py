#desafio 75
#ler 4 valores pelo teclado e guardar na tupla
#quantas vezes apareceu o valor
#em que posicao foi digitado o primeiro valor 3
#quais foram os numeros pares

num =(int(input('Digite um numero: ')),
            int(input('Digite outro numero: ')),
            int(input('Digite mais um numero: ')),
            int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {num}')
if 9 in num:
    print(f'o valor 9 apareceu {num.count(9)} vezes')
else :
    print('O valor 9 não foi digitado')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3)+1}° posição')
else :
    print('o valor 3 não foi digitado em nenhuma posição')
for n in num:
    if n% 2 == 0:
        print(f'os numeros par  : {n}')
