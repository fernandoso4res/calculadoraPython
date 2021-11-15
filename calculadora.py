def menu():
    print("MENU")
    asterisco()
    print("[1] - SOMA")
    print("[2] - SUBTRAÇÃO")
    print("[3] - MULTIPLICAÇÃO")
    print("[4] - DIVISÃO")
    print("[0] - PARA SAIR")
    asterisco()
    asterisco()
    opcao = int(input("Digite uma opção: "))
    return opcao
def asterisco():
    print("*"*30)
def soma(fator1, fator2):
    soma = (fator1 + fator2)
    return print(f"A soma é: {soma}")
def subtracao(minuendo, subtraendo):
    subtracao = (minuendo - subtraendo)
    return print(f"A subtração é: {subtracao}")
def multiplicacao(produto1, produto2):
    resultado = (produto1 * produto2)
    return print(f"O resultado da multiplicação é: {resultado}")
def divisao(dividendo, divisor):
    quociente = (dividendo / divisor)
    return print(f"O quociente da divisão é: {quociente}")
opcao = menu()   
while opcao != 0:
    if (opcao == 1):
        fator1 = float(input("Digite o valor 1: "))
        fator2 = float(input("Digite o valor 2: "))
        soma(fator1, fator2)
        asterisco()
    elif (opcao == 2):
        minuendo = float(input("Digite o minuendo: "))
        subtraendo = float(input("Digite o subtraendo: "))
        subtracao(minuendo, subtraendo)
        asterisco()
    elif (opcao == 3):
        produto1 = float(input("Digite o produto 1: "))
        produto2 = float(input("Digite o produto 2: "))
        multiplicacao(produto1, produto2)
        asterisco()
    elif (opcao == 4):
        dividendo = float(input("Digite o dividendo: "))
        divisor = float(input("Digite o divisor: "))
        divisao(dividendo, divisor)
        asterisco()
    opcao = menu()
else:
    print("Você saiu da calculadora")