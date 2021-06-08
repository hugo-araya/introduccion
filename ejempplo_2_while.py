'''
Leer numeros y calcular su cuadrado y su cubo.
se leeran numeros hasta que se ingrese el numero 0
'''
numero = int(input('Numero: '))
while (numero != 0):
    cuadrado = numero * numero
    cubo = cuadrado * numero
    print  (cuadrado, cubo)
    numero = int(input('Numero: '))
    if numero == 0:
        print('Seria todo ...')
print("---- F i N ---------")