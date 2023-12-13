# Obtenha a entrada do usuário
limite_inferior = int(input("Digite o limite inferior do intervalo: "))
limite_superior = int(input("Digite o limite superior do intervalo: "))
numero_divisor = int(input("Digite o número pelo qual os números podem ser divididos: "))

# Percorra o intervalo e verifique se os números são divisíveis pelo número_divisor
for i in range(limite_inferior, limite_superior + 1):
    if i % numero_divisor == 0:
        print(i)