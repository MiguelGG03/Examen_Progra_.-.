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
    

#Validación de los datos

def main():

    print("=================================================================.")
    print("Test Case 1: Check Class Ataque - Name.")
    print("=================================================================.")

    if isinstance(Ataque.PUÑETAZO, Ataque):
        print("Test PASS. The enum for PUÑETAZO has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Ataque.PATADA, Ataque):
        print("Test PASS. The enum for PATADA has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Ataque.CODAZO, Ataque):
        print("Test PASS. The enum for CODAZO has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Ataque.CABEZAZO, Ataque):
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class Ataque - Value.")
    print("=================================================================.")

    if Ataque.PUÑETAZO.value == 2:
        print("Test PASS. The enum for PUÑETAZO has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if Ataque.PATADA.value == 4:
        print("Test PASS. The enum for PATADA has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if Ataque.CODAZO.value == 6:
        print("Test PASS. The enum for CODAZO has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if Ataque.CABEZAZO.value == 10:
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


if __name__ == "__main__":
    main()
