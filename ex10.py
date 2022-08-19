altura=float(input('Informe sua altura em metros:'))
peso=float(input('Informe seu peso:'))
imc=peso/(altura*altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso normal')
elif imc >= 25 and imc <= 30:
    print('Acima do peso')
else:
    print('Obeso')