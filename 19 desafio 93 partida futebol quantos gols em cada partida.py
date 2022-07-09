#desafio 93
#gerenciar aproveitamento jogador futebol
#nome do jogador.quantas partidas jogou
#qtd gols em cada partida
#total de gols feitos durante campeonato

partidas= list()
jogador = dict()

jogador['nome'] =  str(input('Nome do Jogador : '))
tot = int(input(f' Quantas partidas {jogador["nome"]} jogou  : '))
for c in range(0,tot) :
    partidas.append(int(input(f' quantos gols fez na partida {c+1} : ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=-='*20)
print(jogador)
print('-=-='*10)
     
print(f' => O jogador {jogador["nome"]} fez {jogador["total"]} gols ao total')

for k ,v in enumerate(jogador['gols']):
        print(f' =>no jogo {k+1} fez  {v} gols')

 
