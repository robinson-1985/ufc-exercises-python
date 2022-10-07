''' 3. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a
temperatura em graus Celsius. Dica: C = ( 5 ∗ ( F − 32 ) /9 )'''

temperatura_celsius =float(input('Informe a temperatura em °C: '))
temperatura_farenheit = ((temperatura_celsius*(9/5))+32)
print('A temperatura de {}°F corresponde a {}°C' .format(temperatura_farenheit,temperatura_celsius))
