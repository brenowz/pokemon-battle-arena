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

    "moves": [ {
            "name": "Water Gun",
            "type": "water",
            "damage": 15
        },
        {
            "name": "Tackle",
            "type": "normal",
            "damage": 10
        }]
}

print("POKEMON BATTLE ARENA")

starter_options = ["Bulbasaur", "Charmander", "Squirtle"]

for i in range(0, len(starter_options)):
    print(i + 1, starter_options[i])

starter_choice = int(input(
    "Choose your starter!\n"
    "1 = Bulbasaur\n"
    "2 = Charmander\n"
    "3 = Squirtle\n"
))

while starter_choice < 1 or starter_choice > 3:
    print("Invalid option!")
    starter_choice = int(input("Choose again: "))

starter_choice -= 1

if starter_choice == 0:
    player_pokemon = bulbasaur
    print("Let's go, Bulbasaur!")
    

elif starter_choice == 1:
    player_pokemon = charmander
    print("Let's go, Charmander!")
    

elif starter_choice == 2:
    player_pokemon = squirtle
    print("Let's go, Squirtle!")
    

for i in range(0, len(player_pokemon["moves"])):
    print(i + 1,player_pokemon["moves"][i]["name"])

move_choice = int(input("Choose your move:"))
while move_choice < 1 or move_choice > 2:
    print("Invalid option!")
    move_choice = int(input("Choose your move:"))

move_choice -= 1
    

selected_move = player_pokemon["moves"][move_choice]
print(f"{player_pokemon["name"]} used {selected_move["name"]}!")



    