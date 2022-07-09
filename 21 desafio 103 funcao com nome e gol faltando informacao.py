#desafio 103
#funcao chamada ficha(), receba 2 parametros
#o nome de um jogador e quantos gols le marcou
# devera ser capaz de mostrar a ficha mesmo fltando algum dado

def ficha(nome='<Desconhecido>',gol=0):
    print(f'O jogador {nome} fez {gol} gols')


nome=str(input('Nome jogador:  ' ))
gol=str(input('Quantos gols ? '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() =='':
    ficha(gol=gol)
else:
    ficha(nome,gol)
