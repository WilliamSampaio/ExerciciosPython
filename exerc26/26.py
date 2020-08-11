import os

num1 = float(input('digite o numero 1: '))
num2 = float(input('digite o numero 2: '))
num3 = float(input('digite o numero 3: '))

num=[num1,num2,num3]

print(*sorted(num,reverse=True), sep=', ')

os.system('pause')