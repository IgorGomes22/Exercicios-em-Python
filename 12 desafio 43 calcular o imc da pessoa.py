#desafio 43
#calcular o imc =   Massa(kg) / altura(m)^2 
#ler o peso e a altura da pessoa
#abaixo de 18.5:abaixo do peso
#entre 18.5 e 25: peso ideal
#25 ate 30 sobrepeso
#30 ate 40 obesidade
#acima de 40 obesidade morbita


print('=====vamos calcular o IMC =======')

peso = float(input('Qual o seu peso : '))
altura = float(input('Sua altura : '))

imc = peso / altura**2

if imc < 18.5 :
    print('imc {:.2f} , voce está abaixo do peso '.format(imc))
elif imc >18.5 and imc <25.0 :
    print('imc {:.2f} , voce está com o peso ideal'.format(imc))
elif imc >25.0 and imc < 30.0 :
    print('imc {:.2f} ,ALERTA, com sobrepeso'.format(imc))
elif imc >30.0 and imc < 40.0 :
    print('imc {:.2f} , Cuidado voce está obeso '.format(imc))
elif imc > 40.0 :
    print('imc {:.2f} , PERIGO ,Obesidade mórbita '.format(imc))

idealmax = altura**2 * 25.00
idealmin = altura**2 * 18.5 
print('Para o peso ideal voce deve permanecer entre {:.2f}kg e {:.2f}kg'.format(idealmin,idealmax))

