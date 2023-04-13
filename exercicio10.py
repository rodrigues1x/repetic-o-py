primeiroVetor = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
segundoVetor = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
terceiroVetor =[]

contador = 0
for i in primeiroVetor:
    terceiroVetor.append (i)
    terceiroVetor.append(segundoVetor[contador])
    contador +=1

print('numeros intercalados',terceiroVetor)

