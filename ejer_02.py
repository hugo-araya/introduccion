'''
Leer 20 números e imprimir cuantos son positivos, 
cuantos negativos y cuantos neutros.
'''
i = 0
positivo = 0
negativo = 0
cero = 0
while i < 20:
    print ('Leyendo : ', i+1)
    numero = int(input('Ingrese numero: '))
    if numero > 0:
        positivo = positivo + 1
    else:
        if numero < 0:
            negativo = negativo + 1
        else:
            cero = cero + 1
    i = i + 1

print ('Positivos: ', positivo)
print ('Negativos: ', negativo)
print ('Ceros: ', cero)



