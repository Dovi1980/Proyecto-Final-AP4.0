
from Login.Clear import limpiar_pantalla
from ABMs.Consultas_Varias import *

#--------------------------------------------------------
#---- Menu Consultas ----

def consultasVarias(lc_insc):
    y = "S"
    while y == "S" or y != "N":
        limpiar_pantalla()
        print()
        print("""
    ||===============================================||
    ||==========     CONSULTAS VARIAS      ==========||  
    ||===============================================||              
    ||==========     Listar por:           ==========||
    ||==========       1 > DNI Inscripto   ==========||       
    ||==========       2 > Profesor        ==========||
    ||==========       3 > Fecha Examen    ==========||
    ||==========       0 > Salir           ==========||
    ||===============================================||
    """)
        try:
            op=int(input("    Ingrese una opción: "))
            if op == 0:
                return
            else:
                if op == 1:
                    print(consultaDNI(lc_insc))
                elif op == 2:
                    print(consultaProfe(lc_insc))
                elif op == 3:
                    print(consultaFecha(lc_insc))
                else:
                    print("Opción erronea...")
        except ValueError:
            print("El valor ingresado no es valido....")
        y = str(input("\nDesea volver a las Consultas Varias? - (S/N): ")).upper()
        while y != "S" and y !="N":
            print("El valor ingresado no es valido...")       
            y = str(input("\nDesea volver a las Consultas Varias? - (S/N): ")).upper()
    return
    

