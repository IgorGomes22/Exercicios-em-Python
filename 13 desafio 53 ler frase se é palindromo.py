#desafio 53
# ler  a frase e dizer se é palindromo
#exem: apos a sopa / a sacada da casa /a torre da derrota

frase =input('Digite uma frase:  ').strip().upper()
palavras = frase.split()
frasejunta ='   '.join(palavras)
inverso = frasejunta[::-1]


if inverso != frasejunta :
    print('A frase : {}  não é um Palindromo,pois '.format(frase))
    print('{} é diferente de {}'.format(frasejunta,inverso))
else :
    print (' A frase :{} é um Palindromo,pois'.format(frase))
    print('{} é igual a {}'.format(frasejunta,inverso))
