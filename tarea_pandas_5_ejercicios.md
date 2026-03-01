# Tarea: 5 ejercicios simples de pandas

Usa como base lo visto en clase (`Series`, `DataFrame`, `read_csv`, `read_json`, filtros, `groupby`, limpieza con `dropna` y `fillna`).

## Ejercicio 1: Series basica
1. Crea una `Series` con estos datos: `[100, 102, 204, 202, 203, 204]` y este index: `["a", "b", "c", "d", "f", "g"]`.
2. Imprime:
   - El primer valor usando `iloc`.
   - El valor con etiqueta `"d"` usando `loc`.
   - Solo los valores menores a `200`.
3. Cambia el valor de `"d"` a `250` y vuelve a imprimir la serie completa.

## Ejercicio 2: DataFrame desde diccionario
1. Crea un `DataFrame` con:
   - `Marcas`: `["BMW", "Volvo", "Ford"]`
   - `Pasajeros`: `[3, 7, 2]`
   - Index: `["car1", "car2", "car3"]`
2. Agrega una columna `Costo` con `[1000, 2000, 3000]`.
3. Agrega dos filas nuevas con `pd.concat`:
   - `car4`: `Marcas="Nissan"`, `Costo=2500`
   - `car5`: `Marcas="Kia"`, `Pasajeros=7`, `Costo=1750`
4. Muestra:
   - La fila `car1` con `loc`.
   - La tercera fila por posicion con `iloc`.
   - Solo filas con `Costo >= 2000`.

## Ejercicio 3: Lectura y seleccion con pokemon
1. Carga `pokemon.csv` y `pokemon.json`.
2. Del CSV, imprime:
   - `head(8)`
   - `tail(8)`
3. Muestra solo columnas `Name`, `Type1`, `Height` para las primeras 12 filas.
4. Crea un `DataFrame` con `index_col="Name"` y consulta:
   - Toda la fila de `"Bulbasaur"`.
   - De `"Bulbasaur"`, solo `["Height", "Weight"]`.
   - Rango de `"Kakuna"` a `"Sandslash"` con columnas `["Type1", "Weight"]`.

## Ejercicio 4: Filtros y agrupacion con pokemon
1. Filtra los pokemons legendarios (`Legendary == 1`).
2. Filtra pokemons con `Weight >= 100`.
3. Agrupa por `Type1` y calcula:
   - Promedio de `Height`.
   - Maximo de `Weight`.
4. Ordena el resultado por promedio de `Height` de mayor a menor y muestra los 5 primeros tipos.

## Ejercicio 5: Limpieza y analisis con dataset nuevo
1. Carga `practica_tienda_fitness.csv`.
2. Revisa nulos con `isna().sum()`.
3. Limpia faltantes:
   - `Unidades`: reemplazar por `1`.
   - `Precio_Unitario`: reemplazar por la mediana de la columna.
   - `Metodo_Pago`: reemplazar por `"Efectivo"`.
4. Crea columnas nuevas:
   - `Ingreso_Bruto = Unidades * Precio_Unitario`
   - `Ingreso_Neto = Ingreso_Bruto * (1 - Descuento)`
5. Agrupa por `Sucursal` y `Categoria` para obtener la suma de `Ingreso_Neto`.
6. Muestra la fecha con mayor `Ingreso_Neto` total.

---

## Datos para el Ejercicio 5 (`practica_tienda_fitness.csv`)

```csv
Fecha,Sucursal,Categoria,Producto,Unidades,Precio_Unitario,Metodo_Pago,Descuento,Cliente_Nuevo
2026-02-01,Centro,Proteina,Whey 1kg,3,45.0,Tarjeta,0.10,1
2026-02-01,Norte,Vitaminas,Omega 3,5,18.5,Efectivo,0.00,0
2026-02-02,Sur,Accesorios,Banda elastica,4,12.0,Transferencia,0.05,1
2026-02-02,Centro,Ropa,Camiseta DryFit,2,22.0,Tarjeta,0.00,1
2026-02-03,Norte,Proteina,Caseina 1kg,1,52.0,,0.15,0
2026-02-03,Sur,Vitaminas,Multivitaminico,6,14.0,Efectivo,0.00,1
2026-02-04,Centro,Accesorios,Shaker,8,9.5,Tarjeta,0.00,0
2026-02-04,Norte,Ropa,Short deportivo,3,19.0,Transferencia,0.10,1
2026-02-05,Sur,Proteina,Whey 2kg,2,79.0,Tarjeta,0.05,0
2026-02-05,Centro,Vitaminas,Vitamina D,7,,Efectivo,0.00,1
2026-02-06,Norte,Accesorios,Guantes gym,5,15.0,Tarjeta,0.00,0
2026-02-06,Sur,Ropa,Licra mujer,2,28.0,Tarjeta,0.20,1
2026-02-07,Centro,Proteina,Proteina vegana,3,49.0,Transferencia,0.10,1
2026-02-07,Norte,Vitaminas,Magnesio,4,16.0,Efectivo,0.00,0
2026-02-08,Sur,Accesorios,Cuerda saltar,,11.0,Tarjeta,0.00,1
2026-02-08,Centro,Ropa,Gorra deportiva,3,17.5,Efectivo,0.05,0
2026-02-09,Norte,Proteina,Creatina 300g,6,24.0,Tarjeta,0.00,1
2026-02-09,Sur,Vitaminas,Colageno,2,27.0,Transferencia,0.10,1
2026-02-10,Centro,Accesorios,Muñequeras,4,13.0,Efectivo,0.00,0
2026-02-10,Norte,Ropa,Sudadera,1,35.0,Tarjeta,0.15,0
2026-02-11,Sur,Proteina,Barra proteica caja,5,31.0,Efectivo,0.05,1
2026-02-11,Centro,Vitaminas,Complejo B,4,20.0,Tarjeta,0.00,0
2026-02-12,Norte,Accesorios,Rodillo foam,2,26.0,Transferencia,0.10,1
2026-02-12,Sur,Ropa,Top deportivo,3,21.0,,0.05,1
```
