exercicio3 = [10.0, 9.5, 8.0, 7.0]
media = 0
for i in range (0, len(exercicio3)):
    print('nota', i+1,':', exercicio3[i])
    media = media + exercicio3[i]
media = media / len(exercicio3)
print('Média:', media)