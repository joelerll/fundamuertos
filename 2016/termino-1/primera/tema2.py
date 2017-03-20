import numpy as np
from terminaltables import AsciiTable #para mostrar graicamemte la tabla
visitados = [ 'maria2|www.facebook.com|160',
  'xavi7|www.eluniverso.com|50',
  'jose15|www.sri.gob.ec|30',
  'maria2|www.twitter.com|30',
  'xavi7|www.inec.gob.ec|10',
  'maria2|www.espol.edu.ec|50',
  'jose15|www.sri.gob.ec|120',
  'xavi7|www.sri.gob.ec|20',
  'maria2|www.twitter.com|20']
empleados = ['maria2', 'jose15', 'xavi7']
trabajo = [
  'www.espol.edu.ec',
  'www.inec.gob.ec',
  'www.sri.gob.ec',]

def sitios_no_trabajo():
    array_sitios_visitados = []
    for visitado in visitados:
        registro = visitado.split('|')
        sitio_visitado = registro[1]
        array_sitios_visitados.append(sitio_visitado)
    conjunto_sitios_visitados = set(array_sitios_visitados)
    conjunto_sitios_trabajo = set(trabajo)
    conjunto_sitios_no_de_trabajo = conjunto_sitios_visitados - conjunto_sitios_trabajo
    array_sitios_no_trabajo = list(conjunto_sitios_no_de_trabajo)
    return array_sitios_no_trabajo

def tiempos_paginas_por_empleado():
    array_sitios = trabajo + sitios_no_trabajo()
    array_sitios_vs_empleado = np.zeros((len(empleados),len(array_sitios))) #crear array de zeros
    for registro in visitados:
        registro_array = registro.split('|')
        empleado = registro_array[0]
        sitio_visitado = registro_array[1]
        minutos = registro_array[2]
        index_sitio = array_sitios.index(sitio_visitado)
        index_empleado = empleados.index(empleado)
        array_sitios_vs_empleado[index_empleado,index_sitio] =  array_sitios_vs_empleado[index_empleado,index_sitio] + int(minutos)
    return array_sitios_vs_empleado

if __name__ == '__main__':
    # Literal a
    print('Literal a=========================================')
    print('Sitios no de trabajo')
    print(sitios_no_trabajo())
    print('\n')

    # Literal b
    print('Literal b=========================================')
    print('array original')
    print(tiempos_paginas_por_empleado())
    print('\n * Tabla solo para mostrar graficamente')
    print(empleados)
    tabla = tiempos_paginas_por_empleado().tolist()
    tabla.insert(0,trabajo + sitios_no_trabajo())
    table = AsciiTable(tabla)
    table.title = 'Tiempos de trabajo'
    print (table.table)
