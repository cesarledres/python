'''
Pela tabela a seguir, mostre a descrição e o preço do produto após a
digitação do código pelo usuário. Se o produto não estiver cadastrado,
emitir mensagem avisando. OBS: utilizar o Desvio Condicional de Múltipla
Escolha.

| Código | Descrição | Preço R$ |
|--------|-----------|----------|
|01      |Caneta     |1.20      |
|02      |Lápis      |0.80      |
|03      |Caderno    |4.50      |
|04      |Borracha   |1.00      |
|05      |Régua      |1.50      |
'''

print("---------- MENU DE OPÇÕES ----------")
print("1) Caneta -> R$ 1.20")
print("2) Lápis -> R$ 0.80")
print("3) Caderno -> R$ 4.50")
print("4) Borracha -> R$ 1.00")
print("5) Régua -> R$ 1.50")

opcao = int(input("Digite o número da sua opção: "))

match opcao:
    case 1:
        print("Preço: R$ 1.20")
    case 2:
        print("Preço: R$ 0.80")