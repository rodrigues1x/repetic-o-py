primeiroVetor = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
segundoVetor = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
terceiroVetor =[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
quartoVetor = []

contador = 0
for i in primeiroVetor:
    quartoVetor.append (i)
    quartoVetor.append(segundoVetor[contador])
    quartoVetor.append(terceiroVetor[contador])
    contador +=1

print('numeros intercalados',quartoVetor)