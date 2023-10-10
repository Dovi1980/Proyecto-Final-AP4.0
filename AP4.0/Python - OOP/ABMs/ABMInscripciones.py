
from ABMs.ABM import *
from Clases.Inscriptos import Inscripto
from ABMs.FechaOK import control_fecha
from ABMs.dniOK import control_DNI
from ABMs.Consulta_Pantalla import reprDatos

#---------------------------------------------
#---- Alta ----

def altaExamen(la_insc,enca):
    y = "S"
    while y == "S" or y != "N":
        fecha = control_fecha()
        nombre = str(input("Apellido y Nombre del alumno: ")).upper()
        dni = control_DNI()       
        for a_elemento in la_insc:
            if dni == a_elemento.DNI:
                print("\nDNI existente en base de datos...")
                print("Alta CANCELADA...")          
                return
            else:
                continue
        materia = str(input("Materia a rendir: ")).upper()
        profesor = str(input("Profesor a evaluar: ")).upper()
        curso = str(input("Curso: ")).upper()
        division = str(input("División: ")).upper()
        nota = str(input("Nota (['-1' si no rindio aún): "))
        actividad = "ESTUDIANTE"
        actualiza = enca
        alta(nombre,dni,actividad,fecha,materia,profesor,curso,division,nota,actualiza)
        print("\nOK! --> Alta completa...")          
        y = str(input("\nDesea realizar otra Alta?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("\nDesea realizar otra Alta?(S/N): ")).upper()
    return
            
#-----Baja-----
def bajaExamen(lb_insc):
    y = "S"
    while y == "S" or y != "N":
        print("A continuacion indique DNI del alumno a dar de baja de la mesa de examen... ")
        dni_a = control_DNI()
        nombre = str(input("Apellido y Nombre del alumno: ")).upper()
        for b_elemento in lb_insc:
            if nombre == b_elemento.Nombre and dni_a == b_elemento.DNI:
                print("\nLos datos a eliminar son:")                           
                print(reprDatos(b_elemento)) 
                ok=input("Continuar...?(S/N)").upper()
                while ok != "S" and ok !="N":
                    print("Los valores ingresados no son correctos...")       
                    ok= str(input("\nDesea continuar con la baja?(S/N): ")).upper()
                if ok == "S":
                    baja(lb_insc,b_elemento)
                    print("\nOK! --> Baja realizada...")
                else:
                    return
        y = str(input("\nDesea realizar otra Baja?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("\nDesea realizar otra Baja?(S/N): ")).upper()
    return    
        
#-----Modificacion-----
def modificoExamen(lm_insc,enca):
    profe=False
    y = "S"
    while y == "S" or y != "N":
        print("A continuacion indique DNI del alumno a modificar sus datos de inscripción... ")
        dni_a = control_DNI()
        nombre = str(input("Apellido y Nombre del alumno: ")).upper()
        for m_elemento in lm_insc:
            if dni_a == m_elemento.DNI and nombre == m_elemento.Nombre:
                print("\nLos datos a modificar son:")                       
                print(reprDatos(m_elemento))
                ok=input("\nContinuar...?(S/N)").upper()
                while ok != "S" and ok !="N":
                    print("\nLos valores ingresados no son correctos...")       
                    ok= str(input("Desea continuar con la modificacion de datos?(S/N): ")).upper()
                else:
                    if ok == "S":
                        modifico(lm_insc,m_elemento,profe,enca)
                        print("\nOK! --> Modificación realizada...")
                    elif ok == "N":
                        return
        y = str(input("\nDesea realizar otra Modificación?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("\nDesea realizar otra Modificación?(S/N): ")).upper()
    return    

