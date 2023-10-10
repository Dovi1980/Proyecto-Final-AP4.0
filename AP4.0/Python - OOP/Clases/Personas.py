
#------------------------------------------------------------------------------------
# Se crea esta clase con el fin de utilizar herencia en el Trabajo Práctico.
# Si es profesor, activida = PROFESOR 
# Si es encargado, actividad = ENCARGADO 
# Si es estudiante, actividad = ESTUDIANTE 
# La actividad se utilizara para la muestra por pantalla de las consultas realizadas.
#------------------------------------------------------------------------------------
#---- Clase Persona ----

class Persona:
    def __init__(self, nombre, dni, actividad):
        self._nombre = nombre
        self._dni = dni
        self._actividad = actividad

    @property
    def Nombre(self):
        return self._nombre

    @Nombre.setter
    def Nombre(self,nombre):
        self._nombre = nombre                           

    @property
    def DNI(self):
        return self._dni

    @DNI.setter
    def DNI(self,dni):
        self._dni = dni
    
    @property
    def Actividad(self):
        return self._actividad

    @Actividad.setter
    def Actividad(self,actividad):
        self._actividad = actividad

    def __str__(self):
        return f"Nombre: "+ self._nombre +" -- "+ "DNI: " + self._dni +" -- "+ "Actividad: " + self._actividad

