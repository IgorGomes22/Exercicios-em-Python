#desafio 104
#funcao leiaint()
#aceitar apenas valor numerico

def leiaint(n):
    print(f'O numero é {n}')

while True :
    numero=str(input('Digite um numero inteiro : '))
    if numero.isnumeric():
        numero=int(numero)
        break
    else:
        print('<<Erro! Digite um valor numerico>>')
leiaint(numero)
