'''
Crie um menu com 4 opções (vide abaixo), que devem ser executadas com 2 números inteiros informados pelo
usuário. As opções são as seguintes:

Opcao = 1: verificar qual é o maior número.

Opcao = 2: verificar se o primeiro número é par ou ímpar.

Opcao = 3: verificar qual é o menor número.
'''

print("---------- MENU DE OPÇÕES ----------")
print("1) Verificar qual é o maior número.")
print("2) Verificar se o primeiro número é par ou ímpar.")
print("3) Verificar qual é o menor número.")

opcao = int(input("Digite a opção desejada: "))

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

match opcao:
    case 1:
        maior_numero = max(num1, num2)
        print(f"O maior número é {maior_numero}")
    case 2:
        if num1 % 2 == 0:
            print(f"O primeiro número ({num1}) é par.")
        else:
            print(f"O primeiro número ({num1}) é impar.")
    case 3:
        menor_numero = min(num1, num2)
        print(f"O menor número é {menor_numero}")
    case _:
        print("Opção inválida.")