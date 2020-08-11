import os

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite mais um número inteiro: "))
num3 = float(input("Digite um número real: "))

print('- O produto do dobro do primeiro com metade do segundo: ', end=' ')
print(f'{(num1 * 2) * (num2 / 2)}')
print('- A soma do triplo do primeiro com o terceiro:', end=' ')
print(f'{(num1 * 3) + num3}')
print(f'- O terceiro elevado ao cubo: {num3 ** 3}')

os.system('pause')