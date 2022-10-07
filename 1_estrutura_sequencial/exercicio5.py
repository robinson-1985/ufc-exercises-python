''' 5. Faça um programa na linguagem Python que receba 3 notas, calcule e mostre a média
aritmética.'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1 + n2 + n3)/3

print(f'A média aritmética do aluno é: %.2f' %media)
