import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
moveimport = open("./moves.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
moves = json.load(moveimport)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name. DONE

# Add a language choice feature and print the pokemons name based on the user input DONE

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user DONE

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found.  DONE

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too! DONE

language = input("What language do you prefer, English, Japanese, Chinese, or French? : ")

def printname():
    for i in range(len(data)):
        print(data[i]["name"][language.lower()])
def typesearch():
    usertype = []
    type = input("What type of pokemon would you like to search for? Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dragon, Dark, Steel or Fairy : ")
    for i in range(len(data)):
        for n in range(len(data[i]["type"])):
            if data[i]["type"][n].lower() == type.lower():
                usertype.append(data[i]["name"][language.lower()])
    if len(usertype) == 0:
        print("No pokemon was found.")
    print(usertype)
def namesearch():
    usernames = []
    search = input("What pokemon would you like to search for? ")
    searchlist = list(search)
    for i in range(len(data)):
        pokemonname = list(data[i]["name"][language.lower()])
        pokemonname.insert(0,pokemonname[0].lower())
        pokemonname.pop(1)
        if searchlist == pokemonname[0:len(searchlist)]:
            usernames.append(data[i]["name"][language.lower()])
    if len(usernames) == 0:
        print("No pokemon were found.")
    else:
        print(usernames)
def moveprint():
    pokename = input("Select a pokemon: ")
    poketype = []
    pokemoves = []
    for i in range(len(data)):
        if data[i]["name"]["english"].lower() == pokename.lower():
            for n in range(len(data[i]["type"])):
                poketype.append(data[i]["type"][n])
    for i in range(len(moves)):
        for n in range(len(poketype)):
            if moves[i]["type"].lower() == poketype[n].lower():
                pokemoves.append(moves[i]["ename"])
    print(pokemoves)

printname()
typesearch()
namesearch()
moveprint() 