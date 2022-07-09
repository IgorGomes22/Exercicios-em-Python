# curso 20  funçoes

def linha():
    print('---'*10)

linha()
print('  igor')
linha()
#-----------------------------------
def mensagem(txt):
    print('------------------')
    print(txt)
    print('------------------')

mensagem('  igor gomes pereira  ')
mensagem('       30 anos        ')
mensagem('       casado         ')
#------------------------------------
def soma(a,b):
    s = a + b
    print(s)
 
soma(4,7)
soma(3,6)
soma(2,3)
#-------------------------------------
#soma varios parametros /tuplas()
def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')
   
contador(2,1,7)
contador(3,5,9)
contador(1,2)
#--------------------------------------
#valores em uma lista[]
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos] *=2
        pos+=1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)
print('---'*10)
#----------------------------------------
# desempacotamento
def soma(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')
    
soma(5,2)
soma(3,5,1)
print('---'*10)





