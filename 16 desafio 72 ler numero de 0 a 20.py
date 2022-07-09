#desafio 16
#criar um programa que tenha uma tupla preenchida com extensao
#de zero ate vinte
#digitar numero pelo teclado e mostrar a extensao

cont = ('zero','um','dois','tres','qutro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True :
    num = int(input('Digite um numero entre 0 e 20:  '))
    if 0<= num <= 20 :
        break
    print('tente novamente . ', end=' ')
print(f'voce digitou o numero  {cont[num]}')
