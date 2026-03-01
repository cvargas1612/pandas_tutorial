import pandas as pd

#Es un Objeto, la key es el nombre de las columnas por defecto o 1-D, de una dimencion
#Cada set de datos de la Key se ordenan hacia abajo en su respectiva columna
#Una serie es una columna de datos

data_serie = [100, 102, 204, 202, 203, 204]


#series = pd.Series(data_serie)

series = pd.Series(data_serie, index=["a", "b", "c", "d", "f", "g"]) #esto cambia labels

#.iloc para entrar por interger [0]

#print(series.iloc[0])

#print(series.loc["d"]) #puede usar usado para cambiar el valor tambien

#print(series[series < 200]) #se puede crear un filtro para buscar datos dentro de la serie

#print(series)



calorias = {
  "Dia 1": 1750,
  "Dia 2": 3250,
  "Dia 3": 1600,
}

serie_c = pd.Series(calorias)

#print(serie_c)


