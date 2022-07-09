#aula 19 DICIONÁRIOS
#tuplas=()
#listas= []
#dicionarios = {}

filmes=dict()
filmes={'nome' :  'Velozes e Furiosos' , 'ano': 2020,'duracao' : 2}
print(filmes['nome'])
print(filmes['ano'])
print(filmes['duracao'])
#---------------------------------
#Adicionar em um dicionario
filmes['classificacao'] = '5 estrelas'
print(filmes)
#---------------------------------
#Obter valores,keys ou tudo
print(filmes.values())
print(filmes.keys())
print(filmes.items())
#---------------------------------
for k,v in filmes.items():
    print(f'O { k} é {v}')
#---------------------------------
#forma de buscar as chaves (keys) /aspas duplas nas keys pois o
print('-----'*10)
print(f' O  {filmes["nome"]} tem {filmes["duracao"]}  horas')
print(filmes.keys())
#substituir
filmes['ano']= 2000
for k,v in filmes.items():
    print(f' {k} = {v}')
#Remover elemento
del filmes['classificacao']
#---------------------------------
#dentro de uma lista
brasil = []
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf ': 'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil[1])
print(brasil[1] ['sigla'])
#------------------------------------
#dicionario dentro de listas
carros = list()
marca = dict()
for c in range(0,3):
    marca['toyota'] = str(input('Digite um carro a Toyota : '))
    marca['ano'] = int(input('Digite o ano : '))
    carros.append(marca.copy())
for e in carros:
    for k,v in e.items():
        print(f' O campo  {k} é  {v} ')






