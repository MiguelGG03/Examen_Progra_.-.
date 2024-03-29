#Importando los modulos

from pokemon import pokemon
from tipo_ataque import Ataque



class pokemonAgua(pokemon):


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):


        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                 10, defense_rating)
            
        if(isinstance(attack_rating,int)==True):
            if(11<=attack_rating<=20):
                self.attack_rating=attack_rating
            else:
                raise ValueError("El ataque del pokemon debe estar entre 1 y 10")
        else:
            raise TypeError("La ataque debe ser un valor entero")
    
    def set_attack_rating(self, attack_rating_to_be_set):
        if isinstance(attack_rating_to_be_set, int):
            if 11 <= attack_rating_to_be_set <= 20:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("El parametro attack_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("El parametro attack_rating_to_be_set deberia ser un int.")


def main():

    print("=================================================================.")
    print("Test 1: Crear un Pokemon.")
    print("=================================================================.")
    pokemon_1 = pokemonAgua(1, "Squirtle", Ataque.CABEZAZO, 100, 12, 8)

    if pokemon_1.get_pokemon_name() == "Squirtle":
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

    if pokemon_1.get_attack_rating() == 12:
        print("Test completado. El parametro attack_rating ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")

    if pokemon_1.get_defense_rating() == 8:
        print("Test completado. El parametro defense_rating ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")


    print("=================================================================.")
    print("Test 2: Leer las stats del pokemon.")
    print("=================================================================.")
    pokemon_2 = pokemonAgua(7, "Squirtle", Ataque.CABEZAZO, 100,15, 7)

    if pokemon_2.leer_stats_pokemon() == ("Pokemon ID 7 cuyo nombre es Diglett tiene como ataque asignado CABEZAZO y 100 puntos de vida."):
        print("Test completado. El metodo leer_stats_pokemon ha sido implementado correctamente.")
    else:
        print("Test fallido. Revisa el metodo __str__()." + " Resultado: " + str(pokemon_2))


    print("=================================================================.")
    print("Test 3: Sigue con vida ?.")
    print("=================================================================.")
    pokemon_3 = pokemonAgua(3, "Squirtle", Ataque.PATADA, 97, 15, 8)

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
    pokemon_4 = pokemonAgua(4, "Squirtle", Ataque.CODAZO, 93, 11, 9)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 32:
        print("Test completado. El metodo fight_defense() ha sido implementado correctamente.")
    else:
        print("Test fallido. Revisa el metodo fight_defense().")


    print("=================================================================.")
    print("Test 5: Revisar el ataque durante la batalla.")
    print("=================================================================.")
    pokemon_5 = pokemonAgua(5, "Squirtle", Ataque.PUÑETAZO, 99, 20, 10)
    pokemon_6 = pokemonAgua(6, "Squirtle", Ataque.PUÑETAZO, 99, 18, 9)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 88:
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