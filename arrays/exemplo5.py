# Exemplo: Solicitar que o usuário informe 5 números inteiros para serem armazenados para cada lista (A e B). Em seguida, crie uma nova lista (C) cujos elementos serão criados pela soma dos elementos correspondentes das 2 listas (A e B).

lista_a = []
lista_b = []
lista_c = []

for i in range(5):
    num = int(input("Digite um elemento da lista A: "))
    lista_a.append(num)

for i in range(5):
    num = int(input("Digite um elemento da lista B: "))
    lista_b.append(num)

# Percorrer as listas A e B para calcular os elementos da lista C
for i in range(5):
    soma = lista_a[i] + lista_b[i]
    lista_c.append(soma)

print(lista_a)
print(lista_b)
print(lista_c)
