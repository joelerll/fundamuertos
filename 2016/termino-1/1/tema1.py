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
    "www.facebook.com",
    "www.wse.hardvard.edu.com"
]

def siglas_universidades(lista):
    siglas = [] # guardar las siglas en un array
    for url in lista:
        url_array = url.split(".")
        url_array_minuscula = []
        for palabra in url_array: # recorer el array para hacerlo en minuscula todo
            url_array_minuscula.append(palabra.lower())
        if ('edu' in url_array_minuscula): # filtrar solo las universidades
            index_edu = url_array_minuscula.index('edu') #obtener el index de donde esta edu
            sigla = url_array_minuscula[index_edu-1] #como la sigla siempre debe estar antes de edu, le restamos una unidad
            siglas.append(sigla.upper())
    return siglas

def siglas_cantidad_ecuador(lista):
    siglas = []
    for url in lista:
        url_array = url.split('.')
        url_array_minuscula = []
        for palabra in url_array:
            url_array_minuscula.append(palabra.lower())
        if('edu' in url_array_minuscula and 'ec' in url_array_minuscula):
            index_edu = url_array_minuscula.index('edu')
            sigla = url_array_minuscula[index_edu-1]
            siglas.append(sigla.upper())
    siglas_ecuador = list(set(siglas)) #para que no se repitan las universidades
    diccionario = {}
    for sigla in siglas_ecuador: # inicializar diccionario con cero todo
            diccionario[sigla] = 0
    for sigla in siglas:
        suma = diccionario[sigla] + 1
        diccionario[sigla] = suma
    return diccionario

def imprimir_correo(lista):
    usuario_input = input('Ingrese el usuario: ')
    sigla_input = input('Ingrese el nombre/sigla de la universidad: ').lower()
    dominio = ''
    for url in lista:
        url_array = url.split(".")
        url_array_minuscula = []
        for palabra in url_array: # recorer el array para hacerlo en minuscula todo
            url_array_minuscula.append(palabra.lower())
        if (sigla_input in url_array_minuscula): # filtrar solo las universidades
            index_edu = url_array_minuscula.index(sigla_input) #obtener el index de donde esta edu
            dominio = '.'.join(url_array_minuscula[index_edu:]) # dominio es lo que esta despues del arroba
            break; # si lo encuentra ya no sigue
    print(usuario_input + '@' + dominio)


if __name__ == '__main__':
    # primera pregunta
    print('\nEn la lista aparecen 6 universidades:')
    contador = 1
    conjunto_universidades = set(siglas_universidades(lista)) # convertir en conjuto para eliminar las repetidas
    for i in conjunto_universidades: # recorrer el conjunto que retonrna la funcion
        print('{contador}.) {sigla}'.format(contador = contador, sigla = i))
        contador = contador + 1
    print('\n')

    # segunda pregunta
    siglas_ecuador = siglas_cantidad_ecuador(lista)
    print('En la lista aparecen {} universidades del ecuador'.format(len(siglas_cantidad_ecuador(lista))))
    for key, value in siglas_ecuador.items():
        print('{}.) {}'.format(value, key))
    print('\n')
    imprimir_correo(lista)
