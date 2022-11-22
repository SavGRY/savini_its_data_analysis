import numpy as np
import pandas as pd

# loading the entire csv
df = pd.read_csv('CSV/pokedex_(Update_05.20).csv', index_col=0)

# pick up only the columns i think need now
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

# creating a new dataFrame with starting point my old dataFrame and filtering
# for only the columns in the column list
# and saving it
filtered_pokemon_data = pd.DataFrame(df, columns=col_names)

# Linking genreration number to publish date (JP)
years = [1996, 1999, 2002, 2006, 2010, 2013, 2016, 2019]

my_years = np.where(filtered_pokemon_data['generation'] == 1, years[0],
                                np.where(filtered_pokemon_data['generation'] == 2, years[1],
                                np.where(filtered_pokemon_data['generation'] == 3, years[2],
                                np.where(filtered_pokemon_data['generation'] == 4, years[3],
                                np.where(filtered_pokemon_data['generation'] == 5, years[4],
                                np.where(filtered_pokemon_data['generation'] == 6, years[5],
                                np.where(filtered_pokemon_data['generation'] == 7, years[6],
                                np.where(filtered_pokemon_data['generation'] == 8, years[7], 0))))))))

filtered_pokemon_data.insert(2, column='date_published', value = my_years)
filtered_pokemon_data.to_csv('filtered_pokemon_data_years.csv', index=False)
print(filtered_pokemon_data)
