'''
Uma empresa decidiu dar um bônus aos salários dos funcionários de acordo com o total vendido por cada um.
Nesse sentido, solicite ao usuário o salário de um desses funcionários e qual o total de vendas que ele
efetuou. Caso o total vendido pelo funcionário seja até R$5000.00, então o bônus será de 10%; caso
contrário, o bônus será de 20%. Por fim, exiba o salário do funcionário com o bônus.
'''

salario = float(input("Informe o salário: "))
total_vendas = float(input("Informe o total das vendas: "))

if total_vendas <= 5000:
    salario_bonus = salario * 1.1
else:
    salario_bonus = salario * 1.2

print(f"O salário total é de R$ {round(salario_bonus, 2)}.")