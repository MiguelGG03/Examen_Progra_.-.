class pokemon:
    hp=0
    #health points(1/100), inicialmente 0
    def __init__(self,id,name,weapon,dap,dep):
        self.id=id
        self.name=name
        self.weapon=weapon
        #puñetazo(1),patada(2),codazo(3),cabezazo(4)
        self.dap=dap
        #damage points(1/10)
        self.dep=dep
        #defense points(1/10)