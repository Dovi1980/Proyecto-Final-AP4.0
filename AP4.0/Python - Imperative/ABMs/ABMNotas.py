
from TDAs import TDAInscriptos
from TDAs import TDAabm
from TXTs import CargaTXTs

#---------------------------------------------
#----- Consulta y Modificacion -----
def consulta_modifica(ln_insc,ESprofe):
    profe=False
    y = "S"
    while y == "S" or y != "N":
        nombre = str(input("\nIngrese alumno a Consultar/Modificar: ")).upper()
        for n_elemento in ln_insc:
            if ESprofe == TDAInscriptos.demeProfesor(n_elemento) and nombre == TDAInscriptos.demeNombre(n_elemento):
                print("Los datos consultados son: ", TDAInscriptos.repInscripciones(n_elemento))
                ok=input("Desea continuar con la modificación de la Nota?(S/N): ").upper()
                while ok != "S" and ok !="N":
                    print("\nLos valores ingresados no son correctos...")       
                    ok= str(input("Desea continuar con la modificacion de la Nota?(S/N): ")).upper()
                else:
                    if ok == "S":
                        profe=True
                        TDAabm.modifico(ln_insc, n_elemento, profe)
                        print("\nOK! --> Modificación realizada...")
                        break
                    elif ok == "N":
                        return
        else:
                print("El alumno no pertenece a su catedra...")
        y = str(input("Desea realizar otra Consulta o Modificación?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("Desea realizar otra Consulta o Modificación?(S/N): ")).upper()
    return 


#----- ABM Notas - Menu ------------
def abm_inscriptos(profeOK):
    print()
    y = "S"
    while y == "S" or y != "N":
        print("""
    ||----------------------------------------------||
    ||----   Menu de Carga: Notas Alumnos    ----||
    ||-----             Elija una opción             -------||     
    ||----   1 > Consultar / Modificar Nota    -----||
    ||------                   0 > Salir                  -------||     
    ||----------------------------------------------||
    """)
        try:
            op=int(input("Ingrese una opción: "))
            if op == 0:
                return
            elif op == 1:
                consulta_modifica(CargaTXTs.cargaTXTinscripciones(),profeOK)
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

