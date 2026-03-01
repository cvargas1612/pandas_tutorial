import pandas as pd

df = pd.read_csv("pokemon.csv")

jdf = pd.read_json("pokemon.json")

#print(df.tail(10))
#por defecto imprime los primeros 5 y los ultimos 5
#df.to_string() para imprimir todo el archivo

#.head() # por defecto unicamente muestra los primeros 5 pero se puede agregar el numero que queremos de lineas
#dentro de (10) para mostrar 10

#.tail() # por defecto unicamente muestra los ultimos 5 pero se puede agregar el numero que queremos de lineas
#dentro de (10) para mostrar 10

#Seleccion por columna

#probar con las demas columnas
#***

#print(df["Type1"].to_string())


#Seleccionar multiples Columnas
#print(df[["Name", "Height"]].to_string())

#Podemis indexar por otras columnas
df2 = pd.read_csv("pokemon.csv", index_col = "Name")

#print(df2)


#Buscando por filas, usando df2 como dato
#print(df2.loc['Bulbasaur'])
#print(df2.loc['Bulbasaur', ["Height","Weight"]]) #se puede filtrar que datos quiero

#print(df2.loc['Kakuna':'Sandslash', ["Type1","Weight"]]) #ademas se puede agregar un rango
#print(df2.iloc[0:11]) # se pueden filtrar por index numerico
#print(df2.iloc[0:11, 0:3]) # se pueden filtrar ademas las columnas que se quieren ver
