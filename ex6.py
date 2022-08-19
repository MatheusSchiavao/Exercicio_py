i = 0
midade = 0 
qntd = 0 
prct = 0 

while i < 10:
    idade = int(input('Insira sua idade: '))
    altura = int(input('Insira sua altura: '))
    peso = float(input('Insira seu peso: '))
    midade += idade
    i += 1
    if peso > 90 and altura < 150:
        qntd += 1
    if idade >= 10 and idade <= 30 and altura > 190:
        prct += 1
    if i == 10:
        break 
print('Média de idade: ',midade/10)
print('Pessoas com peso maior que 90kg com menos de 1,50m: ',qntd)
print('Porcentagem de pessoas entre 10 e 30 anos com mais de 1,90m: ',(prct/10)*100)