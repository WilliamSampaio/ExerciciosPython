import os

num = int(input('Digite um numero entre 1 a 7: '))

while num < 1 or num > 7:
    print('numero inválido!')
    num = int(input('um numero: '))

if num == 1:
    print(f'{num} - Domingo')
elif num == 2:
    print(f'{num} - Segunda-feira')
elif num == 3:
    print(f'{num} - Terça-feira')
elif num == 4:
    print(f'{num} - Quarta-feira')
elif num == 5:
    print(f'{num} - Quinta-feira')
elif num == 6:
    print(f'{num} - Sexta-feira')
else:
    print(f'{num} - Sabado')

os.system("pause")
