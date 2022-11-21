import numpy as np
import pandas as pd

df = pd.read_csv('pokedex_(Update_05.20).csv', index_col=0)

col_names = [
    'pokedex_number', 'name', 'generation',
    'status', 'type_number', 'type_1',
    'type_2', 'height_m', 'weight_kg',
    'abilities_number', 'ability_1', 'ability_2',
    'ability_hidden', 'total_points', 'hp',
    'attack', 'defense', 'sp_attack',
    'sp_defense', 'speed', 'catch_rate',
    'base_experience', 'grow_rate', 'percentage_male'
]

filtered_pokemon_data = pd.DataFrame(df, columns=col_names)
filtered_pokemon_data.to_csv('filtered_pokemon_data.csv', index=False)
df = pd.read_csv('filtered_pokemon_data.csv')

