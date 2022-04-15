from clases.pokemon import pokemon
from clases.tipo_ataque import Ataque

class pokemonTierra(pokemon):


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):


        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, 10)
            
        if(isinstance(defense_rating,int)==True):
            if(11<=defense_rating<=20):
                self.defense_rating=defense_rating
            else:
                raise ValueError("La defensa del pokemon debe estar entre 1 y 10")
        else:
            raise TypeError("La defensa debe ser un valor entero")
    
    def set_defense_rating(self, defense_rating_to_be_set):
        if isinstance((defense_rating_to_be_set, int)==True):
            if (1 <= defense_rating_to_be_set <= 10):
                self.defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("El parametro defense_rating_to_be_set deberia estar entre 1 y 10")
        else:
            raise TypeError("El parametro defense_rating_to_be_set deberia ser un int")