
from Login.Clear import limpiar_pantalla
from TXTs.CargaTXTs import cargaTXTinscripciones
from ABMs.ABMInscripciones import *
from ABMs.Consultas_Menu import consultasVarias

#---------------------------------------------
#---- ABM Inscriptos - Menu ----

def abm_inscriptos(enca):
    y = "S"
    while y == "S" or y != "N":
        limpiar_pantalla()
        print()
        print(f"\nBuen dia, {enca}, que desea realizar?")
        print("""
    ||===============================================||
    ||==========    ABM - Inscripciones    ==========||  
    ||===============================================||              
    ||==========     Elija una opción      ==========||
    ||==========       1 > Alta            ==========||       
    ||==========       2 > Baja            ==========||
    ||==========       3 > Modificacion    ==========||
    ||==========       4 > Consultas       ==========||
    ||==========       0 > Salir           ==========||
    ||===============================================||
    """)
        try:
            op=int(input("    Ingrese una opción: "))
            if op == 0:
                return
            else:
                if op == 1:
                    altaExamen(cargaTXTinscripciones(),enca)
                elif op == 2:
                    bajaExamen(cargaTXTinscripciones())
                elif op == 3:
                    modificoExamen(cargaTXTinscripciones(),enca) 
                elif op == 4:
                    consultasVarias(cargaTXTinscripciones())        
                else:
                    print("Opción erronea...")
        except ValueError:
            print("El valor ingresado no es valido....")
        y = str(input("\nDesea volver al Menú de Encargados? - (S/N): ")).upper()
        while y != "S" and y !="N":
            print("El valor ingresado no es valido...")       
            y = str(input("\nDesea volver al Menú de Encargados? - (S/N): ")).upper()
    return