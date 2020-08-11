import os

numeros = [0,0]

numeros[0] = float(input('Digite o numero 1: '))
numeros[1] = float(input('Digite o numero 2: '))

print(f'o maior valor entre os dois é: {max(numeros)}')

os.system('pause')