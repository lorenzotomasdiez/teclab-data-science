---
tags:
  - ml
---
# Anotaciones
#### Objetivos
- Como preparar los datos
- Aprendizaje supervisado
- Aprendizaje no supervisado

Podemos obtener una prediccion del futuro en base a la historia?
- Si podemos pero depende de los datos la certeza que tengamos.

Que es un analisis predictivo? 
El analisis predictivos es el proceso de utilziar informacion para realizar predicciones basadas en datos. En este proceso se hace uso de los datos junto con tecnicas analiticas, estadisticas y de aprendizaje automatico a fin de crear un modelo para predecir eventos futuros. 

- Conjunto de datos (dataset) -> Materia prima
- Entrenamiento -> datos que se construye el modelo
- Validacion: datos que se valida el modelo

### Preparacion del set de datos
- Voy a google colab
- Instalo librerias
- Cargo y visualizo los datos
- valido tipos de datos
- valido si hay faltantes
- representar el patron de los datos y entender su distribucion

### Que es el ML?
Es una subcategoria de ML y permite que las computadoras o maquinas aprendan patrones o conductas sin la necesidad de programar los pasos. Tambien podemos decir que es la inteligencia de negocios.
Podemos decir que el ML es la "union de habilidades con ordenadores y las matematicas y estadisticas"

Historia:
- **1812 Teorema de Bayes:**
	- Método para calcular la probabilidad de un evento usando información previa sobre un evento relacionado que ya ocurrió. Ejemplo: probabilidad de lluvia el jueves, dada la lluvia del miércoles y sus característica
- **1940 - Bases de la programación informática:**
	- Se establecen las bases de máquinas que permiten seguir una serie de acciones secuenciadas en un computador.
- **1950 – Primeras investigaciones de máquinas inteligentes en relación con redes neuronales:**
	- Se crean las primeras neuronas artificiales basadas en computación, que tienen como finalidad transmitir información entre ellas. Para lograr esto, se creó un programa informático que tenía como desafío lograr sacar una bolita de un laberinto, sin tener alguna programación previa para poder lograrlo, sino que aprendía, a partir de ejemplos de salidas que se proporcionaban con anterioridad.
- **1950 – IBM crea el primer programa exitoso del juego de mesa de damas**
- **1967 – K vecinos más próximos**:
	- Se desarrolla el algoritmo _Nearest Neighbors_ que es considerado el nacimiento de los algoritmos de clasificación supervisada, la cual consta del reconocimiento de patrones más cercanos a una vecindad de datos.
- **2003 – Estudios de sistemas de ficheros distribuidos _Google File System_ (GFS):**
	- Se presenta un nuevo paradigma de procesamiento distribuido al que se llamará _Map & Reduce_.
- **Actualidad - Asistentes personales y estudios**
	- Hoy en día, el _machine learning_ está presente en distintos campos de aplicación, desde la toma de decisiones estratégicas de empresas, que permiten predecir datos de fuga de clientes, segmentación de mercados mediante criterios puntuales; reconocimiento de rutas más cortas de viajes; uso de asistentes personales mediante Siri (Apple), Alexa (Amazon); así como en el campo de la medicina permite predecir enfermedades mediante datos e imágenes.

## Aprendizaje Supervisado:
Consiste en entrenar un algoritmo con datos previamente etiquetados para que pueda hacer predicciones en situaciones similares. Como ejemplo cotidiano, cuando éramos pequeños y nuestros padres nos enseñaban a diferenciar entre un perro y un gato, ellos etiquetaban cada animal, y nosotros, como un algoritmo, aprendíamos a identificarlos. En machine learning, el aprendizaje supervisado sigue esta lógica: el modelo recibe datos con etiquetas claras (ej., si un vehículo tiene dos o cuatro ruedas) y aprende a clasificar entradas nuevas basándose en ese entrenamiento previo.
#### **Clasificación binaria**:
Es un tipo de aprendizaje supervisado que clasifica datos en dos grupos, como "normal" (1) o "anormal" (0). Aplicaciones comunes incluyen:
- **Fraude bancario**: Detección de transacciones fraudulentas.
- **Deserción estudiantil**: Predicción de alumnos que pueden abandonar la carrera.
- **Detección de spam**: Clasificación de correos como "spam" o "no spam".
- **Fuga de clientes**: Predicción de cancelación de suscripciones.
- **Conversión de ventas**: Predicción de si un cliente comprará un artículo.

##### Consideraciones de aprendizaje supervisado
- En esta modalidad de _machine learning_, los algoritmos aprenden de los datos introducidos por una persona (o de un set de datos con resultados conocidos).
- Se necesita la intervención humana para etiquetar, clasificar e introducir los datos en el algoritmo.
- El algoritmo genera datos de salida esperados (etiquetas esperadas), ya que en la entrada han sido clasificados por alguien. 
- Si las etiquetas no han sido clasificadas de manera correcta, por consecuencia, la máquina aprenderá de manera errónea y entregará resultados que no se condicen con lo esperado.


## Aprendizaje no supervisado
Este tipo de aprendizaje permite a las máquinas identificar patrones y crear agrupaciones en datos no etiquetados, resolviendo problemas desconocidos sin necesidad de datos preclasificados. Así, los algoritmos encuentran similitudes y organizan la información por sí mismos. Ejemplos comunes incluyen segmentar clientes en marketing, clasificar plantas en biología o agrupar epicentros de terremotos para identificar áreas de riesgo.

El aprendizaje no supervisado es útil para descubrir patrones nuevos en datos desconocidos, pero tiene desventajas, como menor precisión en los resultados y la necesidad de interpretación humana para comprender y etiquetar los grupos.

##### Ejemplo:
Imaginá una librería grande con miles de libros de los que no conocemos el género. Si aplicamos aprendizaje no supervisado, el algoritmo podría identificar patrones basados en palabras, temas o estilos y agrupar los libros en categorías parecidas. Luego, una persona podría revisar esos grupos para etiquetar: "esto parece ser misterio", "esto romance", etc. En este caso, la máquina solo identificó patrones y creó grupos; el etiquetado final depende de un experto.

Este tipo de agrupación es útil, por ejemplo, para identificar tendencias en moda o entender patrones de consumo sin información detallada sobre cada dato.

Clasificaciones clásicas que surgen en el aprendizaje no supervisado nos pueden ayudar a responder preguntas del tipo:
- ¿Están surgiendo nuevos grupos masivos de fraude?
- ¿Están surgiendo nuevos patrones de compra para la promoción de moda de otoño-invierno?

**Desventajas del aprendizaje no supervisado**
Si bien ambos modelos de aprendizaje —supervisado y no supervisado— son altamente utilizados, el aprendizaje no supervisado tiene ciertas desventajas respecto a la precisión de la información que uno quisiera obtener, a continuación, se detallan algunas consideraciones:  

- No se puede obtener información precisa con respecto a la clasificación de datos. **La salida de datos utilizados en el aprendizaje no supervisado es no etiquetada y no se conoce.**
- **Hay menor precisión de los resultados**, esto se debe a que los datos de entrada no son conocidos y no están etiquetados de antemano por la gente. Esto significa que la máquina requiere hacer esto por sí misma.
- El usuario necesita dedicar tiempo a interpretar y etiquetar las clases que siguen esa clasificación.

Entonces, el aprendizaje no supervisado ayuda a descubrir conexiones ocultas en los datos y a segmentarlos en grupos útiles sin necesidad de un etiquetado inicial, lo cual da ventaja al entender mejor tanto a clientes como a problemas complejos en ciencias y otros campos.

## Preparando datos para su analisis
### Predicción de datos
#### Conjuntos de datos (data set):
Es la materia prima del sistema de predicción. Es el histórico de datos que se usa para entrenar al sistema que detecta los patrones. El conjunto de datos se compone de instancias; y las instancias, de factores, características o propiedades.

#### Entrenamiento y validacion:
**Muestra de entrenamiento:** estos son los datos con los que se construye el modelo.  
  
**Muestra de validación:** es una porción de datos que se usa para validar el modelo (prevenir sobreajuste o subajuste).

A modo estándar, ambas muestras, en general, están compuestas por un 70-30, donde el 70 % de los registros corresponde a la muestra de entrenamiento y el 30 % corresponde a validación.

En algunos casos, puede usarse una proporción de 80-20 o, incluso, 90-10. El objetivo es evaluar la capacidad predictiva del modelo en un segmento distinto al de entrenamiento.  

La finalidad de las muestras de entrenamiento y validación es poder testear bajo distintos escenarios el aprendizaje del algoritmo, en otras palabras:

### Preprocesamiento de _data sets_

- **Paso 2: carga y visualización de datos**
- **Paso 3: entender los datos – tipos**
- **Paso 4: entender los datos y valores faltantes**
- **Paso 5: representar el patrón de los datos**

### Imputación de variables
La imputación de variables es una parte del proceso de _data sets_ que siempre la encontraremos en la gran mayoría de los conjuntos de datos que trabajemos.

Estos datos representan aquellos en los que no se almacena ningún valor de datos en una observación. Es por ello que es de vital importancia identificarlos y trabajarlos para su imputación, pero ¿por qué deberíamos imputar datos?  
  
Esto se debe a que, en _machine learning_, debemos intentar trabajar con los valores lo más limpios y completos posible, para un posterior análisis y entrenamiento de los modelos, por eso, es muy importante poder tener un buen preprocesamiento e imputación de las variables, previo al ingreso de los datos al modelo.

Para esto podemos optar por:
-  **Eliminacion de valores nulos**
	- Reducirá la cantidad de datos de la muestra, dejará solo aquellos que son valores numéricos y eliminará las filas en las que se encuentra algún dato faltante
- **Reemplazar por el promedio**
### Ajuste y sobreajuste de datos
El sobreajuste ocurre cuando un modelo aprende demasiado bien los detalles específicos de los datos de entrenamiento, volviéndose incapaz de generalizar con precisión en nuevos datos. Esto sucede cuando el modelo se entrena excesivamente o se expone a datos atípicos, capturando patrones específicos en lugar de generales. En modelos complejos y con menos datos, el sobreajuste es más común. La clave en machine learning es lograr un equilibrio que permita al modelo reconocer patrones generales útiles para futuras predicciones, evitando que dependa demasiado de los datos específicos del entrenamiento.

Existen varios métodos para evaluar cuándo un modelo se está sobreajustando. Uno de los métodos más conocidos es por medio de las gráficas de errores de entrenamiento y de testeo