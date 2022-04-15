#Importando los modulos
import random


from pokemon import pokemon
from tipo_ataque import Ataque



class pokemonElectricidad(pokemon):


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):


        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating)

    def fight_defense_0(self,points_of_damage):
        if(not isinstance(points_of_damage,int)):
            raise TypeError("El parametro points_of_damage deberia ser un int.") 
        else:   
            if(self.defense_rating<points_of_damage):
                h=points_of_damage-self.defense_rating
                self.health_points=self.health_points-h
                return True
            else:
                return False
    

    def fight_defense_1(self,points_of_damage):
        if(not isinstance(points_of_damage,int)):
            raise TypeError("El parametro points_of_damage deberia ser un int.") 
        else:   
            if(self.defense_rating<points_of_damage):
                h=(points_of_damage*2)-self.defense_rating
                self.health_points=self.health_points-h
                return True
            else:
                return False


    def fight_attack(self,pokemon_to_attack):
        n_r=int(random.randint(0,1))
        if(n_r==0):
            if(pokemon_to_attack.fight_defense_0(self.attack_rating)==True):
                print(self.pokemon_name+" ha infringido "+str(self.attack_rating-pokemon_to_attack.defense_rating)+" puntos de daño\nsobre "+pokemon_to_attack.pokemon_name)
                print("La nueva vida de "+pokemon_to_attack.pokemon_name+"\nes de "
                        +str(pokemon_to_attack.health_points)+" puntos de vida.")
                return True
            else:
                print("El ataque no ha sido efectivo")
                return False
        else:
            if(pokemon_to_attack.fight_defense_1(self.attack_rating)==True):
                print(self.pokemon_name+" ha infringido "+str((self.attack_rating*2)-pokemon_to_attack.defense_rating)+" puntos de daño\nsobre "+pokemon_to_attack.pokemon_name)
                print("La nueva vida de "+pokemon_to_attack.pokemon_name+"\nes de "
                        +str(pokemon_to_attack.health_points)+" puntos de vida.")
                return True
            else:
                print("El ataque no ha sido efectivo")
                return False


def main():

    print("=================================================================.")
    print("Test 1: Crear un Pokemon.")
    print("=================================================================.")
    pokemon_1 = pokemonElectricidad(1, "Pikachu", Ataque.CABEZAZO, 100, 8, 7)

    if pokemon_1.get_pokemon_name() == "Pikachu":
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

    if pokemon_1.get_defense_rating() == 7:
        print("Test completado. El parametro defense_rating ha sido correctamente aplicado.")
    else:
        print("Test fallido. Revisa el metodo __init__().")


    print("=================================================================.")
    print("Test 2: Leer las stats del pokemon.")
    print("=================================================================.")
    pokemon_2 = pokemonElectricidad(7, "Pikachu", Ataque.CABEZAZO, 100, 7, 6)

    if pokemon_2.leer_stats_pokemon() == ("Pokemon ID 7 cuyo nombre es Pikachu tiene como ataque asignado CABEZAZO y 100 puntos de vida."):
        print("Test completado. El metodo leer_stats_pokemon ha sido implementado correctamente.")
    else:
        print("Test fallido. Revisa el metodo __str__()." + " Resultado: " + str(pokemon_2))


    print("=================================================================.")
    print("Test 3: Sigue con vida ?.")
    print("=================================================================.")
    pokemon_3 = pokemonElectricidad(3, "Pikachu", Ataque.PATADA, 97, 8, 7)

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
    pokemon_4 = pokemonElectricidad(4, "Pikachu", Ataque.CODAZO, 93, 9, 5)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 34:
        print("Test completado. El metodo fight_defense() ha sido implementado correctamente.")
    else:
        print("Test fallido. Revisa el metodo fight_defense().")


    print("=================================================================.")
    print("Test 5: Revisar el ataque durante la batalla.")
    print("=================================================================.")
    pokemon_5 = pokemonElectricidad(5, "Pikachu", Ataque.PUÑETAZO, 99, 10, 8)
    pokemon_6 = pokemonElectricidad(6, "Pikachu", Ataque.PUÑETAZO, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 95:
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