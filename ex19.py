n1=float(input('Insira um valor:'))
n2=float(input('Insira um valor:'))

print('Selecione uma opção:')
print('1 - Adição        | 2 - Subtração')
print('3 - Multiplicação | 4 - Divisão')
o=float(input())

if o == 1:
    print(n1+n2)
elif o == 2:
    print(n1-n2)
elif o == 3:
    print(n1*n2)
elif o == 4:
    print(n1/n2)
else:
    print('Opção inválida!')

