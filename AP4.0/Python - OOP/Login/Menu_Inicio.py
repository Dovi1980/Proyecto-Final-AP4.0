
from Login.Clear import limpiar_pantalla
from Login.Login_E import login_E
from Login.Login_P import login_P

#------------------------------------------------------------
#---- PP - Menú Inicial ----
def menuPP(profesores,encargados):
    print()
    y = "S"
    while y == "S" or y != "N":
        limpiar_pantalla()
        print("""
    ######################################################
    #|--------------------------------------------------|#
    #|------->>>          BIENVENIDO          <<<-------|#
    #|--------------------------------------------------|#     
    ###################################################### 
    #|--------------------------------------------------|#
    #|------>>>     LOGIN - MENU PRINCIPAL     <<<------|#
    #|------>>>        Elija una opción        <<<------|#
    #|------>>>         1 > Encargado          <<<------|#
    #|------>>>         2 > Profesor           <<<------|#
    #|------>>>         0 > Salir              <<<------|#
    #|--------------------------------------------------|#
    ######################################################
    
    """)
        try:
            print()
            op=int(input("    Ingrese una opción: "))
            if op == 0:
                return
            elif op == 1:
                login_E(encargados)
            elif op == 2:
                login_P(profesores)
            else:
                print("Opción incorrecta...")
        except ValueError:
            print("El valor ingresado no es valido....")
        y = str(input("\nDesea volver al Menú Principal? - (S/N): ")).upper()
        while y != "S" and y !="N":
            print("El valor ingresado no es valido...")       
            y = str(input("\nDesea volver al Menú Principal? - (S/N): ")).upper()
    return

