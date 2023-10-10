from Clases.Profesores import Profesor
from Clases.Encargados import Encargado

#------------------------------------------------------------
#---- Validacion con Recurción ----

def isEncargadoOK(encargados, nombre, dni):
    if not encargados:
        return False
    if encargados[0].Nombre == nombre and encargados[0].DNI == dni:
        return True
    return isEncargadoOK(encargados[1:], nombre, dni)

def isProfesorOK(profesores,nombre,materia,curso,division):
    if not profesores:
        return False
    if profesores[0].Nombre == nombre and profesores[0].Materia == materia\
        and profesores[0].Curso == curso and profesores[0].Division == division:
        return True
    return isProfesorOK(profesores[1:],nombre,materia,curso,division)

