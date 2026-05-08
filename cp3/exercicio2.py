'''
2) Escreva um programa em Python que solicite ao usuário 10 números inteiros para armazenar na lista A. Em seguida, apresente o total de
elementos ímpares existentes na lista e o percentual do valor total de números ímpares em relação à quantidade total de elementos
armazenados na lista.
'''
listaA = []
lista_impares = []

for i in range(10):
    numero = int(input("Digite um número: "))

    listaA.append(numero)

for i in listaA:
    if i % 2 != 0:
        lista_impares.append(i)

quantidade_impares = len(lista_impares)
percentual_impares = quantidade_impares / len(listaA) * 100

print(f"A quantidade de elementos impares na lista A é de {quantidade_impares}.")
print(f"O percentual de elementos impares em relação ao total é de {round(percentual_impares, 2)}%.")