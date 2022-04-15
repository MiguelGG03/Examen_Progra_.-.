#Importando los modulos

from pokemon import pokemon
from tipo_ataque import Ataque



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
            if (11 <= defense_rating_to_be_set <= 20):
                self.defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("El parametro defense_rating_to_be_set deberia estar entre 1 y 10")
        else:
            raise TypeError("El parametro defense_rating_to_be_set deberia ser un int")


def main():

    print("=================================================================.")
    print("Test 1: Crear un Pokemon.")
    print("=================================================================.")
    pokemon_1 = pokemonTierra(1, "Diglett", Ataque.CABEZAZO, 100, 8, 15)

    if pokemon_1.get_pokemon_name() == "Diglett":
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

    if pokemon_1.get_defense_rating() == 15:
        print("Test completado. El parametro defense_rating ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")


    print("=================================================================.")
    print("Test 2: Leer las stats del pokemon.")
    print("=================================================================.")
    pokemon_2 = pokemonTierra(7, "Diglett", Ataque.CABEZAZO, 100, 7, 12)

    if pokemon_2.leer_stats_pokemon() == ("Pokemon ID 7 cuyo nombre es Diglett tiene como ataque asignado CABEZAZO y 100 puntos de vida."):
        print("Test completado. El metodo leer_stats_pokemon ha sido implementado correctamente.")
    else:
        print("Test fallido. Revisa el metodo __str__()." + " Resultado: " + str(pokemon_2))


    print("=================================================================.")
    print("Test 3: Sigue con vida ?.")
    print("=================================================================.")
    pokemon_3 = pokemonTierra(3, "Diglett", Ataque.PATADA, 97, 8, 15)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test completado. El metodo is_alive() ha sido implementado correctamente.")
        else:
            print("Test fallido. Revisa el metodo is_alive().")
    else:
        print("Test fallido. Revisa el metodo is_alive().")


    print("=================================================================.")
    print("Test 4: Revisar la defensa durante la batalla.")
    print("=================================================================.")
    pokemon_4 = pokemonTierra(4, "Diglett", Ataque.CODAZO, 93, 9, 11)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 34:
        print("Test completado. El metodo fight_defense() ha sido implementado correctamente.")
    else:
        print("Test fallido. Revisa el metodo fight_defense().")


    print("=================================================================.")
    print("Test 5: Revisar el ataque durante la batalla.")
    print("=================================================================.")
    pokemon_5 = pokemonTierra(5, "Diglett", Ataque.PUÑETAZO, 99, 10, 20)
    pokemon_6 = pokemonTierra(6, "Diglett", Ataque.PUÑETAZO, 99, 9, 18)

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