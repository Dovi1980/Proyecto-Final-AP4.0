
from TDAs import TDAProfesor
from TDAs import TDAEncargado

#----- PP - Menú Inicial -----
def menuPP(profesores,encargados):
    print()
    y = "S"
    while y == "S" or y != "N":
        print("""
    ------------------------------------------------------
    -------->>>     Login - Menú Principal     <<<--------
    -------->>>           Elija una opción          <<<--------       
    -------->>>             1 > Encargado          <<<--------
    -------->>>             2 > Profesor             <<<--------    
    -------->>>             0 > Salir                   <<<--------
    ------------------------------------------------------
    """)
        try:
            op=int(input("Ingrese una opción: "))
            if op == 0:
                return
            elif op == 1:
                TDAEncargado.login_E(encargados)
            elif op == 2:
                TDAProfesor.login_P(profesores)
            else:
                print("Opción incorrecta...")
        except ValueError:
            print("El valor ingresado no es valido....")
        y = str(input("\nDesea volver al Menú Principal? - (S/N): ")).upper()
        while y != "S" and y !="N":
            print("El valor ingresado no es valido...")       
            y = str(input("\nDesea volver al Menú Principal? - (S/N): ")).upper()
    return

