import requests
import sqlite3

#conectar BD
conn = sqlite3.connect("pokemon.db")
cursor = conn.cursor()

#puxar dados de pokemon
def get_pokemon_data(pokemon_id):
    url = f"http://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json() 

    id = data["id"]
    nome = data["name"]
    altura = data["height"]
    peso = data["weight"]

    #tipo primário do pokemon
    tipo = data["types"][0]["type"]["name"]

    #stats do pokemon
    ataque = None
    defesa = None

    for stat in data["stats"]:
        if stat["stat"]["name"] == "attack":
            ataque = stat["base_stat"]
        if stat["stat"]["name"] == "defense":
            defesa = stat["base_stat"]

    return (id, nome, altura, peso, ataque, defesa, tipo)

#inserir no bd
def insert_pokemon(pokemon):
    cursor.execute("""
                   INSERT OR IGNORE INTO pokemon (id, nome, altura, peso, ataque, defesa, tipo)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   """, pokemon)
    conn.commit()

#coletar alguns pokemons
for i in range(1, 152): #10 primeiros pkmn
    pokemon = get_pokemon_data(i)
    insert_pokemon(pokemon)
    print(f"{pokemon[0]} inserido!")
conn.close()