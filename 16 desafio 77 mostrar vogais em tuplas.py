#desafio 77
#mostrar vogais das palavras na tupla

palavras =('abacate','casa','carro','computador')
print('===========SEPARANDO AS VOGAIS DAS PALAVRAS ===========')
for p in palavras :
    print(f'\nNa palavra {p.upper()} temos AS vogais : ',end='')
    for letra in p :
        if letra.lower() in 'aeiou' :
            print(letra, end='')
