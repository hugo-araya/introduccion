print ('Este programa pide su nombre y la hora.')
print ('Y lo saluda de acuerdo a la hora, observacion: ')
print ('la hora debe ser ingresada en formato 24 hrs.')

nombre = input('Nombre: ')
hora = int(input('Hora: '))

if hora >= 7 and hora <= 12:
    print ('Buenos dias', nombre)
if hora >= 13 and hora <= 20:
    print ('Buenas Tardes', nombre)
if hora >= 21 and hora <= 23:
    print('Buenas Noches', nombre)
if hora >= 0 and hora <= 6:
    print ('Anda a acostarte', nombre)

print ('Eso seria todo')

