import os

valorPorHora = float(input('DIGITE O PREÇO DA HORA TRABALHADA: '))
horaTrabalhada = int(input('DIGITE O TOTAL DE HORAS TRABALHADAS NO MÊS: '))

salario = valorPorHora * horaTrabalhada

print(f'Salário: R${round(salario, 2)}')

os.system('pause')