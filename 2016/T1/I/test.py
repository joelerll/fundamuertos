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

visitados = [ 
  'maria2|www.facebook.com|160',
  'xavi7|www.eluniverso.com|50',
  'jose15|www.sri.gob.ec|30',
  'maria2|www.twitter.com|30',
  'xavi7|www.inec.gob.ec|10',
  'maria2|www.espol.edu.ec|50',
  'jose15|www.sri.gob.ec|120',
  'xavi7|www.sri.gob.ec|20',
  'maria2|www.twitter.com|20'
]

empleados = ['maria2', 'jose15', 'xavi7']

trabajo = [
  'www.espol.edu.ec',
  'www.inec.gob.ec',
  'www.sri.gob.ec'
]

import unittest
from temas import *

class Tema1(unittest.TestCase):
  def test_tema_1_a(self):
    nombres_universidades = tema_1_a(lista)
    nombres_validos_universidades = ['ESPOL', 'UESS', 'UCSG', 'STANFORD', 'HARDVARD', 'EDUCACIONBC']
    es_valido = bool(set(nombres_universidades) - set(nombres_validos_universidades))
    assert es_valido == False
    assert len(nombres_universidades) != 0

  def test_tema_1_b(self):
    nombres_universidades_ecuador = tema_1_b(lista)
    nombres_validos_universidades_ecuador = ['ESPOL', 'UESS', 'UCSG']
    no_es_valido = bool(set(nombres_universidades_ecuador) - set(nombres_validos_universidades_ecuador))
    assert no_es_valido == False
    assert len(nombres_universidades_ecuador) != 0

  def test_tema_1_c(self):
    salida_1 = tema_1_c("rafael.bonilla", "UCSG", lista)
    salida_2 = tema_1_c("rafael.bonilla", "ESPOL", lista)
    salida_3 = tema_1_c("rafael.bonilla", "EDUCACIONBC", lista)
    salida_4 = tema_1_c("rafael.bonilla", "STANFORD", lista)
    assert "rafael.bonilla@ucsg.edu.ec" == salida_1
    assert "rafael.bonilla@espol.edu.ec" == salida_2
    assert "rafael.bonilla@educacionbc.edu.mx" == salida_3
    assert "rafael.bonilla@stanford.edu" == salida_4



if __name__ == "__main__":
  unittest.main()