 #desafio 29 radar
#programa ler a velociade de um carro,se ultrapassar 80km
# mostrar um aviso, A multa vai custar 7 reais por cada km acima do limite

print('-----RADAR limite 80km-----')

km_limite = 80
multa = float( 7)

velocidade = int(input('Digite a sua velocidade:  '))
print('O limite é {} km, e voce passou a {} km'.format(km_limite,velocidade))
                       
valor = (( velocidade - km_limite)*multa)
if velocidade < km_limite :
                       print('Parabens,voce esta dirigindo dentro do limite')
else :
        print('Voce foi multado e o valor da multa é : R${:.2f} reais'.format(valor))
