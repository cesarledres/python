'''
3) Faça um programa em Python que solicite ao usuário 10 elementos que devem ser armazenados em 2 listas (cada uma com
10 elementos).
Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das 2 listas.
'''

lista1 = []
lista2 = []
lista3 = []

for i in range(4):
    numero = int(input("Digite um número para entrar na lista 1: "))
    lista1.append(numero)

for i in range(4):
    numero = int(input("Digite um número para entrar na lista 2: "))
    lista1.append(numero)

for i in lista1:
    if i % 2 != 0:
        lista3.append(i)
    else:
        indice_lista1 = lista1.index(i)
        print(indice_lista1)

        numero_lista2 = lista2[indice_lista1]

        lista3.append(numero_lista2)

print(lista3)