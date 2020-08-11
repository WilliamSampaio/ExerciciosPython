import os

letra = input('digite uma letra: ')

while len(letra) > 1:
    print('Digite apenas uma letra!')
    letra = input('digite uma letra: ')

while letra.isnumeric():
    print('Digite apenas uma letra!')
    letra = input('digite uma letra: ')

if letra == 'a' or letra == 'A':
    print('VOGAL')
elif letra == 'e' or letra == 'E':
    print('VOGAL')
elif letra == 'i' or letra == 'I':
    print('VOGAL')
elif letra == 'o' or letra == 'O':
    print('VOGAL')
elif letra == 'u' or letra == 'U':
    print('VOGAL')
else:
    print('CONSOANTE')

os.system("pause")