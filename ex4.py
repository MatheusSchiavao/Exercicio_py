i = 1 
iddx = 0
midd = 0
cope = 0
malt = 0

while i < 26:
    idd = int(input('Insira sua idade: '))
    alt = int(input('Insira sua altura em cm: '))
    peso = float(input('Insira seu peso: '))
    i += 1
    if idd > 50:
        iddx += 1 
    elif idd >= 10 and idd <=20:
        malt += alt
    if peso < 40:
        cope += 1
    if i == 25:
        break
    mpes = (cope/5)*100
print(f'Quantidade de pessoas com mais de 50 anos: {iddx}')
print(f'Média de altura das pessoas entre 10 e 20 anos: {malt/5}cm')
print(f'Porcentagem de pessoas com peso menor que 40kg: {mpes}%')