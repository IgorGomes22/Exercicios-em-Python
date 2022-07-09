#desafio 79
#ler varios valores numericos e cadastrar em uma lista
#|se numero ja existir nao sera adicionado
#no final sera mostrado todos os numeros em ordem crescente

from tkinter import *
root = Tk()
root.mainloop()
print('----'*10)
lista=[]

while True :
    n = (int(input('Digite um valor : ')))
    if n not in lista :
        lista.append(n)
        print('Valor adicionado com secesso')
    else:
        print('valor repetido , não vou adicionar!')
         
    set = str(input('Voce deseja continuar ? [S/N]'))
    if set in 'Nn' :
        break
lista.sort()
print(f'Os numeros digitados foi : {lista}')
print('----'*10)

