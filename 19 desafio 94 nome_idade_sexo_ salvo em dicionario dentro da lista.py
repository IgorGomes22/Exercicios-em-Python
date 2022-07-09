#desafio 94
#nome , sexo , idade , /dados de cada pessoa em um dicionario.
#e todos os dicionarios em uma lista.
#mostrar quantas pessoas foram cadastradas
# a media de idade do grupo
#uma lista com todas as mulheres
#lista com todas as pessoas com idade acima da media

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:  [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF' :
            break
        print('ERRO! Por favor dgite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    
    while True:
        resp = str(input('Quer continuar ?  [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if resp == 'N': 
        break
print('-='*20)
print('Ao todo foram cadastradas {} pessoas'.format(len(galera)))
media = soma/len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram :', end='')
for p in galera :
    if p['sexo'] in 'Ff' :
        print(f'{p["nome"]} , ',end='')
print()
print(f'As pessoas que estão com a idade acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<<<<<<<ENCERRADO>>>>>>')



