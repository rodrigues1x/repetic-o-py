A = []

for i in range(10):
    numero = int(input(f'Digite o {i+1}° numero:'))
    A.append(numero)

soma = sum(A)
multiplicacao = 1
for numero in A:
    multiplicacao *= numero
print('soma dos numeros:')
print(soma)
print('numero da soma ao quadrado:')
print(multiplicacao)