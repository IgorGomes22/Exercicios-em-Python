#desafio 102
# funcao fatorial()
#receber 2 parametros:o primeiro indica numero a calcular e o outro
#chamado show,que sera um valor logico(opcional)
#indicando sera mostrado ou nao a tela de processo do calculo fatorial

def fatorial(num=1,show=0):
    f = 1
    for c in range(num,0,-1):
        if show:
            print(c,end='')
            if c >1:
                print(' x ', end='')
            else:
                print(' = ',end='')
   
        f *= c
    return f
        
n = int(input('Digite um numero: '))
resp = int(input('Deseja mostrar todo calculo? [1 sim / 0 não]'))
print(fatorial(n,resp))
