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

if media >= 9:
    print(f'media: {media} (A) APROVADO')
elif media >= 7.5:
    print(f'media: {media} (B) APROVADO')
elif media >= 6:
    print(f'media: {media} (C) APROVADO')
elif media >= 4:
    print(f'media: {media} (D) REPROVADO')
else:
    print(f'media: {media} (E) REPROVADO')

os.system("pause")
