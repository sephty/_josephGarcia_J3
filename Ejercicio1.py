
'''
Nombre: Joseph Garcia Jimenez
Fecha: 11/julio/2025
desarrollo: promedio de voltajes
'''
promedio = 0.0
# Entrada de valores
print('Calculadora de promedio de voltajes')
print (' ')
vol1 = float(input('Ingrese el Voltaje 1: '))
vol2 = float(input('Ingrese el Voltaje 2: '))
vol3 = float(input('Ingrese el Voltaje 3: '))
vol4 = float(input('Ingrese el Voltaje 4: '))
vol5 = float(input('Ingrese el Voltaje 5: '))


promedio = (vol1+vol2+vol3+vol4+vol5)/5

print(f'El promedio de los voltajes ingresados es: {promedio}')
if (promedio > 220):
    print('El promedio es mayor a 220' )
else:
    print('El promedio es menor a 220')
