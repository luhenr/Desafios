num = int(input("Digite um numero: "))

fibonacci = [0, 1]
while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if num in fibonacci:
    print("O numero", num, "pertence a sequência de Fibonacci!")
else:
    print("O numero", num, "nao pertence a sequência de Fibonacci.")
