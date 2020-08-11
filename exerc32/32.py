import os

numeros = []

num = 0

while(num < 5):
    numeros.append(float(input("digite o numero {}: ".format(num + 1))))
    num += 1
    
soma = 0
for num in numeros:
    soma += num

media = soma / 5

print("soma: {}".format(soma))
print("media: {}".format(media))

os.system("pause")
