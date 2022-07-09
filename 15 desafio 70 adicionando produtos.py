 #desafio 70
#ler nome e o preco de produtos.
#perguntar se quer continuar
#mostrar total gasto/qts produtos custa acima de mil reais
#nome produto mais barato
print("""*********************************************************************
                                Mercadinho da Automação
*********************************************************************""")
total = totmil = menor = cont = 0
barato =' '
while True :
    produto = str(input('Nome do Produto : '))
    preco = float(input('Preco : R$  '))
    cont += 1
    total += preco
    
    if preco > 1000 :
        totmil += 1
        
    if cont == 1  or preco < menor :
        menor = preco
        barato = produto 
        
    continuar = ' '
    while continuar  not in 'SN' :
        continuar = str(input('Adicionar mais produtos ?  [S / N]')).strip().upper()[0]
    if  continuar == 'N' :
        break

print(f' Total gastos é de R$ {total:.2f}')
print(f' Ao total {totmil} produtos é acima de R$ 1.000,00 ')
print(f' O produto  mais barato é {barato} que custa R$ {menor:.2f}')
