
from ABMs import ABMNotas

#---------------------------------------------
#--- Datos Profesores ---
def crear (nombre,materia,curso,division):
    return {"nombre":nombre, "materia":materia, "curso":curso, "division":division}

def demeNombre(profesor):
    return profesor["nombre"]

def modificarNombre(profesor,nombre):
    profesor["nombre"] = nombre
    return

def demeMateria(profesor):
    return profesor["materia"]

def modificarMateria(profesor,materia):
    profesor["materia"] = materia
    return

def demeCurso(profesor):
    return profesor["curso"]

def modificarCurso(profesor,curso):
    profesor["curso"] = curso
    return

def demeDivision(profesor):
    return profesor["division"]

def modificarDivision(profesor,division):
    profesor["division"] = division
    return

def repProfesor (profesor):
    return "Nombre: "+profesor["nombre"] +" -- "+ "Materia: "+profesor["materia"] + \
        " -- "+ "Curso: "+profesor["curso"] +" -- "+ "Division: "+profesor["division"]

#--- Login Profesores ---
def login_P(profesores):
    y = "S"
    while y == "S" or y != "N":
        try:
            nombre = str(input("Ingrese su nombre: ")).upper()
            materia = str(input("Ingrese su Materia: ")).upper()
            curso = str(input("Curso: ")).upper()
            division = str(input("División: ")).upper()
            for dic in profesores:
                if nombre == demeNombre(dic) and materia == demeMateria(dic) \
                    and curso == demeCurso(dic) and division == demeDivision(dic):
                    print(f"Buen dia {demeNombre(dic)} ...")
                    ABMNotas.abm_inscriptos(nombre)
                    return
            else:
                try:
                    raise KeyError ("Ingreso no válido....")
                except KeyError as PROFESOR_inexistente:
                    print(PROFESOR_inexistente)
        except ValueError:
            print("Los valores ingresados no son correctos...")
        y = str(input("\nDesea intentar nuevamente?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("\nDesea intentar nuevamente?(S/N): ")).upper()
    return 
