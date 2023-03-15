# pedir para o usuário informar a string
string = input("Digite uma string para inverter: ")

# criar uma string vazia para armazenar o resultado
string_invertida = ""

# percorrer a string de trás para frente, adicionando cada caractere à string invertida
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# imprimir a string invertida
print("A string invertida é:", string_invertida)


"""
#Um método mais eficiente
# pedir para o usuário informar a string
string = input("Digite uma string para inverter: ")

# usar slicing para inverter a string
string_invertida = string[::-1]

# imprimir a string invertida
print("A string invertida é:", string_invertida)

"""
