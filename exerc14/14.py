import os

grausCelsius = float(input("Temperatura em celsius: "))

grausFarenheit = grausCelsius * (9 / 5) + 32

print(f'Temperatura em graus farenheit: {round(grausFarenheit, 2)}°F')

os.system('pause')