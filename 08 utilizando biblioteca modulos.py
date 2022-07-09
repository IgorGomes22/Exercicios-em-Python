#        import doces     (bala,pudim,mel,pirulito,chocolate,etc...//importa toda a biblioteca
#        from doces import pudim    //importa somente o necessario
#        ceil arredonda pra cima/floor pra baixo
#        floor arredonda pra baixo
#       randm gera numero aleatorio

import  math
import random
num2 = random.randint(1,10)
print(num2)


num = int(input('Digite um numero:   '))
raiz = math.sqrt(num)                                                        
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))    
