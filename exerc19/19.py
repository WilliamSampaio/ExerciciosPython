import os

num = float(input('Digite um valor: '))

if num == 0:
    print('zero é neutro')
elif num > 0:
    print(f'{num} é positivo')
else:
    print(f'{num} é negativo')

os.system("pause")
