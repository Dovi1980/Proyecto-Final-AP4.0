
from TDAs import TDAInscriptos

from datetime import datetime

#---------------------------------------------
def control_fecha():
    ok=True
    while ok:
        fecha_ing=str(input("\nFecha de examen (dd/mm/aa): "))
        try:
            fecha_ok = datetime.strptime(fecha_ing, "%d/%m/%y")
            return fecha_ing
        except ValueError:
            print('\nEl formato de fecha es incorrecto, intente nuevamente...')

#---------------------------------------------
#-----Alta-----
def alta (fecha,nombre,materia,profesor,curso,division,nota):
    inscripciones = open("./TXTs/inscripciones.txt", "a+")
    inscripciones.write(fecha +","+ nombre +","+ materia +","+ profesor +","+ curso +","+ division +","+ nota +"\n")
    inscripciones.close()

#-----Baja-----
def baja (listado, datos):
    listado.remove(datos)
    inscripciones = open("./TXTs/inscripciones.txt", "w")
    inscripciones.seek(0)
    for i in range(0, len(listado)):
        inscripciones.writelines(",".join(listado[i].values()))
        inscripciones.write("\n")
    inscripciones.close()

#-----Modificación-----
def modifico (listado, datos, profeSI):
    if profeSI:
        fecha = TDAInscriptos.demeFecha(datos)
        nombre = TDAInscriptos.demeNombre(datos)
        materia = TDAInscriptos.demeMateria(datos)
        profesor = TDAInscriptos.demeProfesor(datos)
        curso = TDAInscriptos.demeCurso(datos)
        division = TDAInscriptos.demeDivision(datos)
        nota_actual = str(input("Actualice la Nota: "))
        baja(listado, datos)
        alta(fecha,nombre,materia,profesor,curso,division,nota_actual)
    else:
        baja(listado, datos)
        fecha = control_fecha()
        nombre = str(input("Apellido y Nombre del alumno: ")).upper()
        materia = str(input("Materia a rendir: ")).upper()
        profesor = str(input("Profesor a evaluar: ")).upper()
        curso = str(input("Curso: ")).upper()
        division = str(input("División: ")).upper()
        nota = str(input("Nota (´-1´ si no rindio aún): "))
        alta(fecha,nombre,materia,profesor,curso,division,nota)
