
from Clases.Inscriptos import Inscripto
from ABMs.ABM import *
from TXTs.CargaTXTs import *
from ABMs.Consulta_Pantalla import reprDatos

#--------------------------------------------------------
#---- Consulta y Modificacion ----

def consulta_modifica(ln_insc,quien_modifica):
    profe=False
    y = "S"
    while y == "S" or y != "N":
        print("A continuacion indique DNI del alumno a consultar... ")
        dni_a = control_DNI()
        for n_elemento in ln_insc:
            if dni_a == n_elemento.DNI:
                print("\nLos datos consultados son:")                                   
                print(reprDatos(n_elemento))
                ok=input("\nDesea continuar con la modificación de la Nota?(S/N): ").upper()
                while ok != "S" and ok !="N":
                    print("\nLos valores ingresados no son correctos...")       
                    ok= str(input("\nDesea continuar con la modificacion de la Nota?(S/N): ")).upper()
                else:
                    if ok == "S":
                        profe=True
                        modifico(ln_insc,n_elemento,profe,quien_modifica)
                        print("\nOK! --> Modificación realizada...")
                        break
                    elif ok == "N":
                        return
        else:
                print("El alumno no pertenece a su catedra...")
        y = str(input("\nDesea realizar otra Consulta o Modificación?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("\nDesea realizar otra Consulta o Modificación?(S/N): ")).upper()
    return 



