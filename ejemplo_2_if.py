'''
Leer tres numeros enteros y escribirlos de menor a mayor
y preguntar si desea seguir
'''
ok = 0
while ok == 0:
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    num3 = int(input('Numero 3: '))

    if num1 < num2:
        if num1 < num3:
            if num2 < num3:
                print (num1, num2, num3)
            else:
                print (num1, num3, num2)
        else:
            print (num3, num1, num2)
    else:
        if num2 < num3:
            if num1 < num3:
                print(num2, num1, num3)
            else:
                print (num2, num3, num1)
        else:
            print (num3, num2, num1)
    ok = int(input("Ingrese 0 para continuar, 1 para salir: "))
print ('Eso seria todo ...')
