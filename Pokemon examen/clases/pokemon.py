
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tipo_ataque import Ataque


class pokemon:

    ids_pokemons=[]  
    
    def __init__(self,id, pokemon_name, weapon_type, health_points,attack_rating, defense_rating):
        if (isinstance(id,int)==True):
            if(id not in pokemon.ids_pokemons):
                self.id=id
                pokemon.ids_pokemons.append(self.id)
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
                raise ValueError("La vida del pokemon debe estar entre 1 y 100")
        else:
            raise TypeError("La vida debe ser un valor entero")
        
        if(isinstance(attack_rating,int)==True):
            if(1<=attack_rating<=10):
                self.attack_rating=attack_rating
            else:
                raise ValueError("El ataque del pokemon debe estar entre 1 y 10")
        else:
            raise TypeError("La ataque debe ser un valor entero")
        
        if(isinstance(defense_rating,int)==True):
            if(1<=defense_rating<=10):
                self.defense_rating=defense_rating
            else:
                raise ValueError("La defensa del pokemon debe estar entre 1 y 10")
        else:
            raise TypeError("La defensa debe ser un valor entero")

    def get_id(self):
        return self.id

    def get_pokemon_name(self):
        return self.pokemon_name


    def get_weapon_type(self):
        return self.weapon_type


    def get_health_points(self):
        return self.health_points


    def get_attack_rating(self):
        return self.attack_rating


    def get_defense_rating(self):
        return self.defense_rating

    
    def set_pokemon_name(self, pokemon_name_to_be_set):
        if isinstance(pokemon_name_to_be_set, str):
            self._pokemon_name = pokemon_name_to_be_set
        else:
            raise TypeError("El parametro pokemon_name_to_be_set deberia ser un String.")


    def set_weapon_type(self, weapon_type_to_be_set):
        if isinstance(weapon_type_to_be_set, Ataque):
            self._weapon_type = weapon_type_to_be_set
        else:
            raise TypeError("El parametro weapon_type deberia ser un Ataque.")


    def set_attack_rating(self, attack_rating_to_be_set):
        if isinstance(attack_rating_to_be_set, int):
            if 1 <= attack_rating_to_be_set <= 10:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("El parametro attack_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("El parametro attack_rating_to_be_set deberia ser un int.")


    def set_defense_rating(self, defense_rating_to_be_set):
        if isinstance((defense_rating_to_be_set, int)==True):
            if (1 <= defense_rating_to_be_set <= 10):
                self.defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("El parametro defense_rating_to_be_set deberia estar entre 1 y 10")
        else:
            raise TypeError("El parametro defense_rating_to_be_set deberia ser un int")


    def leer_stats_pokemon(self):
        print("Pokemon ID "+str(self.id)+" cuyo nombre es "+self.pokemon_name+" tiene como ataque asignado"+
                str(self.weapon_type).upper()+" y "+self.health_points+" puntos de vida.")


    def is_alive(self):
        if(self.health_points>=1):
            return True
        else:
            return False


    def fight_defense(self,points_of_damage):
        if(self.defense_rating<points_of_damage):
            self.health_points=self.health_points-(points_of_damage-self.defense_rating)
            return True
        else:
            return False


    def fight_attack(self,pokemon_to_attack):
        if(pokemon_to_attack.fight_defense(self.attack_rating)==True):
            print(self.pokemon_name+" ha infringido "+str(self.attack_rating-pokemon_to_attack.defense_rating)+" puntos de daño\nsobre "+pokemon_to_attack.pokemon_name)
            print("La nueva vida de "+pokemon_to_attack.pokemon_name+"\nes de "
                    +str(pokemon_to_attack.health_points)+" puntos de vida.")
        else:
            print("El ataque no ha sido efectivo")


    def elegir_ataque(self,pregunta):
        pregunta=input('Seleccione el ataque:\nPUÑETAZO \nPATADA \nCODAZO \nCABEZAZO\n-')
        if(isinstance(pregunta,str)==True):
            self.pregunta=pregunta
            Ataque.tipo_ataque(pregunta)
        else:
            raise TypeError("La resupesta debe ser un string")


def main():

    print("=================================================================.")
    print("Test 1: Crear un Pokemon.")
    print("=================================================================.")
    pokemon_1 = pokemon(1, "Ivysaur", Ataque.CABEZAZO, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test completado. El parametro pokemon_name ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")

    if pokemon_1.get_weapon_type().name == "CABEZAZO":
        print("Test completado. El parametro weapon_type ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test completado. El parametro health_points ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test completado. El parametro attack_rating ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test completado. El parametro defense_rating ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = pokemon(2, "Charmander", Ataque.CABEZAZO, 100, 7, 10)

    if pokemon_2.leer_stats_pokemon() == ("Pokemon ID 2 cuyo nombre es Charmander tiene como ataque asignado CABEZAZO y 100 puntos de vida."):
        print("Test completado. The human-readable format of the object ha sido implementado correctamente.")
    else:
        print("Test fallido. Revisa el metodo __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test 3: Sigue con vida ?.")
    print("=================================================================.")
    pokemon_3 = pokemon(3, "Wartortle", Ataque.PATADA, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test completado. El metodo is_alive() ha sido implementado correctamente.")
        else:
            print("Test fallido. Revisa el metodo is_alive().")
    else:
        print("Test fallido. Revisa el metodo is_alive().")


    print("=================================================================.")
    print("Test Case 4: Revisar la defensa durante la batalla.")
    print("=================================================================.")
    pokemon_4 = pokemon(4, "Squirtle", Ataque.CODAZO, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test completado. El metodo fight_defense() ha sido implementado correctamente.")
    else:
        print("Test fallido. Revisa el metodo fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Revisar el ataque durante la batalla.")
    print("=================================================================.")
    pokemon_5 = pokemon(5, "Venusaur", Ataque.CABEZAZO, 99, 10, 7)
    pokemon_6 = pokemon(6, "Charmeleon", Ataque.CABEZAZO, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test completado. El metodo fight_attack() ha sido implementado correctamente.")
        else:
            print("Test fallido. Revisa el metodo fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test completado. El metodo fight_attack() ha sido implementado correctamente.")
        else:
            print("Test fallido. Revisa el metodo fight_attack().")

if __name__ == "__main__":
    main()