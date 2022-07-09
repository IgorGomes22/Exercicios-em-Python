#desafio 41
#confederacao nacional de nataçao
#ler ano de nascimento de um atleta e mostrar sua categoria de acordo com a idade
# ate 9 anos:mirim /ate 14 infantil/ ate 19 junior /ate 20 senior /acima de 20 Master

print('=======Olá vamos analisar os perfis dos atletas==========')
ano = int(input('Ano de nascimento do atleta : ' ))

idade = 2022 - ano

if idade <= 9 :
    print('{} anos : categoria Mirim'.format(idade))
elif idade  >9 and idade <=14 :
    print('{} anos : categoria infantil'.format(idade))
elif idade  >14 and idade <=19 :
    print('{} anos : categoria Junior'.format(idade))
elif idade == 20 :
    print('{} anos : categoria Senior'.format(idade))
elif idade > 20 :
    print('{} anos : categoria Master'.format(idade))
