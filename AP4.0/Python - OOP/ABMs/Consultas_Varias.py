
from ABMs.Consultas_Filtro import *
from ABMs.dniOK import control_DNI
from ABMs.FechaOK import control_fecha
from prettytable import PrettyTable

#--------------------------------------------------------
#---- Filtrado ----

def consulta(lc_insc,dato,flag):
    tabla = PrettyTable()
    tabla.field_names = ["ALUMN@".center(25), "FECHA EXAMEN", "MATERIA".center(20), "PROFESOR".center(25),\
                          "CURSO", "DIVISION", "NOTA", "ULTIMA MODIFICACION"]
    
    if flag == "DNI":
        alumnos_filtrados = filter((lambda alumno: filtrar_dni(alumno, dato)), lc_insc)
    elif flag == "Profe":
        alumnos_filtrados = filter((lambda alumno: filtrar_profesor(alumno, dato)), lc_insc)    
    else:
        alumnos_filtrados = filter((lambda alumno: filtrar_fecha(alumno, dato)), lc_insc)
    
    alumnos_filtrados_lista = list(alumnos_filtrados)
    for alumno in alumnos_filtrados_lista:
        tabla.add_row([alumno.Nombre, alumno.Fecha, alumno.Materia,\
                    alumno.Profesor, alumno.Curso, alumno.Division, \
                        alumno.Nota, alumno.Update])
    return tabla

#---- x DNI ----

def consultaDNI(lc_insc):
    print("\nA continuacion indique DNI del alumno a consultar... ")
    dni_a = control_DNI()
    flag="DNI"
    return consulta(lc_insc,dni_a,flag)
    
#---- x Profesor ----

def consultaProfe(lc_insc): 
    profe = str(input("\nIndique Nombre del Profesor: ")).upper()
    flag="Profe"
    return consulta(lc_insc,profe,flag)

#---- x Fecha Examen ----

def consultaFecha(lc_insc):
    print("\nA continuacion indique fecha de examen a consultar... ")
    fecha = control_fecha()
    flag="Fecha"
    return consulta(lc_insc,fecha,flag)