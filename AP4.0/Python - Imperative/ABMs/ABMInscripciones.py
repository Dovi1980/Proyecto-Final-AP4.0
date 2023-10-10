
from TXTs import CargaTXTs
from TDAs import TDAabm
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
def altaExamen(la_insc):
    y = "S"
    while y == "S" or y != "N":
        fecha = control_fecha()
        nombre = str(input("Apellido y Nombre del alumno: ")).upper()
        materia = str(input("Materia a rendir: ")).upper()
        profesor = str(input("Profesor a evaluar: ")).upper()
        curso = str(input("Curso: ")).upper()
        division = str(input("División: ")).upper()
        nota = str(input("Nota (´-1´ si no rindio aún): "))
        TDAabm.alta(fecha,nombre,materia,profesor,curso,division,nota)
        print("\nOK! --> Alta completa...")
        y = str(input("Desea realizar otra Alta?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("Desea realizar otra Alta?(S/N): ")).upper()
    return
            
#-----Baja-----
def bajaExamen(lb_insc):
    y = "S"
    while y == "S" or y != "N":
        fecha = control_fecha()
        nombre = str(input("Alumno a dar de baja de la mesa: ")).upper()
        for b_elemento in lb_insc:
            if (fecha == TDAInscriptos.demeFecha(b_elemento)) and (nombre == TDAInscriptos.demeNombre(b_elemento)):
                print("Los datos a eliminar son: ", TDAInscriptos.repInscripciones(b_elemento))
                ok=input("Continuar...?(S/N)").upper()
                while ok != "S" and ok !="N":
                    print("Los valores ingresados no son correctos...")       
                    ok= str(input("\nDesea continuar con la baja?(S/N): ")).upper()
                if ok == "S":
                    TDAabm.baja(lb_insc,b_elemento)
                    print("\nOK! --> Baja realizada...")
                else:
                    return
        y = str(input("Desea realizar otra Baja?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("Desea realizar otra Baja?(S/N): ")).upper()
    return    
        
#-----Modificacion-----
def modificoExamen(lm_insc):
    profe=False
    y = "S"
    while y == "S" or y != "N":
        nombre = str(input("\nAlumno a modificar: ")).upper()
        materia = str(input("Materia anotada: ")).upper()
        for m_elemento in lm_insc:
            if (materia == TDAInscriptos.demeMateria(m_elemento)) and \
                (nombre == TDAInscriptos.demeNombre(m_elemento)):
                print("\nLos datos a modificar son : ", TDAInscriptos.repInscripciones(m_elemento))
                ok=input("Continuar...?(S/N)").upper()
                while ok != "S" and ok !="N":
                    print("\nLos valores ingresados no son correctos...")       
                    ok= str(input("Desea continuar con la modificacion de datos?(S/N): ")).upper()
                else:
                    if ok == "S":
                        TDAabm.modifico(lm_insc,m_elemento,profe)
                        print("\nOK! --> Modificación realizada...")
                    elif ok == "N":
                        return
        y = str(input("Desea realizar otra Modificación?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("Desea realizar otra Modificación?(S/N): ")).upper()
    return    

#-----Consulta-----
def consultas(lc_insc):
    y = "S"
    while y == "S" or y != "N":
        nombre = str(input("\nAlumno a consultar: ")).upper()
        materia = str(input("Materia anotada: ")).upper()
        for c_elemento in lc_insc:
            if (materia == TDAInscriptos.demeMateria(c_elemento)) and (nombre == TDAInscriptos.demeNombre(c_elemento)):
                print("Los datos del alumno inscripto son:")
                print(TDAInscriptos.repInscripciones(c_elemento))
                break
        else:
            print("\nEl alumno no se encuentra anotado aún en ninguna mesa de examen...") 
        y = str(input("Desea realizar otra Consulta?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("Desea realizar otra Consulta?(S/N): ")).upper()
    return       


#-------------- ABM Inscriptos - Menu ------------------------------------------
def abm_inscriptos():
    print()
    y = "S"
    while y == "S" or y != "N":
        print("""
    @-----------------------------------------------@
    @----------    ABM - Inscripciones     ----------@      
    @----------        Elija una opción        ----------@
    @----------          1 > Alta                  ----------@       
    @----------          2 > Baja                  ----------@
    @----------          3 > Modificacion     ----------@
    @----------          4 > Consulta           ----------@
    @----------          0 > Salir                  ----------@
    @-----------------------------------------------@
    """)
        try:
            op=int(input("Ingrese una opción: "))
            if op == 0:
                return
            else:
                if op == 1:
                    altaExamen(CargaTXTs.cargaTXTinscripciones())
                elif op == 2:
                    bajaExamen(CargaTXTs.cargaTXTinscripciones())
                elif op == 3:
                    modificoExamen(CargaTXTs.cargaTXTinscripciones()) 
                elif op == 4:
                    consultas(CargaTXTs.cargaTXTinscripciones())        
                else:
                    print("Opción erronea...")
        except ValueError:
            print("El valor ingresado no es valido....")
        y = str(input("\nDesea volver al Menú de Encargados? - (S/N): ")).upper()
        while y != "S" and y !="N":
            print("El valor ingresado no es valido...")       
            y = str(input("\nDesea volver al Menú de Encargados? - (S/N): ")).upper()
    return
    


