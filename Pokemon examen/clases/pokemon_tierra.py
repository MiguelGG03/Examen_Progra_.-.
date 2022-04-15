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
    
    def get_defense_rating(self):
        return self.defense_rating