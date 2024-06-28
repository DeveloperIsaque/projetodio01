# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles

num01 = int(input("Digite um número: "))
num02 = int(input("Digite outro número: "))

operation = input("Digite qual operação deseja realizar (+, -, /, *): ")

if operation == '+':
    print(num01 + num02)
elif operation == '-':
    print(abs(num01 - num02))
elif operation == '/':
    print(num01 - num02)
elif operation == '*':
    print(num01 / num02)
else:
    print("Operação inválida!")

