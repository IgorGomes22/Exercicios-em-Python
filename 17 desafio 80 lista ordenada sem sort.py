#desafio 80
# ler 5 valores numericos  cadastrar em uma lista
#ja na posicao correata sem usar sort()
#mostrar lista ordeada

lista = []

for c in range(0,5):
    n = int(input('Digite um valor :'))
    if c == 0  or n > lista[-1] :                        #se nao for o 1° nem  maior que o ultimo,adiciona
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('---'*10)
print(f'Os valores digitados em ordem foram : {lista}')
