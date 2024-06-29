word = input("Digite uma palavra: ")

if word == word[::-1]:
    print("Esta palavra é sim um palíndromo.")
else:
    print("Palavra inválida.")