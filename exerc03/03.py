import os

pesoCarne = float(input('Digite o peso da carne em Kg: '))
precoPorKg = float(input('Digite o preço por Kg: R$'))
icms = (pesoCarne * precoPorKg) * 0.17
totalAPagar = (pesoCarne * precoPorKg) + icms

print(f'total a pagar: R${round(totalAPagar, 2)}')
print(f'- ICMS: R${round(icms, 2)}')
print(f'= Liquido: R${round((totalAPagar - icms), 2)}')

os.system('pause')