#desafio 71
# funcionamento de caixa eletronico
#qual sera o valor sacado/
#programa ira informar quantas cedulas de cada valor serao entregues
#notas de 50,20,10 e 1 real

print('***'*30)
print('{:-^70}'.format(' CAIXA ELETRÔNICO '))    #CENTRALIZA O TEXTO NO MEIO,ESPACO DE 30 CARACTERES
print('***'*30)

valor = int(input('Qual o valor deseja sacar?  R$ '))

cedula = 100
montante = valor
cont = 0

while True :
    if montante >= cedula :
       montante -= cedula
       cont += 1
    else :
        if cont > 0 :
            print(f'Voce receberá {cont} cedulas de R$ {cedula} ')
        if cedula == 100 :
                  cedula = 50
        elif cedula == 50 :
                  cedula = 20
        elif cedula == 20 :
                  cedula = 10
        elif cedula == 10 :
                  cedula = 5
        elif cedula == 5 :
                  cedula = 1
        cont = 0
        if montante == 0 :
            break
print('{:-^80}'.format(' VOLTE SEMPRE ! '))
