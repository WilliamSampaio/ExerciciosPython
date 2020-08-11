import os

np1 = float(input('digite NP1: '))

while np1 < 0 or np1 > 10:
    print('NP1 inválida!')
    np1 = float(input('digite NP1: '))

np2 = float(input('digite NP2: '))

while (np2 < 0 or np2 > 10):
    print('NP2 inválida!')
    np2 = float(input('digite NP2: '))

media = (np1 + np2) / 2

if media >= 7:
    print(f'MÉDIA SEMESTRAL: {media} - PARABÉNS! Você foi aprovado')
else:
    print(f'MÉDIA SEMESTRAL: {media} - Você foi reprovado! Estude mais')

os.system("pause")
