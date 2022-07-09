#desafio 105
#funcao notas()
#receber varios alunos e retornar um dicionario:
#qtd notas/maior nota/menor nota/media da turma/situacao opcional

def notas(*n, sit=False):
    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor'] = min(n)
    r ['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >=7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] ='RUIM'
    return r

resp = notas(5.2,7.5,1,1,sit=True)
print(resp)
help(notas)
