numeros = []

for i in range(5):
    numero = int(input(f'Digite o {i+1}° numero:'))
    numeros.append(numero)

soma = sum(numeros)
multiplicacao = 1
for numero in numeros:
    multiplicacao *= numero

    print('numeros digitados:', numeros)
    print('soma:', soma)
    print('multiplicacao:', multiplicacao)