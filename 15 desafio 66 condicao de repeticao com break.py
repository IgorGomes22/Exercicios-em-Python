#desafio 66
#ler varios numeros o programa so para quando digitado 999.
#no final mostra quantos numeros foram digitados
#e mostar a soma deles

count =0
soma=0

while True:
    n1 =int(input('Digite um numero (999 para parar): '))
    if n1 != 999 :
        count +=1
        soma = soma+ n1
    else :
        break
print(f' voce diitou {count} numeros e a soma de todos é :{soma}')
count =0
soma=0
