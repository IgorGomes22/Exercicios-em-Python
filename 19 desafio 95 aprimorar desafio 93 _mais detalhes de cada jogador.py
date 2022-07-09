#desafio 95
#aprimorar desafio 93
#funcionar com varios jogadores
#incluir sistema de visualização de detalhes do aproveitamento de cada um
time = list()
partidas=list()
jogador=dict()
while True:
    jogador.clear()
    jogador['nome'] = str(input('>>Nome do jogador: '))
    tot = int(input('>>Quantas partidas o {} jogou?'.format(jogador['nome'])))
    for c in range(0,tot):
        partidas.append(int(input(f'  Quantos Gols na partida {c+1} ?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('>>Quer continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas Sou N')
    if resp == 'N':
        break
    
print('-='*20)
print('cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}' ,end='')
print()

for k,v in enumerate(time):
    print(f'{k:>2} ',end='')
    for d in v.values():
        print(f' {str(d):<15}',end='')
    print()
print('---'*20)
while True:
    busca = int(input('Mostar dados de qual jogador? [999 = sair] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO  DO JOGADOR    {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
print('==='*10)
print('<< VOLTE SEMPRE >>')


                
        
