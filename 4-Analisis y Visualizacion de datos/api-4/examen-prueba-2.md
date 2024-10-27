# Examen de Prueba

- 1. ¿Cuál es la función en Pandas que permite combinar dos DataFrames basándose en columnas comunes?
  - A) *** `pd.concat()` ***
  - B) `pd.merge()`
  - C) `pd.append()`
  - D) `pd.join()`

- 2. Al importar un archivo CSV que contiene caracteres especiales, ¿qué parámetro debemos especificar para evitar problemas de codificación?
  - A) `sep`
  - B) *** `encoding` ***
  - C) `header`
  - D) `index_col`

- 3. ¿Qué método en Pandas se utiliza para cambiar el tipo de dato de una columna?
  - A) *** `astype()` ***
  - B) `convert()`
  - C) `change_type()`
  - D) `set_dtype()`

- 4. En un DataFrame, ¿cómo se accede a la información sobre el número de filas y columnas que contiene?
  - A) `df.size`
  - B) *** `df.shape` ***
  - C) `df.count()`
  - D) `df.length`

- 5. El tipo de dato `object` en Pandas generalmente se utiliza para representar:
  - A) Números enteros
  - B) Números flotantes
  - C) *** Cadenas de texto ***
  - D) Valores booleanos

- 6. ¿Cuál de las siguientes opciones es correcta sobre el método `pd.melt()`?
  - A) *** Convierte datos de formato largo a ancho ***
  - B) Convierte datos de formato ancho a largo
  - C) Elimina columnas no deseadas
  - D) Ordena los datos en el DataFrame

- 7. Para eliminar filas con valores nulos en un DataFrame, utilizamos:
  - A) *** `df.dropna()` ***
  - B) `df.fillna()`
  - C) `df.isnull()`
  - D) `df.notnull()`

- 8. Completar el fragmento con la opción correcta. El Análisis Exploratorio de Datos (EDA) es __________.
  - A) El proceso de modelado predictivo avanzado
  - B) *** La etapa inicial de análisis para resumir las características principales de los datos ***
  - C) La visualización final de los resultados del análisis
  - D) La limpieza y transformación de datos para prepararlos para el análisis

- 9. ¿Qué método se utiliza para obtener un resumen estadístico de las columnas numéricas en un DataFrame?
  - A) `df.info()`
  - B) *** `df.describe()` ***
  - C) `df.summary()`
  - D) `df.statistics()`

- 10. Completar el fragmento con la opción correcta. En la visualización de datos, un histograma es útil para __________.
    - A) Mostrar la relación entre dos variables categóricas
    - B) *** Visualizar la distribución de una variable numérica ***
    - C) Representar datos geográficos en un mapa
    - D) Mostrar cambios en los datos a lo largo del tiempo

- 11. ¿Cuál de las siguientes bibliotecas se construye sobre Matplotlib y proporciona una interfaz más amigable para la visualización?
    - A) *** Seaborn ***
    - B) Pandas
    - C) NumPy
    - D) SciPy

- 12. Para identificar valores atípicos en una columna numérica, podemos utilizar:
    - A) Un diagrama de dispersión
    - B) *** Un boxplot ***
    - C) Un gráfico de barras
    - D) Un mapa de calor

- 13. Completar el fragmento con la opción correcta. La función `pd.read_csv()` se utiliza para __________.
    - A) Exportar datos a un archivo CSV
    - B) *** Importar datos desde un archivo CSV ***
    - C) Leer datos desde una base de datos SQL
    - D) Convertir un DataFrame a formato JSON

- 14. ¿Qué método permite cambiar los nombres de las columnas en un DataFrame?
    - A) *** `df.rename()` ***
    - B) `df.columns()`
    - C) `df.set_names()`
    - D) `df.change_columns()`

- 15. En el contexto del Análisis Exploratorio de Datos, ¿cuál es el propósito principal de utilizar gráficos de dispersión?
    - A) Mostrar la distribución de una variable categórica
    - B) Identificar la relación entre dos variables numéricas
    - C) *** Resumir estadísticas descriptivas de los datos ***
    - D) Visualizar datos faltantes en el conjunto de datos

- 16. ¿Qué significa EDA en el contexto del análisis de datos?
    - A) *** Exploratory Data Analysis ***
    - B) Enhanced Data Algorithm
    - C) External Data Application
    - D) Efficient Data Aggregation

- 17. Completar el fragmento con la opción correcta. Para combinar dos DataFrames apilándolos verticalmente, usamos __________.
    - A) `pd.merge()`
    - B) *** `pd.concat()` ***
    - C) `pd.join()`
    - D) `pd.append_columns()`

- 18. ¿Cuál de las siguientes opciones es correcta sobre la correlación entre dos variables?
    - A) Siempre implica una relación causal
    - B) *** Indica una relación entre las variables, pero no necesariamente causalidad ***
    - C) Significa que una variable es dependiente de la otra
    - D) No es útil en el análisis de datos

- 19. La paradoja de Simpson nos advierte sobre:
    - A) La importancia de los datos faltantes en el análisis
    - B) Los efectos de la multicolinealidad entre variables
    - C) *** Cómo las tendencias pueden invertirse al cambiar el nivel de agregación de los datos ***
    - D) La necesidad de normalizar los datos antes del análisis

- 20. En Pandas, ¿qué método se utiliza para ordenar un DataFrame basado en los valores de una o más columnas?
    - A) `df.order_by()`
    - B) *** `df.sort_values()` ***
    - C) `df.arrange()`
    - D) `df.sort()`

- 21. Completar el fragmento con la opción correcta. En visualización de datos, Seaborn es especialmente útil para __________.
    - A) *** Crear gráficos estadísticos atractivos y complejos ***
    - B) Manipular grandes conjuntos de datos
    - C) Realizar análisis de series temporales
    - D) Conectar y consultar bases de datos SQL

- 22. ¿Qué método de Pandas permite agrupar datos y aplicar funciones de agregación como la suma o el promedio?
    - A) `df.groupby()`
    - B) *** `df.aggregate()` ***
    - C) `df.transform()`
    - D) `df.apply()`

- 23. Al trabajar con fechas en Pandas, ¿qué función se utiliza para convertir una columna a tipo datetime?
    - A) `pd.to_date()`
    - B) `pd.datetime()`
    - C) *** `pd.to_datetime()` ***
    - D) `pd.date_convert()`

- 24. ¿Cuál de las siguientes afirmaciones es correcta respecto a los datos faltantes?
    - A) Siempre deben eliminarse del conjunto de datos
    - B) *** Pueden imputarse utilizando técnicas estadísticas apropiadas ***
    - C) No afectan el análisis si son pocos
    - D) Deben ignorarse para evitar sesgos

- 25. Completar el fragmento con la opción correcta. La función `df.isnull().sum()` en Pandas nos permite __________.
    - A) Reemplazar valores nulos por la suma de la columna
    - B) *** Contar la cantidad de valores nulos por columna ***
    - C) Eliminar las filas que contienen valores nulos
    - D) Llenar los valores nulos con ceros

- 26. En el análisis de datos, ¿qué es una hipótesis nula (H0)?
    - A) Una afirmación que buscamos probar como verdadera
    - B) Una afirmación inicial que se presume verdadera hasta que se demuestre lo contrario
    - C) Una conclusión obtenida después del análisis
    - D) *** Una suposición que no puede ser probada con datos ***

- 27. ¿Qué biblioteca de Python es fundamental para cálculos numéricos y es utilizada por Pandas para manejar matrices y operaciones numéricas?
    - A) Matplotlib
    - B) *** NumPy ***
    - C) Seaborn
    - D) SciPy

- 28. Completar el fragmento con la opción correcta. El coeficiente de correlación de Pearson mide __________.
    - A) *** La fuerza y dirección de una relación lineal entre dos variables ***
    - B) La diferencia entre medianas de dos conjuntos de datos
    - C) La distribución de frecuencias de una variable categórica
    - D) La probabilidad de un evento en un espacio muestral

- 29. ¿Cuál es el objetivo principal de la comunicación efectiva en el análisis de datos?
    - A) Mostrar habilidades técnicas avanzadas
    - B) *** Compartir hallazgos y apoyar decisiones informadas ***
    - C) Impresionar a la audiencia con visualizaciones complejas
    - D) Pdresentar la mayor cantidad de información posible sin simplificar

- 30. Verdadero o Falso: La correlación implica necesariamente causalidad entre dos variables.
    - A) VERDADERO
    - B) *** FALSO ***

#### FIN DEL EXAMEN DE PRUEBA
