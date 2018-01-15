import pokemonMoves
import pokemon
from pokemon import Pokemon

# Prints out the information of pokemon
def printInformation(pokemon):
  print(pokemon.information())
  print(pokemon.moves)
  print("")
  
    
# Initializes Pokemon Team 
PorygonZ = Pokemon("PorygonZ", 75, "Normal")
Metagross = Pokemon("Metagross", 69, "Steel/Psychic")
Volcarona = Pokemon("Volcarona", 73, "Fire/Bug")
Braviary = Pokemon("Braviary", 71, "Flying/Normal")

# Stores the Pokemon team 
pokemon_team = [PorygonZ, Metagross, Volcarona, Braviary]

# Prints out the information for all Pokemon in pokemon_team 
for pokemon in pokemon_team:
  printInformation(pokemon)
