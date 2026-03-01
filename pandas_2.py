import pandas as pd

#Diccionario o data.csv frame


#Puede llamarce diccionario, Json o objeto

mydataset = {
  'Marcas': ["BMW", "Volvo", "Ford"],
  'Pasajeros': [3, 7, 2]
}


myvar = pd.DataFrame(mydataset)

myvar = pd.DataFrame(mydataset, index=["car1", "car2", "car3"])
#print(myvar.loc["car1"])

#print(myvar.iloc[2])


# agregar una nueva columna

myvar["Costo"] = [1000, 2000, 3000]


#agregar una nueva linea

#new_linea = pd.DataFrame([{"Marcas":"Nissan", "Pasajeros": 5}])

#new_linea = pd.DataFrame([{"Marcas":"Nissan", "Pasajeros": 5}], index=["car4"]) #se puede agregar un index

new_lineas = pd.DataFrame([{"Marcas":"Nissan", "Costo": 2500}, {"Marcas":"Kia", "Pasajeros": 7, "Costo": 1750}], index=["car4", "car5"]) #se puede agregar un index


myvar = pd.concat([myvar, new_lineas])


print("\n\n*****tabla original")
print(myvar)