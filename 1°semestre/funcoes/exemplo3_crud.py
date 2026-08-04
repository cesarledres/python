'''
programa que simula um CRUD (Create, Read, Update e Delete) em uma lista de dicionarios para armazenar os dados de funcionarios. Os dados são os seguintes:

- Nome
- Idade
- Salário

O menu deverá ser criado na função "main" e tera as seguintes opções:
1- inserir um funcionario
2- alterar um funcionario
3- excluir um funcionario
4- exibir um funcionario
5- exibir todos os uncionarios
6- sair
'''
from arrays.exemplo2 import indice
from arrays.exemplo6 import nome_procurar


def main():
    lista_funcionario = []

    opcao = 0

    while opcao != 6:
        print("1 - inserir um funcionario")
        print("2 - alterar um funcionario")
        print("3 - excluir um funcionario")
        print("4 - exibir um funcionario")
        print("5 - exibir todos os uncionarios")
        print("6 - sair")
        opcao = int(input("Digite o número da opção: "))

        if opcao >= 1 and opcao <= 6:
            match opcao:
                case 1:
                    inserir_funcionario(lista_funcionario)
                    print("\n")
                case 2:
                    nome_alterar = input("Digite o nome do funcionario que quer usar: ")

                    indice = buscar_funcionario(lista_funcionario, nome_alterar)

                    if indice != -1:
                        alterar_funcionario(lista_funcionario, indice)
                    else:
                        print("Funcionário não encontrado!")
                case 3:
                    nome_excluir = input("Digite o nome do funcionario que quer apagar: ")

                    indice = buscar_funcionario(lista_funcionario, nome_excluir)

                    if indice != -1:
                        alterar_funcionario(lista_funcionario, indice)
                    else:
                        print("Funcionário não encontrado!")
                case 4:
                    nome_exibir = input("Digite o nome do funcionario que quer apagar: ")

                    indice = buscar_funcionario(lista_funcionario, nome_exibir)

                    if indice != -1:
                        alterar_funcionario(lista_funcionario, indice)
                    else:
                        print("Funcionário não encontrado!")
                case 5:
                    exibir_todos_funcionario(lista_funcionario)

def inserir_funcionario(lista_funcionario):
    nome = input("Digite o nome do funcionário: ")
    idade = int(input("Digite a idade do funcionário: "))
    salario = float(input("Digite o salário do funcionário: "))

    dados_funcionarios = {
        'nome': nome,
        'idade': idade,
        'salario': salario
    }

    lista_funcionario.append(dados_funcionarios)
    print("Funcionário inserido com sucesso!")

def buscar_funcionario(lista_funcionario,nome):
    nome_procurar = input("Digite o nome do funcionário que deseja procurar: ")
    indice = -1

    for i in range(len(lista_funcionario)):
        if nome_procurar == lista_funcionario[i]['nome']:
            indice = i

    return indice

def alterar_funcionario(lista_funcionario, indice):
    print(f"Nome do funcionário: {lista_funcionario[indice]['nome']}")
    novo_nome = input("Digite o novo nome para o funcionário: ")

    print(f"Idade do funcionário: {lista_funcionario[indice]['idade']}")
    nova_idade = int(input("Digite a nova idade do funcionário: "))

    print(f"Salário do funcionário: {lista_funcionario[indice]['salario']}")
    novo_salario = float(input("Digite o novo salário do funcionário: "))

    lista_funcionario[indice]['nome'] = novo_nome
    lista_funcionario[indice]['idade'] = nova_idade
    lista_funcionario[indice]['salario'] = novo_salario

    print("Dados do funcionário alterados com sucesso!")

def excluir_funcionario(lista_funcionario, indice):
    lista_funcionario.pop(indice)
    print("Funcionário excluído com sucesso!")

def exibir_um_funcionario(lista_funcionario, indice):
    print("***DADOS DO FUNCIONÁRIO***")
    print(f"Nome do funcionário: {lista_funcionario[indice]['nome']}")
    print(f"Idade do funcionário: {lista_funcionario[indice]['idade']}")
    print(f"Salário do funcionário: {lista_funcionario[indice]['salario']}")

def exibir_todos_funcionario(lista_funcionario):
    print("***DADOS DE TODOS OS FUNCIONÁRIOS***")
    for i in range(len(lista_funcionario)):
        print(f"Nome do funcionário: {lista_funcionario[i]['nome']}")
        print(f"Idade do funcionário: {lista_funcionario[i]['idade']}")
        print(f"Salário do funcionário: {lista_funcionario[i]['salario']}")

if __name__ == "__main__":
    main()