#desafio 37
#ler numero inteiro qualquer / o usuario escolhe qual sera a base de conversao
#  1 binario / 2 octal  / 3 hexadecimal

set =1
while set ==1 :
    valor = int(input('Digite o numero inteiro'))
    print("""Escolha a opção de conversão abaixo :
       1) Binario
       2) Octal
       3) Hexadecimal
    """)
    opcao=int(input('Digite a opção :'))
    if opcao == 1 :
        binary = format(valor,"b")
        print(' o numero {} em binario é : {}'.format(valor,binary))
    elif opcao == 2 :
        octal = format(valor,"o")
        print('O numero {} em Octal é : {}'.format(valor,octal))
    elif opcao == 3:
        hexa = format(valor,"x")
        print('O numero {} em Hexa é : {}'.format(valor,hexa))
