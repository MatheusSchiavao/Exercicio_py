i = 1 

while i < 11:
    n = (input('Insira seu nome: '))
    v = float(input('Insira o valor das suas compras no ano passado: '))
    if v < 1000:
        print('Bônus de 10% nas compras!')
    else:
        print('Bônus de 15% nas compras!')