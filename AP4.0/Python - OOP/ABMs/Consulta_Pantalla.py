
from Clases.Encargados import Encargado
from Clases.Inscriptos import Inscripto
from Clases.Profesores import Profesor
from prettytable import PrettyTable

#-------------------------------------------------------------------------------
# Con este código busco mostrar los datos consultados de una manera más legible
# utilizando la libreria "prettytable".
# Esta función reemplaza al siguiente código en los distintos modulos:
# --> print(f"Los datos consultados son: {n_elemento}")
#-------------------------------------------------------------------------------

def reprDatos(objeto):
    print()
    tabla = PrettyTable()
    if objeto.Actividad == "ENCARGADO":
        tabla.field_names = ["ENCARGADO", "DNI"]
        tabla.add_row([objeto.Nombre, objeto.DNI])
        return tabla

    elif objeto.Actividad == "PROFESOR":
        tabla.field_names = ["PROFESOR", "MATERIA", "CURSO", "DIVISION"]
        tabla.add_row([objeto.Nombre, objeto.Materia, objeto.Curso, objeto.Division])
        return tabla

    elif objeto.Actividad == "ESTUDIANTE":
        tabla.field_names = ["ALUMN@", "FECHA EXAMEN", "MATERIA", "PROFESOR", "CURSO", "DIVISION", "NOTA"]
        tabla.add_row([objeto.Nombre, objeto.Fecha, objeto.Materia,\
                    objeto.Profesor, objeto.Curso, objeto.Division, objeto.Nota])
        return tabla
