import requests
import random

url = "https://pokeapi.co/api/v2/pokemon/"

def GetPokemon():
    #set random id between 1 and 825
    id = random.randint(1,825)
    #turn it to a string for URI
    randomPk = url + str(id)

    #send get request for json file
    resp = requests.get(url=randomPk)
    #Get all pokemon
    #resp = requests.get(url=url)
    data = resp.json()# Check the JSON Response Content documentation below

    #Number
    number = "#" + str(id)
    print(number)

    #Name
    name = data["name"]
    print(name)

    #Sprite
    # Get the Pokémon sprite. Check if there is an animated version available, if not revert to the default.
    sprite = data["sprites"]["versions"]["generation-v"]["black-white"]["animated"]["front_default"]
    print(sprite)
    if sprite == None:
        sprite = data["sprites"]["front_default"]
    print(sprite)

    #Type
    type = data["types"][0]["type"]["name"]
    print(type)

    #color background based on type
    colorType = {
        "normal": "white", 
        "fighting": "red",
        "flying": "white",
        "poison": "purple", 
        "ground": "brown", 
        "rock": "brown", 
        "bug": "green", 
        "ghost": "purple", 
        "steel": "silver", 
        "fire": "red", 
        "water": "blue", 
        "grass": "green", 
        "electric": "yellow",
        "psychic": "purple", 
        "ice": "blue", 
        "dragon": "yellow", 
        "dark": "black", 
        "fairy": "pink", 
        "unknown": "black", 
        "shadow": "black"
       
    }
    #find color
    colorPokemon =colorType.get(type)
    print(colorPokemon)
    return [number, name, sprite, type, colorPokemon]


#define pokemon class
#class Pokemon:
    #def __init__(self, number, name, type, imageURI):
        #self.number = number
        #self.name = name
        #self.type = type
        #self.imageURI = imageURI



