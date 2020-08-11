import os

catetoAd = float(input("Cateto Adjacente: "))
catetoOp = float(input("Cateto Oposto:    "))

hipotenusa = (catetoAd ** 2 + catetoOp ** 2) ** (1 / 2)

print(f'Hipotenusa: {hipotenusa}')

os.system('pause')