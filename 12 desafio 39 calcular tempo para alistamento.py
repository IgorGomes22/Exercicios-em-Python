#desafio 39
#ler ano de nascimento e informar:
#ainda vai se alistar /é hora de se alistar / ja passou do tempo de alistamento
#informar o tempo que falta ou que ja passou do prazo

print('=======Alistamento Militar========')
anonascimento = int(input('Ano nascimento : '))
anoatual = int(input('Digite o ano atual : '))

valor =  anoatual - anonascimento

if valor < 18 :
    print('falta  {} anospra voce  se alistar'.format(18 - valor ))
elif valor == 18 :
    print('È hora de se alistar' )
elif valor >18 :
    print(' Já passou {} anos do tempo de se alistar'.format(valor - 18))
