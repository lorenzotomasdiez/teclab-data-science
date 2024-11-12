---
tags:
  - ml
---
# Anotaciones
#### Objetivos
- Scikit Learning 
- Regresion linea simple y multiple
- Matriz de 


# Regresion linea simple y multiple

## Scikit Learn

Scikit learn cuenta con distintos algoritmos de clasificación, regresión y agrupamiento, dentro de los cuales se incluye la aplicación de vectores _random forest, gradient boosting, k-mean_s y DBSCAN_. Los cuales son utilizados para realizar aprendizajes supervisados y no supervisados.

Nos permite realizar analisis de:
1. **Clasificación**:
	- Identificación de categorías a las cuales pertenece un objeto y variable.
	- **Aplicaciones:** detección de _spam_, reconocimiento de imágenes.
	- **Algoritmos:** _super vector machine_ - SVM, KNN - vecinos más cercanos, _random forest_ - bosque aleatorio y más...
2. **Regresión**:
	- Predecir un atributo de valor continuo, asociado con un objeto.
	- **Aplicaciones:** respuesta a medicamentos, precios de acciones.
	- **Algoritmos:** SVR, KNN - vecinos más cercanos, _random forest_ - bosque aleatorio y más...
3. **Agrupación**:
	- Agrupación automática de objetos similares en conjuntos.
	- **Aplicaciones:** segmentación de clientes, agrupación de resultados de experimentos.
	- **Algoritmos:** _K-means_, agrupamiento espectral, desplazamiento medio y más...
4. **Reducción de dimensionalidad**:
	- Reducir el número de variables aleatorias para considerar.
	- **Aplicaciones:** visualización, aumento de la eficiencia. 
	- **Algoritmos:** PCA, selección de características, factorización de matrices no negativas y más...
5. **Preprocesamiento**:
	- Extracción y normalización de características.
	- **Aplicaciones:** transformación de datos de entrada, como texto, para su uso con algoritmos de aprendizaje automático.
	- **Algoritmos:** preprocesamiento, extracción de características y más...
## Regresión lineal simple
Regresión lineal es un método estadístico que tiene como objetivo modelar la relación existente entre una variable continua (comúnmente descrita en el eje Y de un plano cartesiano) y una o más variables independientes (descrita como el eje X dentro de un plano cartesiano) mediante el ajuste de una ecuación lineal.

En el mundo del machine learning es categorizado como algoritmo de aprendizaje supervisado

- Regresión lineal simple cuando, dentro de nuestros datos, solo exista una variable independiente (eje X)
- Regresión lineal múltiple, cuando hay más de una variable independiente que sea parte de un set de datos.

Dependiendo de cada caso, a la variable continua se le denominará variable dependiente o variable respuesta, y a las variables independientes como: regresores, predictores o _features_.

$$ Y = mX + b $$

## Regresión lineal múltiple
La regresión lineal múltiple cumple con ser un modelo estadístico que permite generar un modelo lineal en el que el valor de la variable dependiente o respuesta (Y) se determina a partir de un conjunto de variables independientes llamadas predictores (X1, X2, X3…).

Los modelos de regresión múltiple pueden emplearse para predecir el valor de la variable dependiente o para evaluar la influencia que tienen los predictores sobre ella

#### **Condiciones para una regresión lineal múltiple**
---
##### **No colinealidad o multicolinealidad**
**Concepto simplificado:**

La **colinealidad** ocurre cuando dos o más variables predictoras en un modelo de regresión están altamente correlacionadas entre sí. Esto significa que proporcionan información similar al modelo, lo que dificulta identificar el efecto individual de cada una sobre la variable respuesta.

**¿Por qué es un problema?**

- **Coeficientes inestables**: Los estimadores de los coeficientes pueden cambiar drásticamente con pequeños cambios en los datos.
- **Interpretación difícil**: Es complicado determinar qué variable realmente influye en la respuesta.
- **Significancia estadística reducida**: Aumenta la varianza de los coeficientes, lo que puede hacer que parezcan no significativos.

**Ejemplo práctico:**
Imagina que estás construyendo un modelo para predecir el rendimiento académico de estudiantes y utilizas como variables predictoras el número de horas de estudio y el número de horas dedicadas a tareas. Si los estudiantes que estudian más también dedican más tiempo a tareas, estas dos variables estarán correlacionadas, causando colinealidad.

**Cómo detectarla y manejarla:**
- **Matriz de correlación**: Revisa las correlaciones entre variables predictoras.
- **Factor de Inflación de la Varianza (VIF)**: Un VIF alto indica multicolinealidad.
- **Soluciones**:
    - Eliminar una de las variables correlacionadas.
    - Combinar las variables en una sola (por ejemplo, sumándolas).
    - Utilizar métodos de regularización como regresión ridge o lasso.

---
##### Parsimonia
**Concepto simplificado:**
La **parsimonia** se refiere a la simplicidad en los modelos. Un modelo parsimonioso es aquel que explica los datos de la manera más simple posible, utilizando el menor número de variables necesarias sin perder poder explicativo.

**¿Por qué es importante?**
- **Facilita la interpretación**: Menos variables hacen que el modelo sea más fácil de entender.
- **Mejora la generalización**: Modelos simples suelen funcionar mejor con nuevos datos.
- **Reduce el riesgo de sobreajuste**: Evita que el modelo se ajuste demasiado a las peculiaridades del conjunto de datos actual.

**Ejemplo práctico:**
Supón que estás prediciendo el precio de automóviles y tienes 15 variables predictoras. Después de analizar, descubres que solo 4 de ellas (como el año, el kilometraje, el tipo de combustible y la marca) explican la mayor parte de la variabilidad en los precios. Un modelo parsimonioso usaría solo estas 4 variables en lugar de las 15.

---  
### Relación lineal entre los predictores numéricos y la variable respuesta

**Concepto simplificado:**
Para que un modelo de regresión lineal sea válido, se asume que existe una relación lineal entre cada variable predictora numérica y la variable respuesta, manteniendo constantes las demás variables.

**Cómo verificarlo:**
- **Gráficos de dispersión**: Visualiza cada predictor contra la variable respuesta.
- **Análisis de residuos**: Grafica los residuos (diferencias entre valores observados y predichos) contra cada predictor. Si los residuos se distribuyen aleatoriamente alrededor de cero, la relación es probablemente lineal.

**Ejemplo práctico:**
Si estás analizando cómo el tamaño de una casa (en metros cuadrados) afecta su precio, esperarías ver una relación lineal: a mayor tamaño, mayor precio. Si al graficar notas una curva en los datos, quizás necesites transformar la variable (por ejemplo, usando logaritmos) o considerar un modelo no lineal.

---
### Tamaño de la muestra

**Concepto simplificado:**
Un tamaño de muestra adecuado es esencial para obtener resultados confiables en un modelo de regresión. Si tienes muy pocas observaciones en comparación con el número de variables predictoras, el modelo puede no ser estable ni generalizable.

**Regla general:**
- **Observaciones por predictor**: Se recomienda tener al menos entre 10 y 20 observaciones por cada variable predictora en el modelo.

**¿Por qué es importante?**
- **Estabilidad del modelo**: Más datos permiten estimar los coeficientes con mayor precisión.
- **Evita sobreajuste**: Un modelo ajustado con pocos datos puede captar ruido en lugar de patrones reales.

**Ejemplo práctico:**
Si estás construyendo un modelo con 5 variables predictoras, deberías tener al menos entre 50 y 100 observaciones. Esto ayuda a garantizar que los resultados sean fiables y que el modelo pueda aplicarse a nuevos datos.

---

# Regresión logística e indicadores
## Matriz de confusion
  **Exactitud =** (verdaderos positivos + verdaderos negativos) / total de datos.  
  
**Precisión =** verdaderos positivos / (verdaderos positivos + falsos positivos)  
  
**_Recall_ =** (verdaderos positivos / (verdaderos positivos + falsos positivos)  
  
**Error=** (falsos positivos + falsos negativos) / total de datos




