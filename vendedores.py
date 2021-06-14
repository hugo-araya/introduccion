'''
 Una compañía de seguros tiene contratados a n vendedores. 
 Cada uno hace tres ventas a la semana. Su política de 
 remuneraciones es que un vendedor recibe un sueldo base, 
 y un 10% extra por comisiones de sus ventas. El gerente de 
 su compañía desea saber cuanto dinero obtendrá en la semana 
 cada vendedor por concepto de comisiones por las tres ventas 
 realizadas, y cual será su remuneración final, tomando en 
 cuenta su sueldo base y sus comisiones.
'''

vendedor = int(input('Cantidad de vendedores: '))
i = 0
while i < vendedor:
    j = 0
    suma_ventas = 0        
    print ('\nDatos del vendedor: ', i+1)
    while j < 3:
        venta = int(input('\tIngrese venta: '))
        suma_ventas = suma_ventas + venta
        j = j + 1
    sueldo_base = int(input('\tIngrese sueldo base: '))
    comision = suma_ventas * 0.1
    print ('\t\tVendedor: ', i+1, '\n\t\tComision: ', comision, '\n\t\tSueldo final: ', sueldo_base + comision)
    i = i + 1
print ('Seria todo ...')