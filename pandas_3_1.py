import pandas as pd

#Filtrando lineas que cumplan una condicion

df = pd.read_csv('pokemon.csv')


#pokemons_mas_altos = df[df["Height"] >= 2]
#pokemons_mas_pesados = df[df["Weight"] >= 100]
pokemons_mas_legendario = df[df["Legendary"] == 1]


print(pokemons_mas_legendario)