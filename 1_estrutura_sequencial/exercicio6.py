''' 6. Faça um programa na linguagem Python que receba duas notas e seus respectivos 
pesos, calcule e mostre a média ponderada.'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

p1 = float(input('Digite o peso primeira nota: '))
p2 = float(input('Digite o peso da segunda nota: '))

print('\nA média ponderada é %.2f', (n1*p1+n2*p2)/(p1+p2))
