import os

nota1 = float(input('digite a 1ª nota bimestral: '))

while nota1 < 0 or nota1 > 10:
    print('nota inválida!')
    nota1 = float(input('digite a 1ª nota bimestral: '))

nota2 = float(input('digite a 2ª nota bimestral: '))

while (nota2 < 0 or nota2 > 10):
    print('nota inválida!')
    nota2 = float(input('digite a 2ª nota bimestral: '))

nota3 = float(input('digite a 3ª nota bimestral: '))

while (nota3 < 0 or nota3 > 10):
    print('nota inválida!')
    nota3 = float(input('digite a 2ª nota bimestral: '))

nota4 = float(input('digite a 4ª nota bimestral: '))

while (nota4 < 0 or nota4 > 10):
    print('nota inválida!')
    nota4 = float(input('digite a 4ª nota bimestral: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'MÉDIA: {round(media, 2)}')

os.system("pause")
