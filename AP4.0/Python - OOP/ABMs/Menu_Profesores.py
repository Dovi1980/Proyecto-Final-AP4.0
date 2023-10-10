
from Login.Clear import limpiar_pantalla
from ABMs.ABMNotas import consulta_modifica
from TXTs.CargaTXTs import cargaTXTinscripciones

#---------------------------------------------
#---- ABM Notas - Menu ----

def abm_notas(profeOK):
    y = "S"
    while y == "S" or y != "N":
        limpiar_pantalla()
        print()
        print(f"\nBuen dia {profeOK} ...")
        print("""
    ||==============================================||
    ||=====    Menu de Carga: Notas Alumnos    =====||
    ||==============================================||          
    ||=====           Elija una opción         =====||     
    ||=====   1 > Consultar / Modificar Nota   =====||
    ||=====              0 > Salir             =====||     
    ||==============================================||
    """)
        try:
            op=int(input("    Ingrese una opción: "))
            if op == 0:
                return
            elif op == 1:
                consulta_modifica(cargaTXTinscripciones(),profeOK)
                break
            else:
                print("Opción erronea...")
        except ValueError:
            print("El valor ingresado no es valido....")
        y = str(input("\nDesea volver al Menú de Profesores? - (S/N): ")).upper()
        while y != "S" and y !="N":
            print("El valor ingresado no es valido...")       
            y = str(input("\nDesea volver al Menú de Profesores? - (S/N): ")).upper()
    return