#variaveis compostas listas part 2

dados = list()
dados.append('Pedro')    #indice [0]
dados.append(25)            #indice[1]
dados.append('ana')
dados.append(22)

print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])      #colocar lista dentro de lista
print(pessoas)

pessoas=[['saulo',40],['igor',30],['dani',27],['theo',3]]
print(pessoas)
print(pessoas[0][0])

print('========'*10)

# adicionando dados em uma lista dentro de lista
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Igor'
teste[1] = 30
galera.append(teste[:])
print(galera)

print('========'*10)
turma = [['Igor  Gomes ',30],['Daniele Nunes',27],['Théo Gomes Nunes','3 meses']]
for p in turma :
    print(f'nome: {p[0]}  idade: {p[1]} ')
print('========'*10)

#inserir dados digitados
lista = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome:  ')))
    dado.append(int(input('Idade:  ')))
    lista.append(dado[:])
    dado.clear()
print(lista)

# pra saber se é maior de idade
for p in lista :
    if p[1] >= 18 :
        print(f' {p[0]} é maior de idade. ')
    else:
        print(f' {p[0]} é menor de idade. ')
        
print(lista)
    

