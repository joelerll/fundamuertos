""" TEMA 1 """

def tema_a(lista):
    nombres_universidades = []
    for direccion in lista: # recorrer la lista de direcciones universidades
        direccion_split = direccion.split('.') # separa cada direccion por el punto y convertirlo en array
        if 'edu' in direccion_split: # detectar si en la direccion se encuentra la palabra clave edu
            nombres_universidades.append(direccion_split[direccion_split.index('edu') - 1].upper()) # extraer la palabra anterior a edu, que seria el nombre de la universidad
    return list(set(nombres_universidades)) # se usa list para limpiar de palabras repetidas

def tema_b(lista):
    nombres_universidades = []
    for direccion in lista:
        direccion_split = direccion.split('.')
        if 'ec' in direccion_split and 'edu' in direccion_split:
            nombres_universidades.append(direccion_split[direccion_split.index('edu') - 1].upper())
    return list(set(nombres_universidades))

def tema_c(usuario, sigla, lista):
    direccion_universidad = ""
    for direccion in lista:
        direccion_split = []
        direccion_split_tmp = direccion.split('.')
        for  direccion_tmp in direccion_split_tmp:
            direccion_split.append(direccion_tmp.lower())
        if sigla.lower() in direccion_split:
            if direccion_split[-1] == 'edu':
                direccion_universidad = direccion_split[-1]
            if direccion_split[-2] == 'edu':
                direccion_universidad = direccion_split[-2] + "." + direccion_split[-1]
    return usuario + "@" + sigla.lower() + "." + direccion_universidad

def tema_c_menu(lista):
    usuario_input = input('Ingrese el usuario: ')
    sigla_input = input('Ingrese el nombre/sigla de la universidad: ').lower()
    correo = tema_c(usuario_input, sigla_input, lista)
    print("El correo electronico del usuario es:")
    print(correo)


""" TEMA 2 """