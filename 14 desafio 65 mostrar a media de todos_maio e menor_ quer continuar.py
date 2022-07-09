#desafio 65
#ler varios valores e pergunta se quer continuar
#mostar a media de todos os numeros digitados
#qual o maior e menor 

numeros =0
count = 0
maior =0
menor = 0
set = 'S'
while set =='S':
    print('======='*11)
    n1 = int(input('Digite algum valor'))
    count +=1
    numeros = numeros +n1
    media = numeros / count
    if n1 > maior :
        maior = n1
        menor = n1
    if n1 < menor :
         menor = n1
    set = str(input('Deseja continuar ? [ S / N ]')).upper()

              
print('Ao total voce digitou {} numeros e a media deles é {}'.format(count,media))
print('O maior numero foi {} , e o menor {}'.format(maior,menor))
count = 0
maior = 0
menor = 0
