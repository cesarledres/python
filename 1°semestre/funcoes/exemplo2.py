# funcao que insere elementos em uma lista

def inserir_elementos_lista(lista, tamanho):
    for i in range(tamanho):
        num = int(input("Digite um numero para inserir na lista: "))
        lista.append(num)


# chamada da função
lista = []
tamanho_lista = int(input("Digite o tamanho da lista que quer criar: "))

inserir_elementos_lista(lista, tamanho_lista)

print(lista)