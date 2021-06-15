neutro = 0
negativo = 0
positivo = 0
veces = 0
while veces < 20:
    numero = int(input('Ingrese numero: '))
    if numero > 0 :
        positivo = positivo + 1
    else:
        if numero < 0 :
            negativo = negativo + 1
        else:
            neutro = neutro + 1
    veces = veces + 1
print ('Positivos: ', positivo)
print ('Negativos: ', negativo)
print ('Neutros: ', neutro)
