# Notas material de lectura

## Hipotesis y Validacion
### Hipótesis, validación y construcción del conocimiento
- La información resulta de agregar contexto y sentido a los datos. El conocimiento resulta de filtrar la información que es efectivamente relevante y útil dentro de nuestro dominio, incrementa nuestro entendimiento. 
- Gestión del conocimiento es la disciplina que se encarga de la gestión de la información relevante y útil dentro de un dominio.
- El conocimiento se comienza a construir en base a preguntas que suelen surgir de algún problema concreto. A partir de ellas nos planteamos hipótesis. Ellas son afirmaciones de las que no tenemos certeza y buscamos validar o constatar con la evidencia.
- Las hipotesis que nos hagamos deben ser contrastables, es decir, deben poder ser probadas y refutadas.


### Como formularnos preguntas
- Se empieza con preguntas originadas en problemas concretos. Relacionados con los procesos, las reglas de decision y los objetivos de las organizaciones.
- Es frecuente que en una organizacion este conocimiento este distribuido en equipos (lo que se conoce como silos de información).
- Es util basarse en la teoria, para generar preguntas e hipotesis.
- La teoria nos dice que en la mayoría de los casos, incrementos en los precios de un producto van a inducir disminuciones en las cantidades vendidas
- No todas las preguntas posibles van a poder responderse con datos generales. Parte del valor agregado del científico de datos es poder orientar sobre qué preguntas tiene sentido plantearse y qué preguntas no.

### Como pensar la validacion de las hipotesis.
- definir las variables mas importantes y la relacion entre ellas.
- es importante tener en cuenta como se generaron los datos, y cuan representativo es el sample.

### Como comunicar hallazgos y conclusiones
- Es uno de los ultimos pasos y se puede hacer mediante reportes, presentaciones o dashboards.
- Es importante tener en cuenta a quien se dirige la presentación.

## Como validar la hipotesis con datos

### Analisis de una variable
- Tras asegurarnos que la variable está lista para ser usada, podremos avanzar hacia entender su distribución
- Podemos usar medidas de resumen o descriptivas. Por ejemplo, la media, mediana, moda, rango, desviacion estandar, etc.
- En algunos casos, puede ser util usar distintas transformaciones sobre alguna variable para poder entender mejor su distribucion.

### Analisis de dos o mas variables
- Podemos usar distintas herramientas descriptivas segun los tipos de variables que consideremos.
- Si tomamos cualitativas, podriamos usar tablas de frecuencia cruzadas.
- Si tomamos variables cuantitativas, podemos usar coeficientes de correlacion y matrices de correlacion.
- Correlación no implica causalidad: explorar correlaciones es diferente a inferir relaciones causa-efecto.
- Correlación lineal fuerte puede deberse a varias razones: causalidad directa, inversa, retroalimentación, tercera variable o coincidencia.
- Correlación espuria: variables sin conexión lógica que muestran correlación.
- Causalidad puede existir sin correlación lineal, pero con asociación no lineal.
- Ejemplo: ventas de helado y casos de insolación correlacionan, pero no se causan mutuamente; ambas dependen de la estación del año.
- Interpretar resultados de correlaciones con precaución y considerar el contexto.

### Niveles de agregacion y paradoja de Simpson
- El nivel que tomemos puede afectar en gran medida a los resultados: si tomáramos un nivel demasiado agregado podríamos hacer un análisis muy superficial o perder detalle importante de las relaciones entre variables, pero si analizamos a un nivel muy granular, tenemos el riesgo de capturar en gran medida “ruido” u otros factores que distorsionen el análisis.
- Nivel de agregación es al que puede accionar nuestro cliente.
- Paradoja de Simpson: esta se da cuando a nivel agregado tenemos un resultado que se revierte cuando lo analizamos a un nivel más desagregado.
- Ejemplo: un gerente nos dice que un departamento no tiene rotación de personal, pero cuando miramos a nivel de empleados vemos que no es asi.
- La paradoja de Simpson nos advierte sobre la importancia de explorar nuestros datos a diferentes niveles de agregación y de desagregación.
- 

### Otros tipos de análisis y de validación de hipótesis

- Es importante entender que hasta ahora sólo hicimos referencia a hipótesis y análisis descriptivo de los datos.
- Tomamos datos observados de lo que ya ocurrió en el pasado o sobre un subconjunto (muestra) de todas las unidades de análisis, no sobre la población completa.
- Si quisiéramos poder hacer afirmaciones más allá de lo que ya conocemos, estaríamos haciendo inferencia.

- En materias futuras vamos a aprender sobre otras formas de extraer conocimientos a partir de los datos disponibles.
- Una de las principales formas son los modelos estadísticos, que podemos usar para, por ejemplo, explicar o predecir una variable en función de otras.
- Para usar cualquiera de estas herramientas es muy importante primero tener una comprensión profunda de los datos disponibles, de las variables y sus distribuciones y de sus potenciales limitaciones.

- Otra forma de validar hipótesis estadísticas son los tests, pruebas o contrastes de hipótesis.
- En ellos buscamos hacer inferencias sobre los parámetros (por ejemplo, media o desvío) de la distribución de una variable usando los datos que ya tenemos.
- En base a la evidencia podemos rechazar o no la hipótesis planteada.