import os

grausFarenheit = float(input("Temperatura em farenheit: "))

grausCelsius = (5 * (grausFarenheit - 32)) / 9

print(f'Temperatura em graus celsius: {round(grausCelsius, 2)}°C')

os.system('pause')