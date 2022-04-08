from enum import Enum


class Ataque(Enum):
    PUÑETAZO = 1
    PATADA = 2
    CODAZO = 3
    CABEZAZO = 4

    Ataque= Enum('Ataque','PUÑETAZO PATADA CODAZO CABEZAZO')
    
