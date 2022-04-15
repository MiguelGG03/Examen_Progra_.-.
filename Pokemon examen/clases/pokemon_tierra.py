from clases.pokemon import pokemon
from clases.tipo_ataque import Ataque

class pokemonTierra(pokemon):
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, 10):
                 