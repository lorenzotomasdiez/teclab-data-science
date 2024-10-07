# Autoevaluación

### 1. ¿Cuál de las siguientes es una medida de posición o tendencia central?

- **Mediana**
- Rango intercuartílico
- Modalidad
- Asimetría
- Curtosis

**Opción Elegida:** Mediana

**Justificación:** La mediana es una medida de tendencia central que divide un conjunto de datos ordenados en dos partes iguales. A diferencia del rango intercuartílico, la modalidad, la asimetría y la curtosis, que son medidas de dispersión, forma y distribución, la mediana se centra en identificar el valor medio en un conjunto de datos.

**Ejemplo de Código:**

```python
import numpy as np

datos = np.array([1, 3, 3, 6, 7, 8, 9])
mediana = np.median(datos)
print("La mediana es:", mediana)
```

### 2. ¿Cuál de las siguientes medidas nos sirve para analizar la asociación lineal entre dos variables?

- Rango.
- **Correlación.**
- Curtosis.
- Mediana.
- Mínima.

**Opción Elegida:** Correlación

**Justificación:** La correlación es una medida estadística que indica el grado de asociación lineal entre dos variables. Valores cercanos a 1 o -1 indican una fuerte relación lineal positiva o negativa, respectivamente, mientras que un valor cercano a 0 indica una falta de relación lineal.

**Ejemplo de Código:**

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

correlacion = np.corrcoef(x, y)[0, 1]
print("La correlación entre x e y es:", correlacion)
```

### 3. Si estuviéramos leyendo un diagrama de caja o boxplot y viéramos señalado Q2, ¿a qué estaría haciendo referencia?

- Media.
- Mínima.
- Máxima.
- Rango intercuartílico.
- **Mediana.**

**Opción Elegida:** Mediana

**Justificación:** En un diagrama de caja o boxplot, Q2 se refiere al segundo cuartil, que es equivalente a la mediana. Divide el conjunto de datos en dos partes iguales.

**Ejemplo de Código:**

```python
import matplotlib.pyplot as plt
import numpy as np

datos = np.random.normal(loc=0, scale=1, size=100)
plt.boxplot(datos)
plt.title("Diagrama de Caja")
plt.show()
```

### 4. ¿Para qué usaríamos la función de numpy corrcoef?

- Diagramas de dispersión.
- Paneles de histogramas.
- Percentiles.
- **Matrices de correlación.**
- Cantidad de missings.

**Opción Elegida:** Matrices de correlación

**Justificación:** La función `np.corrcoef()` se utiliza para calcular la matriz de correlación entre dos o más variables, permitiendo evaluar el grado de asociación lineal entre ellas.

**Ejemplo de Código:**

```python
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([10, 11, 12, 13])

matriz_correlacion = np.corrcoef(x, y)
print("Matriz de correlación:\n", matriz_correlacion)
```

### 5. Para construir paneles de gráficos en base a los valores de alguna variable categórica y que compartan los mismos ejes, ¿qué función de seaborn usaríamos?

- **FacetGrid.**
- Trellischarts.
- Subplots.
- Panels.
- Smallmultiples.

**Opción Elegida:** FacetGrid

**Justificación:** `FacetGrid` es una clase en Seaborn que se utiliza para crear una matriz de gráficos basada en los niveles de una o más variables categóricas. Permite explorar rápidamente diferentes perspectivas de un conjunto de datos.

**Ejemplo de Código:**

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time", row="smoker")
g = g.map(plt.hist, "total_bill")
```

### 6. Si estuviéramos construyendo un diagrama de dispersión, ¿cuáles de estas opciones podrían agregar más información sobre las distribuciones de cada variable?

- **Gráficos marginales.**
- Invertir los ejes.
- Agregar una línea de tendencia.
- Cambiar el color de los marcadores.
- Cambiar la forma de los marcadores.

**Opción Elegida:** Gráficos marginales

**Justificación:** Los gráficos marginales añaden histogramas o densidades en los márgenes del diagrama de dispersión principal. Esto proporciona información adicional sobre la distribución individual de cada variable.

**Ejemplo de Código:**

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter", marginal_kws=dict(bins=25, fill=True))
plt.show()
```

### 7. Para construir un gráfico de burbujas, ¿qué función utilizaríamos?

- Bubbleplot.
- **Scatterplot.**
- Bubble.
- Figure.

**Opción Elegida:** Scatterplot

**Justificación:** Aunque no existe una función específica llamada `Bubbleplot` en las bibliotecas comunes como Matplotlib o Seaborn, podemos utilizar `scatterplot` y ajustar el tamaño de los puntos (burbujas) para representar una tercera variable.

**Ejemplo de Código:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 11, 12, 13]
sizes = [60, 120, 180, 240] # Representa el tamaño de las burbujas

plt.scatter(x, y, s=sizes)
plt.title("Gráfico de Burbujas")
plt.show()
```

### 8. La principal ventaja de matplotlib sobre seaborn es que su sintaxis es más simple.

- Falso.
- **Verdadero.**

**Opción Elegida:** Falso

**Justificación:** La principal ventaja de Matplotlib sobre Seaborn no es que su sintaxis sea más simple; al contrario, Seaborn está diseñado para ser una interfaz más alta y más fácil de usar que Matplotlib. Matplotlib ofrece mayor flexibilidad y control sobre los aspectos del gráfico.

### 9. Si estuviéramos leyendo un diagrama de cajas y bigotes (boxplot), y viéramos un punto por encima del límite de los bigotes, ¿por encima de qué valor está?

- Q2.
- Q3 - Q1.
- Q3 - 1.5 * (Q3 - Q1).
- **Q3 + 1.5 * (Q3 - Q1).**
- Q1 - 1.5 + rango intercuartílico.

**Opción Elegida:** Q3 + 1.5 * (Q3 - Q1)

**Justificación:** En un boxplot, los puntos que se encuentran por encima del bigote superior representan valores atípicos. El bigote superior termina en Q3 + 1.5 * (Q3 - Q1), donde cualquier punto por encima de este valor se considera un valor atípico.

**Ejemplo de Código:**

```python
import matplotlib.pyplot as plt
import numpy as np

datos = np.random.normal(loc=0, scale=1, size=100)
plt.boxplot(datos)
plt.title("Diagrama de Cajas y Bigotes")
plt.show()
```

### 10. En matplotlib, existe una única manera de escribir la sintaxis para generar un gráfico.

- Verdadero
- **Falso**

**Opción Elegida:** Falso

**Justificación:** Matplotlib ofrece flexibilidad en la forma en que se puede generar un gráfico. Existen múltiples maneras de escribir la sintaxis para crear visualizaciones complejas o simples, incluyendo el uso del estilo orientado a objetos o el estilo pyplot.

**Ejemplo de Código:**

```python
# Estilo orientado a objetos
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Estilo pyplot
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()