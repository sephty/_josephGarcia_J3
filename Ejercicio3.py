'''
Nombre: Joseph Garcia Jimenez
Fecha: 11/julio/2025
Desarrollo: Calculadora de consumo empresarial
'''

def calconsumo(consumoW, hora, dias, cantidad):
    consumo = (consumoW * hora * dias * cantidad) / 1000
    return consumo

def calemisiones(consumokwh, factor):
    return consumokwh * factor

def impresion(nombre_equipo, consumo_total, emisiones_totales):
    print(nombre_equipo)
    print('Consumo Total (kWh):', consumo_total)
    print('Emisiones Totales (kg CO2e):', emisiones_totales)
    print('---')

def CalcEmisionesTotal(equipo1, equipo2, equipo3, equipo4, diasfunc, factor):
    total = 0

    nombre1 = equipo1['nombre']
    c1 = equipo1['cantidad']
    p1 = equipo1['potenciaW']
    h1 = equipo1['hora']
    consumo1 = calconsumo(p1, h1, diasfunc, c1)
    emision1 = calemisiones(consumo1, factor)
    total = total + emision1
    impresion(nombre1, consumo1, emision1)

    nombre2 = equipo2['nombre']
    c2 = equipo2['cantidad']
    p2 = equipo2['potenciaW']
    h2 = equipo2['hora']
    consumo2 = calconsumo(p2, h2, diasfunc, c2)
    emision2 = calemisiones(consumo2, factor)
    total = total + emision2
    impresion(nombre2, consumo2, emision2)

    nombre3 = equipo3['nombre']
    c3 = equipo3['cantidad']
    p3 = equipo3['potenciaW']
    h3 = equipo3['hora']
    consumo3 = calconsumo(p3, h3, diasfunc, c3)
    emision3 = calemisiones(consumo3, factor)
    total = total + emision3
    impresion(nombre3, consumo3, emision3)

    nombre4 = equipo4['nombre']
    c4 = equipo4['cantidad']
    p4 = equipo4['potenciaW']
    h4 = equipo4['hora']
    consumo4 = calconsumo(p4, h4, diasfunc, c4)
    emision4 = calemisiones(consumo4, factor)
    total = total + emision4
    impresion(nombre4, consumo4, emision4)

    print('Emisiones totales anuales:')
    print(total)
    return total


equipo1 = {'nombre': 'Computadores', 'cantidad': 5, 'potenciaW': 100, 'hora': 2}
equipo2 = {'nombre': 'Impresoras', 'cantidad': 2, 'potenciaW': 250, 'hora': 2}
equipo3 = {'nombre': 'Lamparas', 'cantidad': 10, 'potenciaW': 40, 'hora': 10}
equipo4 = {'nombre': 'Acondicionado', 'cantidad': 1, 'potenciaW': 1500, 'hora': 6}

diasfunc = 250
factoremision = 0.5

print('Bienvenido a la calculadora de contaminacion empresarial')
CalcEmisionesTotal(equipo1, equipo2, equipo3, equipo4, diasfunc, factoremision)

