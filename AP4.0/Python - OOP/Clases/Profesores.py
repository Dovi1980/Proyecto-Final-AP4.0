
from Clases.Personas import Persona

#---- Clase Profesor ----

class Profesor(Persona):
    def __init__(self,nombre,dni,actividad,materia,curso,division):
        super().__init__(nombre, dni, actividad)
        self._materia = materia
        self._curso = curso
        self._division = division

    @property
    def Materia(self):
        return self._materia

    @Materia.setter
    def Materia(self,materia):
        self._materia = materia

    @property
    def Curso(self):
        return self._curso

    @Curso.setter
    def Curso(self,curso):
        self._curso = curso

    @property
    def Division(self):
        return self._division

    @Division.setter
    def Division(self,division):
        self._division = division

    def __str__(self):
        return f"Nombre: "+ self._nombre +" -- "+ "DNI: "+ self._dni +" -- "+ "Actividad: "+ self._actividad + \
                 " -- "+"Materia: " + self._materia +" -- "+ "Curso: "+ self._curso +" -- "+ "Division: "+ self._division

