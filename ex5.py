i = 1 
q = 0

while i < 11:
    x = float(input('Insira um valor: '))
    if x >= 30 and x <= 90:
        q += 1
    i += 1
    if i == 10:
        break
print('Quantidade de valores entre 30 e 90: ',q)