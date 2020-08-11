import os

mesTrabalhado = input('DIGITE O MÊS TRABALHADO: ')
valorPorHora = float(input('DIGITE O PREÇO DA HORA TRABALHADA: '))
horaTrabalhada = int(input('DIGITE O TOTAL DE HORAS TRABALHADAS NO MÊS: '))

salarioBruto = valorPorHora * horaTrabalhada
impostoDeRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
descontoSindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - (impostoDeRenda + inss + descontoSindicato)

os.system('cls')

print()
print(f'CONTRACHEQUE - {mesTrabalhado.upper()}')
print('----------------------------------------------')
print(f'+ Salário Bruto : R${round(salarioBruto, 2)}')
print(f'- IR (11%) : R${round(impostoDeRenda, 2)}')
print(f'- INSS (8%) : R${round(inss, 2)}')
print(f'- Sindicato ( 5%) : R${round(descontoSindicato, 2)}')
print('----------------------------------------------')
print(f'= Salário Liquido : R${round(salarioLiquido, 2)}')

os.system('pause')