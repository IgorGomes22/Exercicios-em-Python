#desafio 55
#pegar peso de 5 pessoas
#mostrar qual foi o maior e menor


maior = 0
menor = 0

for c in range(1,6):
    peso = int(input('Digite o peso   :'))
    
    if  c == 1 :
        maior = peso
        menor = peso
    else:
        if peso > maior :
           maior = peso
           
        if  peso < menor:
            menor = peso

print('O maior peso foi  {}kg'.format(maior))
print('O menor peso foi  {}kg'.format(menor))
