#desafio 101
#funcao chamada voto()
#receber parametro o ano de nascimento
#retornar um valor literal
#indicando se vota,nao vota,opcional,obrigatorio
from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano
    if idade < 18:
        print(f'Com {idade} anos voce não pode votar')
    elif idade >=18 and idade <=65 :
        print(f'Com {idade} anos seu voto é obrigatório')
    else:
        print(f'Com {idade} anos seu voto é opcional')
print('%%%%'*10)
anonascimento=int(input('Em que ano voce nasceu ? '))
voto(anonascimento)
