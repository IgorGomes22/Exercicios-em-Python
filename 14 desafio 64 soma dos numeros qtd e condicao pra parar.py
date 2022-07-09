#desafio
# ler varios numeros, mostrar soma de todos , e quantos numeros foi digitado
# e o programa se encerra quando digita 999

count =0
soma =0
set =1
while  set==1 :
    n1 =int(input('Digite algum numero  :'))
    if n1 != 999 :
        count += 1
        soma = soma+n1
    if n1 ==999 :
        print(' Foram digitados {} numeros, e a soma de todos foi {}'.format(count,soma))
        count=0
        soma=0
print('============FIM=============')
