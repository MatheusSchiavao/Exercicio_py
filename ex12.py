n=int(input('Insira sua nota (valor inteiro):'))

if n<3:
    print('Conceito E')
elif n>=3 and n<=5:
    print('Conceito D')
elif n>=6 and n<=7:
    print('Conceito C')
elif n>=8 and n<=9:
    print('Conceito B')
else: 
    print('Conceito A')