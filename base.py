import csv
import sqlite3
import json

# Connect to the DB
conn = sqlite3.connect('pokemon.db')
cursor = conn.cursor()

# Create table for Pokemon data
cursor.execute("DROP TABLE IF EXISTS Pokemon")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pokemon (
        Name TEXT,
        Type_1 TEXT,
        Type_2 TEXT,
        Generation INTEGER,
        Legendary TEXT
    )
''')

# Read the CSV and insert into the DB
with open('pokemon.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    try:
        for row in csvFile:

            # Grab data
            name = row['Name']
            type1 = row['Type 1']
            type2 = row['Type 2']
            generation = int(row['Generation']) 
            legendary = row['Legendary']
            
            # Insert the data into the table
            cursor.execute('''
                INSERT INTO Pokemon (Name, Type_1, Type_2, Generation, Legendary) VALUES (?, ?, ?, ?, ?)
            ''', (name, type1, type2, generation, legendary))
        print("Pokemon added to the DB successfully")
    except:
        print("Adding to DB failed")


# Select all legendary Pokemon
cursor.execute("SELECT * FROM Pokemon WHERE Legendary = 'True'")

# Fetch all legendary Pokémon rows
legendary_pokemon = cursor.fetchall()

conn.close()

# Convert the fetched data to a list of dictionaries
legendary_pokemon_list = []
for pokemon in legendary_pokemon:
    legendary_pokemon_list.append({
        "Name": pokemon[0],
        "Type_1": pokemon[1],
        "Type_2": pokemon[2],
        "Generation": pokemon[3],
        "Legendary": pokemon [4]
    })

# Write the legendary Pokémon data to a JSON file
with open('legendary_pokemon.json', 'w') as json_file:
    json.dump(legendary_pokemon_list, json_file, indent=4)

print("Legendary Pokémon data has been written to legendary_pokemon.json")

