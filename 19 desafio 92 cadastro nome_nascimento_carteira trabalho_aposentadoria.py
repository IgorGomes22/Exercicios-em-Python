#desafio 92
#ler nome, ano nascimento,carteira de trabalho,cadastrar com idade
#se CTPS(carteira de trabalho) for diferente de zero
#receber o ano da contratacao e o salario
#calculare acrescentar alem da idade com quantos anos a pessoa vai aposentar >=35 anos
from datetime import datetime

dados = dict()
anoatual = 2022

trabalho = 35

dados['nome']= str(input('Nome : '))
dados['nascimento'] = int(input('Ano Nascimento :'))
dados['ctps'] = int(input('Carteira de trabalho:      /(0 não tem) '))
dados['idade'] = datetime.now().year  - dados['nascimento']

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação :  '))
    dados['salario'] = float(input('Salário : '))
    dados['Idade aposentadoria'] = ((dados['contratacao'] + trabalho)- dados['nascimento'])

print('========== Dados do Usuário ===========')                                  
print(f'> Nome: :{dados["nome"]}')
print('> Idade : {}'.format(dados['idade']))
print(f'> Nascimento :{dados["nascimento"]}')
if dados['ctps'] != 0 :
    print('> CTPS : {}'.format(dados['ctps']))
    print('> Salário : R${:.2f} '.format(dados['salario']))
    print('> Na sua aposentadoria voce tera {} anos'.format(dados['Idade aposentadoria']))
print('===='*10)
for k,v  in dados.items():
    print(f' > {k} = {v}')
