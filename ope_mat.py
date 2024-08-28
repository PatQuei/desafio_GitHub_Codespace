# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
operacao = input("Qual operação deseja fazer(+, -, *, /) : ")

if operacao == "+":
    print(num1 + num2)

elif operacao == "-":
    print(num1 - num2)

elif operacao == "*":
    print(num1 * num2)

elif operacao == "/":
    print(num1 / num2)

else:
    print("Operação digitada inválida")