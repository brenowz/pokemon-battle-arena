import random


# Pokemon data
bulbasaur = {
    "name": "Bulbasaur",
    "hp": 100,
    "type": "grass",
    "moves": [
        {
            "name": "Vine Whip",
            "type": "grass",
            "damage": 15
        },
        {
            "name": "Tackle",
            "type": "normal",
            "damage": 10
        }
    ]
}

charmander = {
    "name": "Charmander",
    "hp": 100,
    "type": "fire",
    "moves": [
        {
            "name": "Ember",
            "type": "fire",
            "damage": 15
        },
        {
            "name": "Scratch",
            "type": "normal",
            "damage": 10
        }
    ]
}

squirtle = {
    "name": "Squirtle",
    "hp": 100,
    "type": "water",
    "moves": [
        {
            "name": "Water Gun",
            "type": "water",
            "damage": 15
        },
        {
            "name": "Tackle",
            "type": "normal",
            "damage": 10
        }
    ]
}


#list with all pokemons
pokemons = [bulbasaur, charmander, squirtle]


print("POKEMON BATTLE ARENA")

#starter options
starter_options = ["Bulbasaur", "Charmander", "Squirtle"]

for i in range(0, len(starter_options)):
    print(i + 1, starter_options[i])


#player chooses the starter
starter_choice = int(input(
    "Choose your starter!\n"
    "1 = Bulbasaur\n"
    "2 = Charmander\n"
    "3 = Squirtle\n"
))


#checks if the option is valid
while starter_choice < 1 or starter_choice > 3:
    print("Invalid option!")
    starter_choice = int(input("Choose again: "))


#sakes the choice match the list index
starter_choice -= 1


#saves the chosen pokemon
if starter_choice == 0:
    player_pokemon = bulbasaur
    print("Let's go, Bulbasaur!")

elif starter_choice == 1:
    player_pokemon = charmander
    print("Let's go, Charmander!")

elif starter_choice == 2:
    player_pokemon = squirtle
    print("Let's go, Squirtle!")


#creates the enemy options without the player pokemon
enemy_options = []

for pokemon in pokemons:
    if pokemon != player_pokemon:
        enemy_options.append(pokemon)


#random enemy
enemy_pokemon = random.choice(enemy_options)

print(f"A wild {enemy_pokemon['name']} appeared!")


#battle keeps going while both pokemons are alive
while player_pokemon["hp"] > 0 and enemy_pokemon["hp"] > 0:

    print("\nChoose your move:")

    #shows the player moves
    for i in range(0, len(player_pokemon["moves"])):
        print(i + 1, player_pokemon["moves"][i]["name"])


    #player chooses a move
    move_choice = int(input("Choose your move: "))


    #checks if the move exists
    while move_choice < 1 or move_choice > 2:
        print("Invalid option!")
        move_choice = int(input("Choose your move: "))


    #makes the choice match the move index
    move_choice -= 1

    selected_move = player_pokemon["moves"][move_choice]


    #player attacks the enemy
    enemy_pokemon["hp"] -= selected_move["damage"]


    print(f"\n{player_pokemon['name']} used {selected_move['name']}!")
    print(f"{enemy_pokemon['name']} took {selected_move['damage']} damage!")
    print(f"{enemy_pokemon['name']} HP: {enemy_pokemon['hp']}")


    #checks if the enemy fainted
    if enemy_pokemon["hp"] <= 0:
        print(f"\n{enemy_pokemon['name']} fainted!")
        print(f"{player_pokemon['name']} wins!")
        break


    #enemy chooses a random move
    enemy_move = random.choice(enemy_pokemon["moves"])


    #enemy attacks the player
    player_pokemon["hp"] -= enemy_move["damage"]


    print(f"\n{enemy_pokemon['name']} used {enemy_move['name']}!")
    print(f"{player_pokemon['name']} took {enemy_move['damage']} damage!")
    print(f"{player_pokemon['name']} HP: {player_pokemon['hp']}")


    #checks if the player fainted
    if player_pokemon["hp"] <= 0:
        print(f"\n{player_pokemon['name']} fainted!")
        print(f"{enemy_pokemon['name']} wins!")
        break