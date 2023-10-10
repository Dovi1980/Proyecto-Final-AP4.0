
from TDAs import TDAProfesor
from TDAs import TDAEncargado
from TDAs import TDAInscriptos

#---------------------------------------------
def cargaTXTenc():
  enc_list=[]
  encargados = open("./TXTs/encargados.txt", "r")
  lista=encargados.readlines()
  encargados.close()
  for elemento in lista:
    e=elemento.split(",")
    enc_list.append(TDAEncargado.crear(e[0], e[1].rstrip()))
  return enc_list

def cargaTXTprofe():
  profe_list=[]
  profesores = open("./TXTs/profesores.txt", "r")
  lista=profesores.readlines()
  profesores.close()
  for elemento in lista:
    e=elemento.split(",")
    profe_list.append(TDAProfesor.crear(e[0], e[1], e[2], e[3].rstrip()))
  return profe_list      

def cargaTXTinscripciones():
  insc_list=[]
  inscripciones = open("./TXTs/inscripciones.txt", "r")
  lista=(inscripciones.readlines())
  inscripciones.close()
  for elemento in lista:
    e=elemento.split(",")
    insc_list.append(TDAInscriptos.crear(e[0], e[1], e[2], e[3], e[4], e[5], e[6].rstrip()))
  return insc_list

