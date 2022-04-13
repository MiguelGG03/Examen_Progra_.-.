from enum import Enum


class Ataque(Enum):
    PUÑETAZO = 2
    PATADA = 4
    CODAZO = 6
    CABEZAZO = 10

    def __str__(self):
        return self.name

    @staticmethod
    
    def tipo_ataque(stringdelarma):

        stringdelarma=stringdelarma.lower()
        if (stringdelarma == 'puñetazo'):
            return Ataque.PUÑETAZO
        elif (stringdelarma == 'patada'):
            return Ataque.PATADA
        elif (stringdelarma == 'codazo'):
            return Ataque.CODAZO
        elif (stringdelarma == 'cabezazo'):
            return Ataque.CABEZAZO
        else:
            print('***'+str(stringdelarma.upper())+' NO ES UN TIPO DE ATAQUE REGISTRADO***')  
    
