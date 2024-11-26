# Aprendizaje no supervisado
Dentro del machine learning, nos enfrentaremos a problemas en los que los datos disponibles consisten en ejemplos _sin etiquetar_. El objetivo de los algoritmos de aprendizaje no supervisado es aprender patrones útiles o propiedades estructurales de los datos.
- Puede manejar grandes cantidades de datos sin etiquetar y sin estructurar.
- Hace que sea más fácil y rápido analizar datos complejos.
- Es capaz de identificar patrones previamente no detectados.
- Aprende acerca de los datos para que puedan enseñarle lo que no sabe.

**Desventajas del aprendizaje no supervisado**
- No se puede obtener información precisa con respecto a la clasificación de datos y la salida como datos utilizados en el aprendizaje no supervisado está etiquetada y no se conoce.
- La menor precisión de los resultados se debe a que los datos de entrada no son conocidos y no están etiquetados por la gente de antemano. Esto significa que la máquina requiere hacer esto por sí misma.
- Las clases espectrales no siempre corresponden a las clases informativas.
- El usuario necesita dedicar tiempo a interpretar y etiquetar las clases que siguen esa clasificación.
- Las propiedades espectrales de las clases también pueden cambiar con el tiempo, por lo que no puede tener la misma información de clase mientras se mueve de una imagen a otra.

**Los modelos de aprendizaje no supervisados se utilizan para dos tareas principales: agrupar datos y asociar datos.**
- **Agrupación de datos:** es un método para agrupar los objetos en grupos, de modo que los objetos con la mayoría de las similitudes permanezcan en un grupo y tengan menos o ninguna similitud con los objetos de otro grupo. El análisis de conglomerados encuentra los puntos en común entre los objetos de datos y los clasifica según la presencia o ausencia de esos puntos en común.
- **Asociación:** una regla de asociación es un método de aprendizaje no supervisado que se utiliza para encontrar las relaciones entre las variables en la gran base de datos. Determina el conjunto de elementos que aparecen juntos en el conjunto de datos. La regla de asociación hace que la estrategia de _marketing_ sea más efectiva. Por ejemplo, las personas que compran el artículo X (supongamos que un pan) también tienden a comprar el artículo Y (mantequilla/mermelada). Un ejemplo típico de la regla de asociación es el análisis de la cesta de la compra.

### Algoritmos de aprendizaje no supervisado
**Agrupamiento de k-medias**
K-medias o k-means se refiere a una colección de datos agregados debido a ciertas similitudes. Para poder aplicarlo se debe definir un número objetivo, “k”, que se refiere a la cantidad de centroides que se necesita en el conjunto de datos. Un centroide es la ubicación imaginaria o real que representa el centro del grupo.

Dicho de otro modo, lo que buscar este algoritmo es poder agrupar datos en grupos que tendrán como centro del grupo un centroide.

**KNN (k-vecinos más cercanos)**
Este algoritmo tiene como finalidad, asignar un conjunto de datos a cuantos de ellos corresponderán los “k” números de los cuales se va a componer una agrupación. Por ejemplo, si K= 3, quiere decir que sobre el centro de los datos se van a asignar los 3 puntos o vecinos de datos más cercanos. Y si K = 6, se amplía el rango del clúster para asignar a cada agrupación.

**Agrupación jerárquica**
El algoritmo de clúster jerárquico agrupa los datos basándose en la distancia entre cada uno y buscando que los datos que están dentro de un clúster sean los más similares entre sí.

En una representación gráfica los elementos quedan anidados en jerarquías con forma de árbol.

**Análisis de componentes principales**
El análisis de componentes principales es una técnica popular de aprendizaje no supervisado para reducir la dimensionalidad de los datos. Aumenta la interpretabilidad y, al mismo tiempo, minimiza la pérdida de información. 

Su finalidad es ayudar a encontrar las características más significativas en un conjunto de datos y facilita el trazado de los datos en 2D y 3D. PCA ayuda a encontrar una secuencia de combinaciones lineales de variables.
