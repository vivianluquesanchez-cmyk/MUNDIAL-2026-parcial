import os
from configuracion import crearTorneo,cargarEquipos,cargarPartidos
from archivos import crear_archivo

def menu():
    print("Menu de Carga")
    print("1) Crear Torneo")
    print("2) Cargar Equipos")
    print("3) Cargar Partidos")
    print("4) Volver")

crear_archivo("torneo.txt")
menu()
completos=[False,False,False]
opc=int(input("Ingrese una opción: "))

while opc!=4:
    if os.path.getsize("torneo.txt")>0:
        completos[0]=True

    if(opc==1 and not completos[0]):
        crearTorneo()
        completos[0] = True
    elif(opc==2 and completos[0]):
        cargarEquipos()
        completos[1] = True
    elif(opc==3 and completos[1]):
        cargarPartidos()
        completos[2] = True
    else:
        print("Opción no valida. Intentelo otra vez.")
        input("Presione Enter para continuar...")

    print("\033[H\033[J")
    menu()
    opc = int(input("Ingrese una opcion: "))
