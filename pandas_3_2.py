import pandas as pd

#Funciones matematicas en pandas

df = pd.read_csv('pokemon.csv')

#numeric_only se agrega como true dando que algunas columnas no son numeros si no strings
#sum
#min
#max
#count
#Aplica a todo el documento

#print(df.mean(numeric_only=True))

#para una sola columna

#print(df["Height"].sum(numeric_only=True))


#Agrupando datos, esto es agrupando todos los que tenga el mismo dato dentro de la columna que indiquemos

group = df.groupby("Type1")

print(group["Height"].mean())