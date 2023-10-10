
#---------------------------------------------
#--- Datos Inscriptos ---
def crear (fecha,nombre,materia,profesor,curso,division,nota):
    return {"fecha":fecha, "nombre":nombre, "materia":materia, "profesor":profesor, "curso":curso, "division":division, "nota":nota}

def demeFecha(inscriptos):
    return inscriptos["fecha"]

def modificarFecha(inscriptos, fecha):
    inscriptos["fecha"]=fecha

def demeNombre(inscriptos):
    return inscriptos["nombre"]

def modificarNombre(inscriptos, nombre):
    inscriptos["nombre"]=nombre

def demeMateria(inscriptos):
    return inscriptos["materia"]

def modificarMateria(inscriptos, materia):
    inscriptos["materia"]=materia

def demeProfesor(inscriptos):
    return inscriptos["profesor"]

def modificarProfesor(inscriptos, profesor):
    inscriptos["profesor"]=profesor

def demeCurso(inscriptos):
    return inscriptos["curso"]

def modificarCurso(inscriptos, curso):
    inscriptos["curso"]=curso

def demeDivision(inscriptos):
    return inscriptos["division"]

def modificarDivision(inscriptos, division):
    inscriptos["division"]=division

def demeNota(inscriptos):
    return inscriptos["nota"]

def modificarNota(inscriptos, nota):
    inscriptos["nota"]=nota

def repInscripciones (inscriptos):
    return "Fecha Examen: "+inscriptos["fecha"] +" -- "+ "Nombre: "+ \
        inscriptos["nombre"] +" -- "+ "Materia: "+inscriptos["materia"] +" -- " \
            + "Profesor: "+inscriptos["profesor"] +" -- "+ "Curso: "+inscriptos["curso"] + \
                " -- "+ "Division: "+inscriptos["division"] +" -- "+ "Nota: "+inscriptos["nota"]

