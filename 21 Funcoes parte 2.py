# funcoes parte 2
#
#define  os parametros como 0,caso o 
def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(5,2)
somar(9)
print('---'*10)
#-------------------------------------------------------------
#variAVEIS LOCAIS E GLOBAIS
def local(b):
    global a  #a variavel global passa a valer 8
    a = 8
    b +=  50      #peg o valor passado ara o parametro e soma
    print(f' A variavel a vale {a}')
    print(f'Variavel local vale {b}')

a = 2       #variavel global
local(a)    #passa o valor da para o parametro
print(f'A variavel global vale {a}')
#------------------------------------------------------------
print('---'*10)
#utilizando (return) para mandar o resultado
def soma(a=0,b=0,c=0):
    s =a+b+c
    return s

r1 = soma(3,2,5)
r2 = soma(1,7)
r3 = soma(4)
resp = soma(3,2,5)
print(resp)
print(f'Meus cálculos deram {r1},{r2},{r3}.')
#------------------------------------------------------------
print('---'*10)
#
def fatorial(num=1):
    f = 1
    for c in range(num,0, -1):
        f *= c
        return f
n = int(input('Digie um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

#------------------------------------------------------------
print('---'*10)
def contador(a,b,c):
    p= a
    while p <=b:
        print(f'{p}',end='...')
        p += c
contador(0,10,2)
#------------------------------------------------------------









