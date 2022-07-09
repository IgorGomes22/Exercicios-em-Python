#desafio 59
# input 2 valores e mostre um menu
#1 somar/2 multiplicar /3 maior /4 novos numeros /5 sair do programa

n1  = int(input('Digite o primeiro valor'))
n2 = int(input('Digite segundo valor'))
opcao = 0
soma = 0
set = 1
while set ==1 :
    print('===='*2)
    print(""" [1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa""")
    
    opcao = int(input('>>>>>escolha uma opcao   :'))
    if opcao == 1 :
        soma = n1+n2
        print('A soma de {} e {}  é igual a {}'.format(n1,n2,soma))
    if opcao == 2 :
        soma = n1* n2
        print('A multiplicacao de {} e {}  é igual a {}'.format(n1,n2,soma))
    if opcao == 3 :
        if n1>n2 :
            print(' {} é maior que {}'.format(n1,n2))
        else :
            print(' {} é maior que {}'.format(n2,n1))
    if opcao == 4 :
        n1  = int(input('Digite o primeiro valor'))
        n2 = int(input('Digite segundo valor'))
    if opcao ==5 :
         print('================ FIM ================')
         set =0
set=0
