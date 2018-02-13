from temas import *
import numpy as np
from pytest import *
import sys
lista = [
    "www.espol.edu.ec",
    "www.google.com",
    "www.sri.gob.ec",
    "www.fiec.espol.edu.ec",
    "www.FIEC.espol.edu.ec",
    "www.fcnn.Espol.edu.ec",
    "www.fict.espol.edu.ec",
    "www.ucsg.edu.ec",
    "www.Stanford.edu",
    "www.hardvard.edu",
    "www.opensource.org",
    "www.ESPOL.edu.ec",
    "www.uess.edu.ec",
    "www.educacionbc.edu.mx",
    "www.UCSG.edu.ec",
    "www.facebook.com",
    "www.wse.hardvard.edu.com"
]

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



if __name__ == '__main__':

    # TEMA 1
    # a
    nombres_universidades = tema_a(lista)
    nombres_validos_universidades = ['ESPOL', 'UESS', 'UCSG', 'STANFORD', 'HARDVARD', 'EDUCACIONBC']
    no_es_valido = bool(set(nombres_universidades) - set(nombres_validos_universidades))
    if (no_es_valido and len(nombres_universidades) != 0):
        print("ERROR tema1(a) NO valido")
        print(nombres_universidades)
        sys.exit(1)

    # b
    nombres_universidades_ecuador = tema_b(lista)
    nombres_validos_universidades_ecuador = ['ESPOL', 'UESS', 'UCSG']
    no_es_valido = bool(set(nombres_universidades_ecuador) - set(nombres_validos_universidades_ecuador))
    if (no_es_valido and len(nombres_universidades_ecuador) != 0):
        print("ERROR tema1(b) NO valido")
        print(nombres_universidades_ecuador)
        sys.exit(1)

    # c
    salida_1 = tema_c("rafael.bonilla", "UCSG", lista)
    salida_2 = tema_c("rafael.bonilla", "ESPOL", lista) 
    salida_3 = tema_c("rafael.bonilla", "EDUCACIONBC", lista) 
    salida_4 = tema_c("rafael.bonilla", "STANFORD", lista)

    if (salida_1 != "rafael.bonilla@ucsg.edu.ec" or salida_2 != "rafael.bonilla@espol.edu.ec" or salida_3 != "rafael.bonilla@educacionbc.edu.mx" or salida_4 != "rafael.bonilla@stanford.edu"):
        print("ERROR tema1(c)")
        sys.exit(1)


    # TEMA 2

    sys.exit(0)