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

    def crear_pokemon(self,vida):
        if(self.vida>100 or self.vida<1):
            print('La vida debe ser un entero entre el 1 y el 100')