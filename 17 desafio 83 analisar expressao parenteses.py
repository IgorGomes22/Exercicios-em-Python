#desafio 83
#digite uma expressao que use parentese
#  aplicativo devera analisar se a expressao esta  com parentese fechado e aberto

expr = str(input('Digite a expresao :'))
pilha = []

for simb in expr :
    if simb == '(' :
        pilha.append('(')
    elif simb == ')' :
        if len(pilha) > 0 :
            pilha.pop()
        else :
            pilha.append(')')
            break
if len(pilha)== 0 :
    print('Sua expressao é valida')
else :
    print('Sua expressao é inválida')
