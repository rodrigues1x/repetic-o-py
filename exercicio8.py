idade = [14, 22, 44, 64, 84,]
altura = [1.5, 1.8, 1.9, 1.7, 1.4]
alturaVazia = []
idadeVazia = []
print(idade)
print(altura)

for i in range (5):
    idadeVazia.append(idade.pop())
    alturaVazia.append(altura.pop())

print(idadeVazia)
print(alturaVazia)