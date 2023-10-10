
from Clases.Inscriptos import Inscripto

#--------------------------------------------------------------------------------
# Estos filtros se crearon con el fin de que en el caso de realizar una consulta
# y en la base de datos exista por error información duplicada, el 
# encargado lo note y pueda realizar las modificaciones correspondientes...
# 
# También se aplican como Funciones de Orden Superior en "Consultas_Varias".
#--------------------------------------------------------------------------------

def filtrar_dni(dato_alumno, dni):
    if dato_alumno.DNI != dni:
        return False
    return True
#---
def filtrar_profesor(dato_alumno, profesor):
    if dato_alumno.Profesor != profesor:
        return False
    return True
#---
def filtrar_fecha(dato_alumno, fecha):
    if dato_alumno.Fecha != fecha:
        return False
    return True
