import os

numeros = []

maior = 0

for num in range(0,5):
    numeros.append(float(input(f'digite o numero {num + 1}: ')))
    if num == 0:
        maior = numeros[num]
    else:
        if numeros[num] > maior:
            maior = numeros[num]
            
print(f'maior numero digitado: {maior}')

os.system("pause")
