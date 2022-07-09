#desafio 69
#cadastro de pessoas
# idade,sexo , quer continuar? se nao mostrar
# a)qts pessoas tem mais de 18 anos /b)qts homens cadastrados /c)qts mulheres menos de 20

auxidade = 0
maiores = 0
homens = 0
escolha =' '
contm = 0
print('****'*22)
print('                                                      CADASTRO DE PESSOAS')
print('****'*22)
while True :
    idade = int(input('Idade : '))
    sexo = ' ' 
    
    while sexo not in 'MF' :
        sexo = str(input('Sexo : [M / F]')).strip().upper()[0]  
    if idade >= 18 :
        maiores += 1 
    if  sexo == 'M'  :
            homens = homens + 1
    if idade < 20 and sexo == 'F' :
            contm = contm + 1
    print(f'****'*22)
    continuar = ' ' 
    while continuar not in 'SN' :
            continuar=str(input('Quer continuar?  [S / N]' )).strip().upper()[0]
    if continuar =='N' :
        break
print(f'----'*20)
print(f' Cadastrados mais de 18 anos : {maiores}  ')
print(f' Total de homens cadastrados : {homens}')
print(f' Mulheres menos de 20 anos : {contm} ')

    
    
    
