print ('Este programa pide su nombre y la hora.')
print ('Y lo saluda de acuerdo a la hora, observacion: ')
print ('la hora debe ser ingresada en formato 24 hrs.')

nombre = input('Nombre: ')
hora = int(input('Hora: '))

if hora >= 7:
    if hora <= 12:
        print ('Buenos dias', nombre)
    else:
        if hora <= 20:
            print ('Buenas Tardes', nombre)
        else:
            if hora <= 23:
                print('Buenas Noches', nombre)
else:
    print ('Anda a acostarte', nombre)

print ('Eso seria todo')

