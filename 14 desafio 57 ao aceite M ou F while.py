#desafio 57
# ler o sexo mas so aceite os valores 'M' ou 'F'. caso esteja errado
#pedir  digiacao novamente

sexo = ' '
set = 's'

while  set =='s' :
    print('===='*11)
    sexo = str(input('Qual o seu sexo  [M / F ]?  ')).upper()
    if sexo == 'M' :
        print('Seu sexo é Masculino ')
    elif sexo == 'F' :
          print('Seu sexo é feminino ')
    else  :
        print('Digite o valor correto')
        set != 's'

