# a) A lógica é adicionar 2 ao número anterior. Portanto, o próximo elemento é 9.
a = [1, 3, 5, 7]
prox = a[-1] + 2
print(prox)  # imprime 9

# b) A lógica é multiplicar o número anterior por 2. Portanto, o próximo elemento é 128.
b = [2, 4, 8, 16, 32, 64]
prox = b[-1] * 2
print(prox)  # imprime 128

# c) A lógica é elevar o índice da sequência ao quadrado. Portanto, o próximo elemento é 49.
c = [0, 1, 4, 9, 16, 25, 36]
prox = len(c) ** 2
print(prox)  # imprime 49

# d) A lógica é elevar o índice da sequência ao quadrado e multiplicar por 4. Portanto, o próximo elemento é 100.
d = [4, 16, 36, 64]
prox = (len(d) + 1) ** 2 * 4
print(prox)  # imprime 100

# e) A lógica é somar os dois números anteriores. Portanto, o próximo elemento é 13.
e = [1, 1, 2, 3, 5, 8]
prox = e[-1] + e[-2]
print(prox)  # imprime 13

# f) Não há lógica aparente para esse problema. Uma possível resposta 'certa' envolve aplicar que os números apresentados começam com a letra D, então lógicamente o próximo número, nesse contexto, seria o 200.
seq = [2, 10, 12, 16, 17, 18, 19]
prox = 200
print(prox)  # imprime 200
