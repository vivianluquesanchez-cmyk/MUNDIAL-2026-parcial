import os
def crear_archivo(nombre="torneo.txt"):
    if not os.path.exists(nombre):
       archivo = open(nombre, "a")
       archivo.close()
def cargarEnArchivo(nombre,texto):
    archivo=open(nombre,"a")
    archivo.write(texto)
    archivo.close()
