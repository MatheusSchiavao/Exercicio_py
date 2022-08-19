i = 0
t = 0

while i < 5:
    a = float(input('Insira um valor: '))
    i += 1
    if a < 0:
        t += 1
    if i == 5:
        break
print('Quantidade de valores negativos: ',t)