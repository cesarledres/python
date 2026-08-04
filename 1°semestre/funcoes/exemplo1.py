'''
Funções em Python

Existem 2 tipos:

- Procedimentos: executam tarefas (linhas de código), porém NÃO retornam dados
- Funções: executam tarefas (linhas de códigos), porém RETORNAM dados
'''
from arrays.exemplo2 import tamanho_lista


# função que exibe uma mensagem na tela:
def exibir_mensagem():
    print("Minha primeira função")

# utilização/chamada da função:
exibir_mensagem()

# funcao que exibe mensagem na tela
def exibir_mensagem_custom(mensagem):
    print(mensagem)

exibir_mensagem_custom("a funcao")

mensagem_usuario = input("Digite uma mensagem para ser exibida: ")
exibir_mensagem_custom(mensagem_usuario)

# funcção com retorno:
def somar_numeros(num1, num2):
    soma = num1 + num2
    return soma

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print(f"A soma dos dois números é {somar_numeros(n1, n2)}")

