from pokemons import * #Import *, es para que importe todo, clases de ataques, clase pokemon, los elementos, etc
import random #Para poder elegir una opción cualquiera de random, como en piedra, papel, tijera

print("POKEMON".center(50, "#"))
print("Oak: Select your first pokemon...")
[print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(pokemons)]
user = int(input("Choose: ")) - 1
pokemon_a = pokemons[user]
print(pokemon_a)



# for i, pokemon in enumerate(pokemons):
#      print(f"{i + 1}. {pokemon.name}")

# user = int(input("Choose: "))

