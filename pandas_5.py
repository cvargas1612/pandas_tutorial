import pandas as pd

df = pd.read_csv('workout_example.csv')

#tomar en cuenta que, esto solo funciona en este caso con celdas del mismo tipo, en este caso int
#si hubiera una celda con otro tipo de datos faltante, como una fecha daria error

#print(df)


"""
# en ese caso indicariamos, que en caso de encontrar una fecha faltante cual poner

"""
df.fillna({
    "Calories": 130,
    "Date": "2020/01/01"
}, inplace=True)

# se puede indicar que solo reemplace en ciertos casos
#df.fillna({"Calories": 130}, inplace=True)


#df.fillna(999, inplace = True)

print(df.to_string())