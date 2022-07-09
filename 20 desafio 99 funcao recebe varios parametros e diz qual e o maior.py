#desafio 99
#funcao chamada maior()
#receber vario sparametros com valore inteiros
#o programatem que analisar todos os parametros
#e dizer qual e o maior

from time import sleep

def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...' )
    for valor in num:
        print(f'{valor}  ',end='',flush=True)
        sleep(0.5)
        if cont == 0 :
            maior=maior
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo . ')
    print(f'O maior valor inforado foi {maior}.')


maior(2,5,1,7)
maior(4,7,89,2,4)
maior(4,1,6,0,2)
