
from ABMs.Menu_Profesores import abm_notas 
from Login.Validacion import isProfesorOK

#------------------------------------------------------------
#---- Login Profesores ----

def login_P(profesores):
    print()
    y = "S"
    while y == "S" or y != "N":
        try:
            nombre = str(input("Ingrese su nombre: ")).upper()
            materia = str(input("Ingrese su Materia: ")).upper()
            curso = str(input("Curso: ")).upper()
            division = str(input("División: ")).upper()
            if isProfesorOK(profesores,nombre,materia,curso,division):
                abm_notas(nombre)
                return
            else:
                try:
                    raise KeyError ("Ingreso no válido....")
                except KeyError as PROFESOR_inexistente:
                    print(PROFESOR_inexistente)
        except ValueError:
            print("Los valores ingresados no son correctos...")
        y = str(input("\nDesea intentar nuevamente?(S/N): ")).upper()
        while y != "S" and y !="N":
            print("Los valores ingresados no son correctos...")       
            y = str(input("\nDesea intentar nuevamente?(S/N): ")).upper()
    return 

