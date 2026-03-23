'''
A jornada de trabalho semanal de um funcionário é de 40 horas. Considerando que o mês possua 4 semanas, o
funcionário que trabalhar mais de 160 horas receberá hora extra, cujo cálculo é o valor da hora regular
com um acréscimo de 50%. Escreva um algoritmo que solicite o número de horas trabalhadas em um mês, o
salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras,
caso tenham sido trabalhadas.
'''

horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
salario_por_hora = float(input("Informe o valor do salário por hora: "))

if horas_trabalhadas > 160:
    valor_regular = salario_por_hora * 160 
    horas_extras = horas_trabalhadas - 160
    valor_extras = horas_extras * salario_por_hora * 1.5
    salario_total = valor_extras + valor_regular
    print(f"O salário total é R$ {salario_total}.")
else:
    valor_regular = salario_por_hora * horas_trabalhadas
    print(f"O salario total é R$ {valor_regular}.")
    