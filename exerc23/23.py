import os

numeros = [0,0,0]

numeros[0] = float(input('Digite o numero 1: '))
numeros[1] = float(input('Digite o numero 2: '))
numeros[2] = float(input('Digite o numero 3: '))

print(f'o maior valor entre os três é: {max(numeros)}')

os.system('pause')