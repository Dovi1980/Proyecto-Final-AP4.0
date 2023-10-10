
from datetime import datetime

#---------------------------------------------
#---- Control Ingreso de Fecha ----

def control_fecha():
    ok=True
    while ok:
        fecha_ing=str(input("\nFecha de examen (dd/mm/aa): "))
        try:
            fecha_ok = datetime.strptime(fecha_ing, "%d/%m/%y")
            return fecha_ing
        except ValueError:
            print('\nEl formato de fecha es incorrecto, intente nuevamente...')