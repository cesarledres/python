# Exemplo: solicitar ao usuário que ele einforme 10 números inteiros para inserir em uma lista

lista_numeros = []

for i in range(10): # i vai variar de 0 a 9
    num = int(input("Digite um número para inserir na lista: "))
    lista_numeros.append(num)

print(lista_numeros)