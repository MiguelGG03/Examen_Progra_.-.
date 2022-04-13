from clases.tipo_ataque import *

ids_pokemons=[]

class pokemon:
    
    def __init__(self,id, pokemon_name, weapon_type, health_points,attack_rating, defense_rating):
        if (isinstance(id,int)==True):
            if(id not in pokemon.global_ids):
                self.id=id
                pokemon.global_ids.append(self.id)
            else:
                raise ValueError("El id del pokemon deberia ser uno nuevo id y no uno repetido de otro pokemon.")
                # "raise" es para hacer saltar un error
        else:
            raise TypeError("El parametro id deberia ser un valor entero")

        if(isinstance(pokemon_name,str)==True):
            self.pokemon_name=pokemon_name
        else:
            raise TypeError("El nombre deberia ser un string")

        if(isinstance(weapon_type,Ataque)==True):
            self.weapon_type=weapon_type
        else:
            raise TypeError("El tipo de ataque no pertenece a la clase /Ataque/")
                
        if(isinstance(health_points,int)==True):
            if(1<=health_points<=100):
                self.health_points=health_points
            else:
                raise ValueError("La vida del poquemon debe estar entre 1 y 100")
        else:
            raise TypeError("La vida debe ser un valor entero")
        
        if(isinstance(attack_rating,int)==True):
            if(1<=attack_rating<=100):
                self.attack_rating=attack_rating
            else:
                raise ValueError("La vida del poquemon debe estar entre 1 y 100")
        else:
            raise TypeError("La vida debe ser un valor entero")
        
        if(isinstance(defense_rating,int)==True):
            if(1<=defense_rating<=100):
                self.defense_rating=defense_rating
            else:
                raise ValueError("La vida del poquemon debe estar entre 1 y 100")
        else:
            raise TypeError("La vida debe ser un valor entero")

    def leer_stats_pokemon(self):
        print("Pokemon ID"+str(self.id)+" cuyo nombre es "+self.pokemon_name+" tiene como ataque asignado"+
                str(self.weapon_type.upper())+" y "+self.health_points+" puntos de vida.")

    def elegir_ataque(self,pregunta):
        pregunta=input('Seleccione el ataque:\nPUÑETAZO \nPATADA \nCODAZO \nCABEZAZO\n-')
        if(isinstance(pregunta,str)==True):
            self.pregunta=pregunta
            Ataque.tipo_ataque(pregunta)
        else:
            raise TypeError("La resupesta debe ser un string")
