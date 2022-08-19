a=int(input('Insira o ano do seu nascimento:'))
i=2022-a

if i >= 18:
    print('Possui idade para votar e ter CNH.')
elif i >= 16 and i <=17:
    print('Possui idade para votar. Não pode ter CNH.')
else:
    print('Não possui idade para votar e nem ter CNH.')