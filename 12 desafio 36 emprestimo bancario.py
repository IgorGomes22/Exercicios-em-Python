#desafio 36
#emprestimo bancario
#Aprovar o emprestimo para compra da casa
#Perguntar o valor da casa /O salario /quantos anos deseja pagar
#calcular o valor da prestacao mensal,nao pode exceder 30% do salario

print('==============Banco de Empréstimo=================')
print('Olá Vamos começar preenchendo alguns dados ')
nome = ('Seu nome : ')
salario = int(input('Seu salário : '))
preco_imovel = int(input('O valor do imóvel que deseja comprar : '))
tempoAno = int(input('Em quantos anos deseja pagar : '))

tempoMes = tempoAno *12
valorprestacao = preco_imovel / tempoMes
investimento = salario*0.30

if valorprestacao <= investimento:
 print('Prazo de {}  meses'.format(tempoMes))
 print('Prestacao de R$ {:.2f} '.format(valorprestacao))
 print('Você irá gastar 30% do seu salario R$ {:.2f}  '.format(investimento))
 print('=============Empréstimo Aprovado pelo nosso banco,Parabéns=========')
else:
        print('Prazo de {}  meses'.format(tempoMes))
        print('Prestacao de R$ {:.2f} '.format(valorprestacao))
        print('Dinheiro para prestação, 30% do seu salario R$ {:.2f}  '.format(investimento))
        print('Infelizmente o Empréstimo foi Reprovado pelo')
        print('nosso banco,pois o valor da prestacao ultrapassa o limite de 30%')
