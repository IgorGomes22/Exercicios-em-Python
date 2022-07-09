#desafio 89
#nome e duas notas de varios alunos/guardar em uma lista
#mostrar boletim contendo a media de cada um e permitindo
#que o usuario possa mostrar as notas de cada aluno individualmente

ficha = list()
while True:
    nome =str(input('Nome :     '))
    nota1 = float(input('Nota 1 :    '))
    nota2 = float(input('Nota2 :    '))
    media = (nota1 + nota2 ) /2
#posicao da lista> [nome = 0 ,[nota=1].media = 2]
    ficha.append( [nome, [nota1 , nota2] ,media])
    resp = str(input('Quer continuar ? [S/N] :'))
    if resp in 'Nn' :
        break
print('-=='*10)
print(f'{"No.  ":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)

for i , a in  enumerate(ficha) :
    print(f'{i:<8}{a[0]:<12}{a[2]:>8.1f} ')
while True :
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno ? (999 interrompe) :'))
    if opc == 999:
         print('Finalizando...')
         break
    if opc <=len(ficha) - 1 :
        print(f'Notas de  {ficha[opc][0]} são {ficha[opc][1]}')
    
