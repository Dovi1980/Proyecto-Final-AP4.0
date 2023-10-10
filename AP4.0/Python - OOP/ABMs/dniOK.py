
#---------------------------------------------------------------------
# Aca se realiza un control de ingreso de DNI valido para nuestro
# país, suponiendo que la numeracion definida en el codigo corresponde
# a la poblacion mayor de 18 años.
#---------------------------------------------------------------------
#---- Control Ingreso DNI ----

def control_DNI():
    ok=True
    while ok:
        dni_ing= int(input("Ingrese DNI: "))
        try:
            if (7<= len(str(dni_ing)) <9) and (4000000 <= dni_ing <= 34999999):
                return str(dni_ing)
        except ValueError:
            print('\nEl DNI es inválido, intente nuevamente...')
