#cores no terminal
# \033[0;33;44m
#\033[style;text;background m
print('\033[4;34m   Olá Maria   \033[m ' )

      
nome = 'Igor'
cores = {'limpa' : '\033[m ' , ' azul ' : '\033[34m' , 'amarelo ' : ' \033[33m ' , 'pretoebranco' : '\033[7;30' }
print('Muito Prazr em te conhecer,{}{}{}'.format(cores['pretoebranco'],nome,cores['limpa']))
