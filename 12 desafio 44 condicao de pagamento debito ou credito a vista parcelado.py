#desafio 44
# calcular valor a ser pago em um produto
# 1 )a vista dinheiro/cheque: 10% desaconto
# 2 )Debito 5% desconto
# 3 )ate 2x no cartao preco normal
# 4 )3x ou mais 20% de juros

from time import sleep
print('===== Vamos calcular os descontos e juros de um produto =====')
valor = int(input('Insira o valor do produto : '))
opcao=0
while opcao != 6 :     
    print(""" Segue as opções de pagamento: 
           1)  A vista 10% desconto   
          2) Debito 5% de desconto
          3) 2x no cartão sem juros
          4) 3x  com 20% de juros
          5) inserir novo valor
          6) Fechar programa""")
    opcao = int(input('Digite uma opção: '))

    if opcao == 1 :
                  produto = valor*0.10
                  preco = valor - produto
                  print(' O valor com desconto  é : R${:.2f} '.format(preco))
                  
    elif opcao == 2 :
            produto = valor * 0.05
            preco = valor - produto
            print('O valor no débito é  : R${:.2f} '.format(preco))
            
    elif  opcao == 3 :
            produto = valor / 2
            preco = valor
            print('O valor 2x no cartão sem juros é :{:.2f} , prestacao de :R${:.2f}'.format(preco,produto))
            
    elif opcao == 4 :
            produto = valor *0.20
            preco = valor + produto
            div3 = preco /3
            print('O valor 3x no cartão com 20% juros é : {:.2f} , parcelas R${:.2f}'.format(preco ,div3 ))
            
    elif opcao == 5 :
             valor =int(input('Informe o novo valor :'))
             
    elif opcao == 6 :
            print('Finalizando...')

    else :
        print('Opção invalida')
    print('===' * 10)
              
    sleep(2)   
print('============Fim do programa============')
                  
            
    
