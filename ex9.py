v = 1 
n = 0
total = 0
pstv = 0
ngtv = 0 
print('Digite 0 para encerrar.')
while v != 0:
    v = int(input('Insira um valor:'))
    if v != 0:
        total += v 
        n += 1
        if v > 0:
            pstv += 1
        elif v < 0:
            ngtv += 1
        elif v == 0:
            break
print('Média dos valores:',total/n)
print('Quantidade de valores positivos:',pstv)
print('Quantidade de valores negativos:',ngtv)
print('Percentual de valores positivos:',(pstv/n)*100)
print('Percentual de valores negativos:',(ngtv/n)*100)