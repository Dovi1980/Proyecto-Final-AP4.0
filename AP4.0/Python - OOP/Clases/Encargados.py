
from Clases.Personas import Persona

#---- Clase Encargado ----

class Encargado(Persona):
    def __init__(self,nombre,dni,actividad):
                super().__init__(nombre, dni, actividad)

    def __str__(self):
        return f"Nombre: "+ self._nombre +" -- "+ "DNI: " + self._dni +"--"+ "Actividad: "+ self._actividad

