import os

letra = input('Digite uma letra: ')

while letra.isnumeric():
    print('Digite apenas uma letra!')
    letra = input('Digite uma letra: ')

if letra[0] == 'm' or letra[0] == 'M':
    print('Masculino')
elif letra[0] == 'f' or letra[0] == 'F':
    print('Feminino')
else:
    print('Sexo Inválido!')

os.system("pause")
