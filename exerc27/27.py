import os

turno = input('Qual turno você estuda? ')

if turno[0] == 'm' or turno[0] == 'M':
    print('Bom Dia!')
elif turno[0] == 'v' or turno[0] == 'V':
    print('Boa Tarde')
elif turno[0] == 'n' or turno[0] == 'N':
    print('Boa Noite')
else:
    print('Valor Inválido!')

os.system("pause")
