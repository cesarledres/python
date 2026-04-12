'''
Um grupo de amigos resolveu fazer um happy hour em um bar após o horário de trabalho. Na ocasião eles
pediram porções de batatas fritas, pastéis e cervejas para acompanhar. Escreva um programa em Python
que calcule o total do pedido baseado nas quantidades de porções e cervejas consumidas tendo como
referência a tabela abaixo. Além disso, calcule o valor individual da conta de acordo com o número de
amigos.
'''

qnt_fritas = int(input("Informe a quantidade de porções de batatas fritas: "))
qnt_pasteis = int(input("Informe a quantidade de porções de pastéis: "))
qnt_cervejas = int(input("Informe a quantidade de cervejas: "))

num_amigos = int(input("Informe o números de amigos na mesa: "))

valor_total = qnt_fritas * 35 + qnt_pasteis * 25 + qnt_cervejas

valor_individual = valor_total / num_amigos

print(f"O valor total da conta é R$ {round(valor_total, 2)}.")
print(f"O valor individual é R$ {round(valor_individual, 2)}.")