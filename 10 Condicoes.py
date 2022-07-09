#aula 10 condicao
# versao simplificada   print('Carro novo'  if tempo <3 else 'Carro velho')


nome=str(input('Qual é o seu nome?  '))
if nome == 'Igor':
    print('Que nome lindo você tem ')
print('Bom dia , {}! '.format(nome))

n1 = float(input('Digite a primeira nota:  '))
n2 = float(input('Digite a segunda nota:  '))
media = (n1 +n2 )/2
print ('A sua média foi {:.1f} ' .format(media))
if media >=6.0 :
    print('Sua média foi Boa')
else:
    print('Sua média foi ruim')
