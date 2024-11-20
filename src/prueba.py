
def leerArchivo(ruta):
    with open (ruta, "r") as archivo:
        archivo.readline()
        for linea in archivo:
            lst_datos = linea.split(', ')
            nombre = lst_datos[0];
            descripcion = lst_datos[1];
            atributo = lst_datos[2]
            print(f'Nombre:{nombre}Descripcion:{descripcion}atributo:{atributo}')


leerArchivo("src/archivoCartasTrampa.txt")
