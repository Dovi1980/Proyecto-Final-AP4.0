
from Clases.Inscriptos import Inscripto
from ABMs.FechaOK import control_fecha
from ABMs.dniOK import control_DNI

#---------------------------------------------
#----- Alta -----

def alta (nombre,dni,actividad,fecha,materia,profesor,curso,division,nota,actualiza):
    inscripciones = open("./TXTs/inscripciones.txt", "a+")
    inscripciones.write(nombre +","+ dni +","+ actividad +","+ fecha +","+ materia +","+ \
                        profesor +","+ curso +","+ division +","+ nota +","+ actualiza +"\n")
    inscripciones.close()

#----- Baja -----

def baja (listado, datos):
    listado.remove(datos)
    inscripciones = open("./TXTs/inscripciones.txt", "w")
    inscripciones.seek(0)
    for i in range(0, len(listado)):
        inscripciones.writelines(",".join((listado[i].Nombre, listado[i].DNI, listado[i].Actividad,\
                                        listado[i].Fecha, listado[i].Materia, listado[i].Profesor, \
                                        listado[i].Curso, listado[i].Division, listado[i].Nota, listado[i].Update)))
        inscripciones.write("\n")
    inscripciones.close()

#----- Modificación -----

def modifico (listado, datos, profeSI, quien_modifica):
    if profeSI:
        fecha = datos.Fecha
        nombre = datos.Nombre
        dni = datos.DNI
        materia = datos.Materia
        profesor = datos.Profesor
        curso = datos.Curso
        division = datos.Division
        nota_actual = str(input("Actualice la Nota: "))
        actividad = "ESTUDIANTE"
        actualiza = profesor
        baja(listado, datos)
        alta(nombre,dni,actividad,fecha,materia,profesor,curso,division,nota_actual,actualiza)
    else:
        baja(listado, datos)
        fecha = control_fecha()
        nombre = str(input("Apellido y Nombre del alumno: ")).upper()
        dni = control_DNI()       
        materia = str(input("Materia a rendir: ")).upper()
        profesor = str(input("Profesor a evaluar: ")).upper()
        curso = str(input("Curso: ")).upper()
        division = str(input("División: ")).upper()
        nota = str(input("Nota (¨-1¨ si no rindio aún): "))
        actividad = "ESTUDIANTE"
        actualiza = quien_modifica
        alta(nombre,dni,actividad,fecha,materia,profesor,curso,division,nota,actualiza)
