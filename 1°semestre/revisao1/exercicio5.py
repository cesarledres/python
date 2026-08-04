'''
Escreva um programa que receba o nome e salário bruto de um funcionário.
Calcule o valor do desconto do INSS com base na tabela abaixo:
'''

nome_funcionario = input("Informe o nome do funcionaro")
salario_bruto = input("Informe o salário bruto do funcionário")

if salario_bruto <= 1100:
    desc_inss = salario_bruto * 0.075
elif salario_bruto <= 2203.48:
    desc_inss = salario_bruto * 0.09
elif salario_bruto <= 3305.22:
    desc_inss = salario_bruto * 0.12
elif salario_bruto <= 6433.57:
    desc_inss = salario_bruto * 0.14

print(f"O desconto do INSS é de R$ {round(desc_inss, 2)}.")