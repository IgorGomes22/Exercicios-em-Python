print("""Olá seja bm vindo para aprender sobre manipulação de textos
que aprenderemos a seguir alguns passos do que essa linguagem é capaz
a nossa frase que vamos manipular é Ig Automação""")


frase = ('Ig Automação')


len(frase)
print(' - Essa frase tem  ',len(frase), '  caracteres')
print(' - A primeira letra é  ' ,frase[0] , ' E a ultima letra é  ' ,frase[-1] )
print(' - Pulando de 2 em 2 será:  ',frase[::2])
frase = frase.replace('Automação' , 'Python')
print(' - Substituindo uma palavra ficará : ',frase)
