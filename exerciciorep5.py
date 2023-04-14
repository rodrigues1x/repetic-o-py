print("Insira a população da A:")
a = int(input())
print("Insira a população da B:")
b = int(input())
print("Insira o crescimento da A:")
ca = float(input())
while ca < 0:
    print("Número inválido")
    ca = float(input())
print("Insira o crescimento da B:")
cb = float(input())
while cb < 0:
    print("Número inválido")
    cb = float(input())
ano = 0

while a <= b:
    a += a * (ca / 100)
    b += b * (cb / 100)
    ano += 1
print(ano)