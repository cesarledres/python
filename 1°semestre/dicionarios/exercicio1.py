'''
	Escreva um programa em Python que crie uma lista de 10 funcionários, utilizando o conceito de dicionários, contendo
os seguintes dados:
o	Nome;
o	Cargo;
o	Salário.
Depois da lista criada, exiba todos os funcionários.
OBS: o programa deverá solicitar que o usuário informe os dados para alimentar a lista de dicionários.
'''

lista_funcionarios = []

for i in range(10):
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    dados_funcionarios = {
        'nome': nome,
        'cargo': cargo,
        'salario': salario
    }

    lista_funcionarios.append(dados_funcionarios)

for i in range(10):
    print(lista_funcionarios[1])

for i in range (10):
    if lista_funcionarios[i]['salario'] > 5000:
        print(lista_funcionarios[i])