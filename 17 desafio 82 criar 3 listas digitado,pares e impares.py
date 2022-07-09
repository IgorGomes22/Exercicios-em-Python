#desafio 82
#ler varios numeros em uma lista
#criar duas listas extras que vao onter pares, e impares
#mostar conteudo das tres listas

lista = []
listapar =[]
listaimpar =[]

while True :
    continuar = ' '
    lista.append(int(input('Digite um valor  :')))
     
    while continuar not in 'SN':
         continuar = str(input('Deseja continuar ?  [S / N]')).strip().upper()   
    if continuar in 'Nn' :
        break
for list in (lista):
    if list  % 2 == 0 :
        listapar.append(list) 
    else: listaimpar.append(list)
print('¨¨¨¨'*10)
print(f'A lista geral é : {lista}')
print(f'A lista par é : {listapar}')
print(f'A lista impar é :{listaimpar}')
