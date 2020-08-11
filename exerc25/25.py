import os

produto1 = float(input('Digite o preço do produto 1: '))
produto2 = float(input('Digite o preço do produto 2: '))
produto3 = float(input('Digite o preço do produto 3: '))

produto = [produto1,produto2,produto3]

print(f'Compre o produto com o preço R${min(produto)}')

os.system('pause')