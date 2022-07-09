#desafio 98
#FUNCAO CHAMADA CONTADOR()
#RECEBER 3 PARAMETROS: INICIO,FIM E O PASSO E REALIZA CONTAGEM
#TERA QUE REALIZAR 3 CONTAGENS ATRAVES DA FUNCAO
#A) DE 1 ATE 10,DE 1 EM 1
#B) DE 10 ATE 0,DE 2 EM 2
#C)UMA CONTAGEM PERSONALIZADA
from time import sleep

def contador(i,f,p):
    if p < 0 :
        p*= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont=i
        while cont <=f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >=f :
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont-= p
        print('FIM!')
contador(1,10,1)
contador(10,1,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio : '))
fim = int(input('Fim : '))
pas = int(input('Passo : '))
contador(ini,fim,pas)
