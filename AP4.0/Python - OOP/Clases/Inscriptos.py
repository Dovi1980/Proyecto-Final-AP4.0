
from Clases.Personas import Persona

#-----------------------------------------------------------------------
# Se agregan instancias no solicitadas en el Trabajo sólo para 
# demostrar lo aprendido.
# El dato de "actividad" se utilizara con el fin de realizar un filtrado
# y el dato de "update" es con el fin de colocar el último usuario en
# realizar una modificación en la inscripcion.
#-----------------------------------------------------------------------
#---- Clase Inscripto ----

class Inscripto(Persona):
    def __init__(self,nombre,dni,actividad,fecha,materia,profesor,curso,division,nota,update):
        super().__init__(nombre, dni, actividad)
        self._fecha = fecha
        self._materia = materia
        self._profesor = profesor
        self._curso = curso
        self._division = division
        self._nota = nota
        self._update = update

    @property
    def Fecha(self):
        return self._fecha

    @Fecha.setter
    def Fecha(self,fecha):
        self._fecha = fecha

    @property
    def Materia(self):
        return self._materia

    @Materia.setter
    def Materia(self,materia):
        self._materia = materia

    @property
    def Profesor(self):
        return self._profesor

    @Profesor.setter
    def Profesor(self,profesor):
        self._profesor = profesor

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

    @property
    def Nota(self):
        return self._nota

    @Nota.setter
    def Nota(self,nota):
        self._nota = nota

    @property
    def Update(self):
        return self._update

    @Update.setter
    def Update(self,update):
        self._update = update

    def __str__(self):
        return f"Nombre: "+ self._nombre +" -- "+"DNI: "+ self._dni +" -- "+ "Actividad: "+ self._actividad +" -- "+\
            "Fecha Examen: "+ self._fecha +" -- "+"Materia: "+ self._materia +" -- "+ "Profesor: "+ self._profesor +" -- "+ \
                "Curso: "+ self._curso +" -- "+ "Division: "+ self._division +" -- "+ "Nota: "+ self._nota + \
                    "Ultima Modificación: "+ self._update

