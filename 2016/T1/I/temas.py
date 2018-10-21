""" TEMA 1 """
# Mostrar los nombres de las universidades sin repetir
def tema_1_a(correos):
    nombres_universidades = []
    for correo in correos: # recorrer la lista de direcciones universidades
        correo_split = correo.split('.') # separa cada direccion por el punto y convertirlo en array
        if 'edu' in correo_split: # detectar si en la direccion se encuentra la palabra clave edu
            ubicacion_nombre = correo_split.index('edu') - 1
            nombre_universidad = correo_split[ubicacion_nombre].upper() # convertirlo en mayuscula tambien
            nombres_universidades.append(nombre_universidad) # extraer la palabra anterior a edu, que seria el nombre de la universidad
    nombres_universidades_sin_repetir = list(set(nombres_universidades)) # se usa list para limpiar de palabras repetidas
    return nombres_universidades_sin_repetir

def tema_1_b(correos):
    nombres_universidades = []
    for correo in correos:
        correo_split = correo.split('.')
        if 'ec' in correo_split and 'edu' in correo_split:
            ubicacion_nombre = correo_split.index('edu') - 1
            nombre_universidad = correo_split[ubicacion_nombre].upper() # convertirlo en mayuscula tambien
            nombres_universidades.append(nombre_universidad) # extraer la palabra anterior a edu, que seria el nombre de la universidad
    nombres_universidades_sin_repetir = list(set(nombres_universidades)) # se usa list para limpiar de palabras repetidas
    return nombres_universidades_sin_repetir

def tema_1_c(usuario, sigla, lista):
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

def tema_1_c_menu(lista):
    usuario_input = input('Ingrese el usuario: ')
    sigla_input = input('Ingrese el nombre/sigla de la universidad: ').lower()
    correo = tema_1_c(usuario_input, sigla_input, lista)
    print("El correo electronico del usuario es:")
    print(correo)


""" TEMA 2 """