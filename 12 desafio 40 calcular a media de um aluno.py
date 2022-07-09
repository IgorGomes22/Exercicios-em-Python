#desafio 40
#ler duas notas de um aluno e calcular sua media
#abaixo de 5.0  reprovado
#entre 5.0 e 6.9 recuperacao
#igual ou acima de 7.0 aprovado

print('========Bem Vindo aluno=========')
n1 = float(input('Digite sua primeira nota :'))
n2 = float(input('Digite sua segunda nota :'))

media = (n1+n2)/2

if media < 5.0 :
    print('REPROVADO, média {}'.format(media))
elif media > 5.0  and  media <  6.9 :
    print(' RECUPERAÇÃO ,média {}'.format(media))
elif media >= 7.0 :
    print('APROVADO , média {} '.format(media))
 
