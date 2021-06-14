'''
Simular el comportamiento de un reloj digital, escribiendo la hora, 
minutos y segundos de un día desde las 0:00:00 horas hasta 
las 23:59:59 horas
'''
hora = 0
while hora < 24:
    minu = 0
    while minu < 60:
        segu = 0
        while segu < 60:
            print (hora,':', minu, ':', segu)
            segu = segu + 1
        minu = minu + 1
    hora = hora + 1
print ('Se acabo el dia ...')
