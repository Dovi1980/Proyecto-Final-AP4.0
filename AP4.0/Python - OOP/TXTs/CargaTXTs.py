
from Clases.Profesores import Profesor
from Clases.Encargados import Encargado
from Clases.Inscriptos import Inscripto

#---------------------------------------------------------------
#---- Carga Inicial de Archivos ".txt" ----

def cargaTXTenc():
  enc_list=[]
  encargados = open("./TXTs/encargados.txt", "r")
  lista=encargados.readlines() 
  encargados.close()
  for elemento in lista:
    e=elemento.split(",")
    enc = Encargado(e[0], e[1], e[2].rstrip())
    enc_list.append(enc)
  return enc_list

def cargaTXTprofe():
  profe_list=[]
  profesores = open("./TXTs/profesores.txt", "r")
  lista=profesores.readlines()
  profesores.close()
  for elemento in lista:
    e=elemento.split(",")
    profe = Profesor(e[0], e[1], e[2], e[3], e[4], e[5].rstrip())
    profe_list.append(profe)
  return profe_list      

def cargaTXTinscripciones():
  insc_list=[]
  inscripciones = open("./TXTs/inscripciones.txt", "r")
  lista=inscripciones.readlines()
  inscripciones.close()
  for elemento in lista:
    e=elemento.split(",")
    insc = Inscripto(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9].rstrip())
    insc_list.append(insc)
  return insc_list

