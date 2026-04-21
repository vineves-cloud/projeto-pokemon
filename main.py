import requests
import sqlite3

#conectar BD
conn = sqlite3.connect("pokemon.db")
cursor = conn.cursor()

#puxar dados de pokemon
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json() 

    id = data["id"]
    nome = data["name"]
    altura = data["height"]
    peso = data["weight"]

    #tipo primário do pokemon
    tipo1 = data["types"][0]["type"]["name"]

    #tipo secundário (se existir)
    if len(data["types"]) > 1:
        tipo2 = data["types"][1]["type"]["name"]
    else:
        tipo2 = None
    
    
    #stats do pokemon
    ataque = None
    defesa = None

    for stat in data["stats"]:
        if stat["stat"]["name"] == "attack":
            ataque = stat["base_stat"]
        if stat["stat"]["name"] == "defense":
            defesa = stat["base_stat"]

    print(nome, tipo1, tipo2)
    return (id, nome, altura, peso, ataque, defesa, tipo1, tipo2)

#inserir no bd
def insert_pokemon(pokemon):
    cursor.execute("""
        INSERT INTO pokemon (id, nome, altura, peso, ataque, defesa, tipo1, tipo2)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
        nome=excluded.nome,
        altura=excluded.altura,
        peso=excluded.peso,
        ataque=excluded.ataque,
        defesa=excluded.defesa,
        tipo1=excluded.tipo1,
        tipo2=excluded.tipo2
        """, pokemon)
    conn.commit()

#coletar alguns pokemons
#for i in range(1, 152): #151 primeiros pkmn
for i in range(1, 10): #10 primeiros pkmn
    pokemon = get_pokemon_data(i)
    insert_pokemon(pokemon)
    print(f"{pokemon[0]} inserido!")
conn.close()



