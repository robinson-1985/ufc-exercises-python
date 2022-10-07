''' 9. Faça um programa na linguagem Python que pede os seguintes dados: Valor do 
salário de um funcionário e aumento em porcentagem. Depois mostre o valor do aumento 
e o salário com aumento arredondados para duas casas decimais.'''

salario = float(input('Qual o valor do seu salário? '))
percentual = float(input('Digite o valor em porcentagem do aumento: '))

novoSalario = salario + ((salario*percentual)/100)
aumento = novoSalario - salario

print ('Aumento de: R$" ', aumento)
print ('Novo salário: R$ ', novoSalario)
