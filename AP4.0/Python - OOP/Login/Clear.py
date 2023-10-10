
import os

#------ Para limpiar la pantalla entre menues -------

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

