from clases.tipo_ataque import *

ids_pokemons=[]

class pokemon:
    
    def __init__(self,id,name,weapon,hp,DAP,DEP):
        self.id=id
        self.name=name
        self.weapon=weapon
        #puñetazo(1),patada(2),codazo(3),cabezazo(4)
        self.hp=hp
        #health points(1/100), inicialmente 0  
        self.dap=DAP
        #damage points(1/10)
        self.dep=DEP
        #defense points(1/10)

    def elegir_ataque(self,pregunta):
        pregunta=input('Seleccione el ataque:\nPUÑETAZO \nPATADA \nCODAZO \nCABEZAZO\n-')
        self.pregunta=pregunta
        Ataque.tipo_ataque(pregunta)
