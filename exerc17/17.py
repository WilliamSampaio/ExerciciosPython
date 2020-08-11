import os
from math import ceil

areaMetrosQuad = float(input('DIGITE A ÁREA EM METROS²: '))

litrosDeTinta = areaMetrosQuad / 3

latasTotal = ceil(litrosDeTinta / 18)

print(f'Área total: {areaMetrosQuad} m²')
print(f'Total de litros: {round(litrosDeTinta, 2)} litros')
print(f'Total de latas: {latasTotal} (R${float(latasTotal * 80)})')


os.system('pause')