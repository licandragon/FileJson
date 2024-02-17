import json


def leer_json(archivo):
    with open(archivo, 'r', encoding='utf-8') as datos:
        pokedex = json.load(datos)
        for pokemon in pokedex:
            print(pokemon)


if __name__ == '__main__':
    archivo = 'pokedex.json'
    leer_json(archivo)
