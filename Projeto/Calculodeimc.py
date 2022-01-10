print('------------- \033[1;34mCÁLCULO DE IMC\033[m -------------')
peso = float(input('Qual o seu peso (kg) ?  '))
altura = float(input('Qual a sua altura (m) ?  '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('Você está abaixo do peso, seu IMC é {:.1f}'.format(imc))
elif 25 > imc >= 18.5:
    print('Você está no peso ideal, seu IMC é {:.1f}'.format(imc))
elif 30 > imc >= 25:
    print('Você está sobrepeso, seu IMC é {:.1f}'.format(imc))
elif 40 >= imc >= 30:
    print('Você está obeso, seu IMC é {:.1f}'.format(imc))
else:
    print('Você está em Obesidade mórbida, seu IMC é {:.1f}'.format(imc))
