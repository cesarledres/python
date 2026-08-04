# Exemplo: Solicitar que o usuário digite 10 nomes de alunos e armenene-os em uma lista. Na sequência, solicite as medias desses aluno, armazenando-os em outra lista. Depois que as 2 listas estiverem preenchidas, faça uma busca por um nome de aluno e exiba sua media.
from arrays.exemplo2 import nota_procurar

lista_alunos = []
lista_media = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    lista_alunos.append(nome)

    media = input("Digite a média do aluno: ")
    lista_media.append(media)

nome_procurar = input("Digite o nome do aluno que deseja saber a média: ")

if nome_procurar in lista_alunos:
    indice_nome = lista_alunos.index(nome_procurar)

    nota_procurar = lista_media[indice_nome]

    print(f"A média dessa pessoa é {nota_procurar}")
else:
    print("Este nome não está na lista")
