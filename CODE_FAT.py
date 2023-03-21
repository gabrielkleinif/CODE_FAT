print("Calculadora de Fatorial")

# solicita o número a ser calculado o fatorial
num = int(input("Digite um número inteiro positivo: "))

# calcula o fatorial do número
fat = 1
for i in range(1, num + 1):
    fat *= i

# exibe o resultado
print("O fatorial de", num, "é", fat)
