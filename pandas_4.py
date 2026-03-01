import pandas as pd

#Manipulando y Limpiando archivos

df = pd.read_csv("workout_example.csv")

df_limpio = df.dropna()

#para editar la variable df directamente
#df.dropna(inplace = True)

print(df.to_string())
print("\n")
print("********************************************************")
print("\n")
print(df_limpio.to_string())