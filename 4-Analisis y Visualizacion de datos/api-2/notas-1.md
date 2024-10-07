# Notas de Clase Online 1: Análisis de Datos con Python

## Introducción

En esta clase, abordaremos conceptos fundamentales relacionados con la manipulación y análisis de datos utilizando Python y la biblioteca Pandas. Estos conceptos son esenciales para gestionar y transformar datos de forma efectiva.

## Estructura de un DataFrame

### Forma (Shape)

La forma de un DataFrame se refiere al número de filas y columnas que contiene. Se puede acceder a esta información utilizando la propiedad `shape`:

```python
shape = df.shape  # Retorna una tupla (filas, columnas)
```

### Tipos de Datos (dtypes)

Cada columna de un DataFrame tiene un tipo de dato asociado. En Python, esto se puede verificar con `dtypes`. Si es necesario, se puede cambiar el tipo de dato utilizando el método `astype`. Por ejemplo:

```python
df = df.astype({"pais": str, "year": int, "crecimiento_pbi": float})
```

### Tipo Object

El tipo `object` en Pandas se utiliza para representar datos que no tienen un tipo definido, como cadenas de texto. Es importante identificar y gestionar adecuadamente estos tipos de datos.

## Codificación de Archivos

Al importar datos, especialmente de diferentes regiones, es crucial especificar la codificación. Para regiones que utilizan caracteres especiales, se recomienda usar:

```python
encoding = "latin-1"
```

## Manejo de Archivos

### Saltar Filas Finales

Al importar un archivo, se puede omitir un número determinado de filas al final utilizando el parámetro `skipfooter`:

```python
df = pd.read_csv("archivo.csv", skipfooter=3)
```

### Filtrar Datos

Para filtrar datos en un DataFrame, se puede usar el método `isin`. Por ejemplo, para seleccionar filas que contienen ciertos valores en una columna:

```python
df_filtrado = df[df["nombre_columna"].isin(["x", "xx"])]
```

### Eliminar Columnas

Si hay columnas que no son de interés, se pueden eliminar de la siguiente manera:

```python
df = df.drop(columns=["nombre_columna"])
```

### Modificar Estructura de la Tabla

Para cambiar la estructura de un DataFrame, se puede utilizar la función `pd.melt`. Esto es útil para transformar datos de formato ancho a formato largo:

```python
df_melted = pd.melt(df, id_vars=["columnas_sin_modificar"], var_name="year", value_name="crecimiento_pbi")
```

### Renombrar Columnas

Es posible renombrar columnas utilizando el método `rename`:

```python
df = df.rename(columns={"Country": "pais"})
```

### Ordenar Filas

Para ordenar las filas de un DataFrame, se utiliza el método `sort_values`:

```python
df = df.sort_values(by=["pais", "year"])
```

### Descripción Estadística

Para obtener información estadística sobre las columnas, se puede utilizar el método `describe`:

```python
estadisticas = df["crecimiento_pbi"].describe()
```

## Combinación de DataFrames

### Merge y Concatenación

Para combinar DataFrames, se pueden utilizar `merge` y `concat`.

- **Merge**: Permite combinar DataFrames basándose en columnas comunes, especificando el tipo de combinación (inner, outer, left, right):

```python
df_combinado = pd.merge(df1, df2, on="columna_comun", how="inner")
```

- **Concatenación**: Combina DataFrames apilando uno encima del otro, siempre que tengan las mismas columnas:

```python
df_concatenado = pd.concat([df1, df2], axis=0)
```

## Funciones de Agregación

Las funciones de agregación permiten resumir datos agrupándolos y aplicando funciones como suma o promedio. Por ejemplo, para calcular el promedio de `crecimiento_pbi` por país:

```python
df_agregado = df.groupby(["pais"], as_index=False).agg({"crecimiento_pbi": "mean"})
```

El parámetro `as_index=False` indica que no se debe utilizar el índice como columna en el resultado.

## Resolución del Caso Práctico (API2)

1. Cargar la población y especificar la codificación:
   ```python
   df_poblacion = pd.read_csv("poblacion.csv", encoding="latin-1")
   ```
2. Eliminar la fila total de país, que no es relevante.
3. Cargar el dataset de hogares y viviendas con el mismo encoding:
   ```python
   df_hogares = pd.read_csv("hogares_viviendas.csv", encoding="latin-1")
   ```
4. Eliminar también la fila total de país en este DataFrame.
5. Realizar un merge utilizando la columna `provincia` para obtener la superficie correspondiente:
   ```python
   df_resultado = pd.merge(df_hogares, df_poblacion, on="provincia")
filenotfounderror: [Errno 2] No such file or directory: '/home/ruffossj/study/teclab-data-science/Analisis y Visualizacion de datos/api-2/api-2-archivos/poblacion.csv'   ```
6. Crear una nueva columna llamada `densidad`, calculando la densidad poblacional:
   ```python
   df_resultado["densidad"] = df_resultado["poblacion_total"] / df_resultado["superficie_km2"]
   ```
7. Exportar el DataFrame final como un archivo CSV sin el índice:
   ```python
   df_resultado.to_csv("resultado.csv", index=False)
   ```

## Conclusión

El manejo y análisis de datos con Python y Pandas es una habilidad crucial en ciencia de datos. A través de la comprensión y aplicación de estos conceptos, se puede transformar y analizar datos de manera efectiva.

## Recursos Adicionales

Para profundizar en los temas tratados, se recomiendan los siguientes recursos:

- **Libros**:
  - "Python for Data Analysis" de Wes McKinney.
  - "Data Science from Scratch" de Joel Grus.

- **Artículos**:
  - "Pandas Documentation" [enlace](https://pandas.pydata.org/pandas-docs/stable/)
  - "Data Manipulation with Pandas" [enlace](https://realpython.com/pandas-dataframe/)

- **Cursos Online**:
  - Coursera: "Applied Data Science with Python" por la Universidad de Michigan.
  - edX: "Data Science MicroMasters" por la Universidad de California, San Diego.