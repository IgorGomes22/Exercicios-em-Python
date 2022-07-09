#desafio 34
#vlor de aumento do salario > que 1.250 + 10%
#menor ou igual a 1.250 +15%

print('-----Olá, vamos calcular o valor do aumento do seu salario -----')

salario = float(input('Informe o seu salário : R$ '))

dez = salario * 0.10
quinze = salario * 0.15

if salario >1250.0:
    print('Seu aumento será de 10%,seu  salário aumentará  R${:.2f}'.format( dez))
    print('Passará a ser R$ {:.2f}'.format(dez+salario))
else:
    print('Seu aumento será de 15%,seu  salário aumentará R${:.2f}'.format( quinze))
    print('Passará a ser R$ {:.2f}'.format(quinze+salario))
