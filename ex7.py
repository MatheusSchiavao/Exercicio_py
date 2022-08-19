x = 1
i = 0
tx = 0

print('Finalize o laço ao digitar 0.')
while x != 0:
    x =  int(input('Insira sua idade: '))
    if x != 0:
        tx += x
        i += 1
    elif x == 0:
        break
media = tx/i 
print('Média de idades: ',media)