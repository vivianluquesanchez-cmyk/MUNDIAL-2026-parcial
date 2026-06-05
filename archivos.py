import os
def crear_archivo(nombre="torneo.txt"):
    if not os.path.exists(nombre):
       archivo = open(nombre, "a")
       archivo.close()
def cargarEnArchivo(nombre,texto):
    archivo=open(nombre,"a")
    archivo.write(texto)
    archivo.close()
def cuentaLineas(nombre): #Sirve para ver si todos los equipos están cargados o no.
    archivo=open(nombre,"a")
    lineaCnt=0
    for line in archivo:
        lineaCnt+=1
    archivo.close()
    return lineaCnt
