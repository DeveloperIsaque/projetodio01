# Para descobrir a média

i = int(0); 
array = []

while i < 3:
    element = int(input("digite um número: "))
    array.append(element)
    i += 1
    
soma = sum(array)

print(soma/3)