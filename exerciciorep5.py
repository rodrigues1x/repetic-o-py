a = 80000
b = 200000
ano = 0

populacao = input('digite a populaçao:')
taxa = input('digite as taxas de crescimento iniciais:')

while a <= b:
    a += a * 0.03
    b += b * 0.015
    ano += 1

print('A passa ou fica igual a B em %d anos' %ano)