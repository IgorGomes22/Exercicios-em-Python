# ESTRUTURA DE REPETIÇÃO
from time import sleep

# conta de 0  6 crescente
for   c in range(0,4):
    print('{} Igor gomes '.format(c)) 
    sleep(1)
print('fim')

#conta ed 6 a 0 decrescente
for b in range(4, 0 ,-1):
    print(b)
    sleep(1)
print('final')

#conta de 0 a 6 pulando de dois em dois
for a in range (0,4,2):
  print(a)
  sleep(1)
print('FIM')

#usando um numero de entrada

n =int(input('Digite um numero'))
for d in range(0,n,):
 print(d)
 sleep(1)
print('FiM')

#somatorio
resp=0
for e in range(0,3):
    valor=int(input('digite o numero:  '))
    resp += valor
print('O somatorio é  :{}'.format(resp))




  
