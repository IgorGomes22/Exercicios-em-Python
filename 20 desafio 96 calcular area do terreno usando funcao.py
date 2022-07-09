#DESAFIO 96
#CALCULAR AREA DE UM TERRENO

def area(largura,comprimento):
    valor = largura*comprimento
    print(f'A area do terreno {largura}x{comprimento} é {valor} m2.')


print('::::'*10)
print('======== CONTROLE DE TERRENO ==========')
l = float(input('Digite a largura  (m) : '))
c = float(input('Digite o comprimento (m) : '))
area(l,c)
