# Funções mais utilizadas em listas

lista_notas = [6.5,10,8.7,9.4,3.4,7.5,2.5]

# Função que retorna o tamanho da lista
tamanho_lista = len(lista_notas)
print(f"O tamanho da lista é {tamanho_lista}")

# Função que retorna um somatório da lista
soma_lista = sum(lista_notas)
print(f"A soma de todas as notas é {soma_lista}")

# Função que retorna o maior valor da lista
maior_nota = max(lista_notas)
print(f"A maior nota é {maior_nota}")

# Função que retorna o menor valor da lista
menor_nota = min(lista_notas)
print(f"A menor nota é {menor_nota}")

# Função que retorna se um elemento pertene a lista
nota_procurar = float(input("Digite a nota que deseja procurar na lista: "))

if nota_procurar in lista_notas:
    print("Está dentro da lista")
else:
    print("Não está dentro da lista")

# Função que retorna o índice de um elemento que está dentro da lista
nota_procurar = float(input("Digite o a nota para informar seu índice da lista: "))

if nota_procurar in lista_notas:
    indice = lista_notas.index(nota_procurar)
    print(f"Está nota está armazenada no índice {indice} da lista")