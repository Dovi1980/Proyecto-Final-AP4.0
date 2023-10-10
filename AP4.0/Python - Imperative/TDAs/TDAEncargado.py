
from ABMs import ABMInscripciones

#---------------------------------------------
#--- Datos Encargados ---
def crear (nombre,dni):
    return {"nombre":nombre, "dni":dni}

def demeNombre(encargado):
    return encargado["nombre"]

def modificarNombre(encargado,nombre):
    encargado["nombre"] = nombre
    return

def demeDni(encargado):
    return encargado["dni"]

def modificarDni(encargado,dni):
    encargado["dni"] = dni
    return

def repEncargado(encargado):
    return "Nombre: " + encargado["nombre"] + " -- " + "DNI: "+ encargado["dni"] 

#--- Login Encargados ---
def login_E(encargados):
    y = "S"
    while y == "S" or y != "N":
        try:
            nombre = input("\nIngrese su Nombre: ").upper()
            dni_enc= str(input("Ingrese su DNI: "))
            for dic in encargados:
                if (7<= len(dni_enc) <9) and nombre == demeNombre(dic) and dni_enc == demeDni(dic):
                    print(f"Buen dia, {demeNombre(dic)}, que desea realizar?")
                    ABMInscripciones.abm_inscriptos()
                    return
            else:
                try:
                    raise KeyError ("Ingreso no válido...")
                except KeyError as DNIinexistente:
                    print(DNIinexistente)             
        except ValueError:
            print("\nLos valores ingresados no son correctos...")
        y = str(input("Desea intentar nuevanente?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("Desea intentar nuevanente?(S/N): ")).upper()
    return 
