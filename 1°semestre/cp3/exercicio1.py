'''
1) Escreva um programa que possua 2 listas: lista de temperaturas e lista de cidades. A inserção das temperaturas e suas respectivas
cidades deverá ser executada até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). Após a inserção, informe:
a) a maior temperatura e qual a cidade;
b) a menor temperatura e qual a cidade;
c) a média das temperaturas.
'''

lista_temperatura = []
lista_cidade = []
saida = 1

while saida != 0:
    cidade = input("Informe a cidade: ")
    temperatura = int(input("Informe a temperatura: "))

    lista_cidade.append(cidade)
    lista_temperatura.append(temperatura)

    saida = int(input("Deseja continuar (1-SIM / 0-NÃO): "))

maior_temperatura = max(lista_temperatura)
indice_maior_temperatura = lista_temperatura.index(maior_temperatura)
cidade_maior_temperatura = lista_cidade[indice_maior_temperatura]

menor_temperatura = min(lista_temperatura)
indice_menor_temperatura = lista_temperatura.index(menor_temperatura)
cidade_menor_temperatura = lista_cidade[indice_menor_temperatura]

media_temperatura = sum(lista_temperatura) / len(lista_temperatura)

print(f"A maior temperatura é de {maior_temperatura}° registrada na cidade {cidade_maior_temperatura}.")
print(f"A menor temperatura é de {menor_temperatura}° registrada na cidade {cidade_menor_temperatura}.")
print(f"A média de temperatura das cidades é de {media_temperatura}.")