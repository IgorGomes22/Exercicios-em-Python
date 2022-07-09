#desafio 32
#erifica se o ano é bissesto ou nao


from calendar import isleap

print('-----Voce vai saber se o ano é bissesto-----')

ano =int(input('Digite o ano : '))

if isleap(ano):
         print('O ano  {} È bissesto'.format(ano))
else :
        print('O ano  {} não é bissesto'.format(ano))
