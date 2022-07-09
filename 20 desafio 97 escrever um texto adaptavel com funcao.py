#DESAFIO 97
#CRIAR FUNÇAO CHAMADO ESCREVA()
#COM TAMANHO ADAPTAVEL

def escreva(txt):
    print('='*len(txt))
    print(txt)
    print('='*len(txt))

e = str(input('Escreva uma frase :> '))
escreva(e)
