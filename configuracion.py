from archivos import cargarEnArchivo
def crearTorneo():
    seguro=0
    while seguro!=1:
        nombreTor=input("Ingresar nombre del Torneo: ")
        fechaIni=input("Ingrese fecha de inicio (DD/MM/AAAA): ")
        fechaFin=input("Ingrese fecha de la Final(DD/MM/AAAA):")
        seguro=int(input("Está seguro? Marque 1 para confirmar. "))
    torneoTxt=f"{nombreTor}-{fechaIni}-{fechaFin}\n"
    cargarEnArchivo("torneo.txt",torneoTxt)
    print("Torneo creado con éxito")

def cargarEquipos():
    seguro = 0
    while seguro != 1:
        pais =  input("Ingresar el nombre de la selccion: ")
        abrev =  input("Ingresar el abreviacion de la selccion : ")
        tel =  input("Ingresar el telefono de la selccion : ")
        conf =  input("Ingresar la confederacion de la seleccion : ")
        grupo = input("Ingresar el grupo de la seleccion : ")
        idEquipo = grupo + tel
        print("El id de la seleccion es : ",idEquipo)
        seguro = int(input("Esta seguro? Marque 1 para confirmar. "))
    equipoTxt=f"{pais}-{abrev}-{tel}-{conf}-{grupo}-{idEquipo}\n"
    cargarEnArchivo("equipos.txt",equipoTxt)
    print("Equipo cargado con éxito")


#Este hay que revisar porque mezcla cosas de la opcion 1 y 2 del menu principal
def cargarPartidos():
    seguro = 0
    while seguro != 1:
        fecha =  input("Ingresar la fecha del partido : ")
        hora =  input("Ingresar la hora del partido : ")
        #aca podemos llegar a ver o del tema de la fases
        lugar =  input("Ingresar el lugar del partido : ")
        idLocal =  input("Local : ")
        idVisit = input("Visitante : ")
        golesLocal = int(input("GOL Local : "))
        golesVisit = int(input("GOL Visitante : "))
        #dependiendo de eso agregar para lo de penales
        seguro = int(input("Esta seguro? Marque 1 para confirmar. "))
    archivo=open("partidos.txt","a")
    archivo.write(f"\n{fecha}-{hora}-{lugar}-{idLocal}-{idVisit}-{golesLocal}-{golesVisit}") #Sujeto a cambios
    archivo.close()    
    print("Partido cargado con exito")
