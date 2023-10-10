
from ABMs.Menu_Encargados import abm_inscriptos
from ABMs.dniOK import control_DNI
from Login.Validacion import isEncargadoOK

#------------------------------------------------------------
#---- Login Encargados ----

def login_E(encargados):
    print()
    y = "S"
    while y == "S" or y != "N":
        try:
            nombre = input("\nIngrese su Nombre: ").upper()
            dni_enc= control_DNI()
            if isEncargadoOK(encargados,nombre,dni_enc):               
                abm_inscriptos(nombre)
                return
            else:
                try:
                    raise KeyError ("Ingreso no válido...")
                except KeyError as ENCARGADO_inexistente:
                    print(ENCARGADO_inexistente)             
        except ValueError:
            print("\nLos valores ingresados no son correctos...")
        y = str(input("Desea intentar nuevanente?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("Desea intentar nuevanente?(S/N): ")).upper()
    return 
