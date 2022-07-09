#desafio 31
#se viagem e < que 200km = 0,50 por km
#se viagem > que200 km = 0,45 por km

preco1 = float(0.50)
preco2 = float(0.45)

print('-----Ola ,Vamos calcular o vaor de sua viajem?-----')
distancia = int(input('Digite quantos km tem seu destino :  '))

valorperto = distancia * preco1
valorlonge = distancia* preco2
if  distancia < 200:               
                    print(' voce vai gastar R$ {:.2f} em passagem'.format(valorperto))
else :
                    print(' voce vai gastar R$ {:.2f} em passagem'.format(valorlonge))
