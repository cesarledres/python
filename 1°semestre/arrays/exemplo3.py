# Funções para inserção e remoção de elementos da lista

# 1) Inserção (append)
# Exemplo 1:

lista_nomes = ["João", "Ana", "Luiz", "Pedro", "Maria"]

# Inserir mais um nome na lista
nome = input("Digite um nome para inserir na lista: ")

lista_nomes.append(nome)

print(lista_nomes)

# 2) Remoção
# a) pop
lista_nomes.pop() # Se não for colocado nada entre parênteses remove o ultimo item da lista

print(lista_nomes)

# Execluão do segundo elemento da lista
lista_nomes.pop(1)

print((lista_nomes))
