'''
Desenvolva um programa que receba os dados de duas pessoas: nome e altura.

Exiba o nome da pessoa mais alta
'''

nome1 = str(input("Informe o nome da primeira pessoa: "))
altura1 = float(input("Informe a altura: "))

nome2 = str(input("Informe o nome da segunda pessoa: "))
altura2 = float(input("Informe a altura: "))

if altura1 >= 0 or altura2 >= 0:
    if altura1 > altura2:
        print(f"{nome1} é o mais alto.")
    elif altura1 == altura2:
        print(f"Os dois possuem a mesma altura.")
    else:
        print(f"{nome2} é o mais alto.")
else:
    print("Altura inválida.")