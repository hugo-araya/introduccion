# Entrada
sueldo_base = int(input('Ingrese sueldo base: $'))
venta1 = int(input('Ingrese venta 1: $'))
venta2 = int(input('Ingrese venta 2: $'))
venta3 = int(input('Ingrese venta 3: $'))

# Proceso
sueldo_pagar = sueldo_base + (venta1 + venta2 + venta3) * 0.1

# Salida
print('Recibe por comision: $', (venta1 + venta2 + venta3) * 0.1)
print('Sueldo a recibir: $', sueldo_pagar)
