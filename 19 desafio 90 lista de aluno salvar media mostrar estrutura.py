#desafio 90 dicionarios
#ler nome e media de um aluno,guardando a situacao no dicionario. aprovado reprovado
#no final mostrar conteudo da estrutura na tela

dados=dict()

dados['nome']=str(input('Nome do aluno : '))
dados['media']=float(input('Sua média :'))

if dados['media'] >= 7.0 :
    dados['status'] = 'APROVADO'
elif  5<= dados['media'] <7 :
    dados['status']= 'RECUPERAÇÃO'
else: dados['status'] = 'REPROVADO'

print(f' O aluno {dados["nome"]} , está {dados["status"]} com a média de {dados["media"]} ')
