import os

n1 = float(input('NOTA 1: '))
n2 = float(input('NOTA 2: '))
n3 = float(input('NOTA 3: '))
n4 = float(input('NOTA 4: '))

media = (n1 + (n2 * 2) + (n3 * 3) + n4) / 7

print(f'Média: {round(media, 2)}')

os.system('pause')