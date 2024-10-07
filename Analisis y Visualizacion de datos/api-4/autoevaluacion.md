### Pregunta 1: Si quisiéramos operacionalizar el concepto de "comprador frecuente", ¿cuál de estas variables nos sería más útil?

**Opciones de selección:**

- Ticket promedio.
- Cantidad de medios de pago distintos que usó.
- Antigüedad de la primera compra.
- Cantidad de veces que compró en un determinado periodo. ✅
- Cantidad de sucursales en las que compró.

**Opción Elegida:** Cantidad de veces que compró en un determinado periodo.

**Justificación:** La variable "Cantidad de veces que compró en un determinado periodo" es la más directamente relacionada con la frecuencia de compra, lo cual es esencial para operacionalizar el concepto de "comprador frecuente". Las otras variables pueden proporcionar información útil sobre el comportamiento del comprador, pero no capturan directamente la frecuencia de compra.

**Ejemplo de Código:**

```python
import pandas as pd

# Supongamos que tenemos un DataFrame con las compras de los clientes
datos = {'cliente_id': [1, 1, 2, 2, 2, 3, 3],
         'fecha_compra': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15', '2023-02-20', '2023-03-01', '2023-03-15']}
df_compras = pd.DataFrame(datos)

# Calcular la cantidad de compras por cliente en el periodo
compras_por_cliente = df_compras.groupby('cliente_id').count()
compras_por_cliente.rename(columns={'fecha_compra': 'cantidad_compras'}, inplace=True)

print(compras_por_cliente)
```

### Pregunta 2: Analizando dos variables numéricas x e y, encontramos que su coeficiente de correlación es cercano a 1, ¿qué nos permite afirmar esto?

**Opciones de selección:**

- Que la relación no está influida por otras variables.
- Que existe asociación lineal, pero que no implica una relación causa-efecto. ✅
- Que la relación va a mantenerse en el futuro.
- Que x e y se causan mutuamente.
- Que x causa y, por lo que implica una relación causa-efecto.

**Opción Elegida:** Que existe asociación lineal, pero que no implica una relación causa-efecto.

**Justificación:** Un coeficiente de correlación cercano a 1 indica una fuerte asociación lineal positiva entre las dos variables; sin embargo, esto no implica causalidad. La correlación mide la fuerza y dirección de una relación lineal entre dos variables numéricas, pero no puede determinar si un cambio en una variable es la causa del cambio en la otra.

**Ejemplo de Código:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Generar datos simulados
x = np.arange(0, 10, 0.5)
y = 2 * x + np.random.normal(0, 1, len(x))

# Calcular el coeficiente de correlación
coef_correlacion = np.corrcoef(x, y)[0,1]

print(f"Coeficiente de correlación: {coef_correlacion}")

# Graficar los datos
plt.scatter(x, y)
plt.title('Relación entre X e Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

### Pregunta 3: En los proyectos de datos frecuentemente tenemos que tomar decisiones sobre el nivel de agregación de los datos, ¿cuál de estos factores va a imponer mayores restricciones?

**Opciones de selección:**

- Problemas de calidad.
- Agregación a la que el cliente puede accionar.
- Restricciones legales. ✅
- Agregación original de los datos crudos.
- Agregación a la que el cliente está acostumbrado a ver los resultados.

**Opción Elegida:** Restricciones legales.

**Justificación:** Las restricciones legales pueden limitar significativamente cómo se pueden recopilar, almacenar, procesar y compartir los datos. Estas restricciones son imperativas y deben cumplirse para evitar sanciones legales. Afectan directamente el nivel de agregación que se puede aplicar a los datos, especialmente cuando se trata de información sensible o personal.

**CORRECCION:** Justificación: La agregación original de los datos nos va a imponer la mayor restricción, debido a que es mucho más sencillo agregar datos originales que tengan desagregación suficiente, que el caso contrario (el cual algunas veces es posible, aunque puede requerir hacer supuestos, por ejemplo).

**Ejemplo de Código:**

```python
# Este ejemplo es más conceptual y se enfoca en cómo podríamos aplicar restricciones legales al procesamiento de datos.

import pandas as pd

# Supongamos que tenemos un DataFrame con información personal
datos_personales = {'nombre': ['Juan', 'Ana', 'Luis'],
                    'edad': [25, 30, 22],
                    'ingreso_anual': [30000, 45000, 28000]}

df_personales = pd.DataFrame(datos_personales)

# Aplicar agregación para cumplir con restricciones legales (ej. GDPR)
# Podemos calcular estadísticas agregadas sin revelar información individual
ingreso_promedio = df_personales['ingreso_anual'].mean()

print(f"Ingreso anual promedio: {ingreso_promedio}")
```

### Pregunta 4: De las siguientes, ¿en qué etapa puede afectar la "maldición del conocimiento"?

**Opciones de selección:**

- Comunicación de las conclusiones. ✅
- Feedback de los clientes y nuevas preguntas.
- Procesamiento de los datos.
- Análisis de los datos.
- Obtención de los datos.

**Opción Elegida:** Comunicación de las conclusiones.

**Justificación:** La "maldición del conocimiento" se refiere a la dificultad que tienen las personas expertas en un tema para imaginar cómo es no tener ese conocimiento. Esto puede afectar significativamente la comunicación de las conclusiones a una audiencia no especializada, ya que el experto puede asumir erróneamente que ciertos conceptos son obvios o fáciles de entender para todos.

**Ejemplo de Código:**

```python
# Este ejemplo es más conceptual y se enfoca en cómo presentar conclusiones de manera efectiva.

# Supongamos que hemos realizado un análisis complejo y queremos comunicar nuestras conclusiones

conclusiones = """
Hemos encontrado una fuerte correlación entre el uso del producto X y la mejora en la satisfacción del cliente.
"""

# Para evitar la maldición del conocimiento:
# - Evitar jerga técnica innecesaria
# - Usar ejemplos o analogías para explicar conceptos complejos
# - Resaltar la importancia y aplicabilidad de las conclusiones

conclusiones_simples = """
Descubrimos que cuando los clientes usan el producto X, tienden a estar más contentos con nuestro servicio.
Esto es similar a cómo sentirse después de tomar una taza de tu café favorito por la mañana; simplemente mejora tu día.
"""

print(conclusiones_simples)
```

### Pregunta 5: Si estuviéramos en la etapa de análisis exploratorio de un proyecto, ¿qué correspondería hacer?

**Opciones de selección:**

- Explorar estudios previos sobre el mismo tema.
- Relevar necesidades del cliente.
- Explorar el conocimiento de dominio sobre el tema del proyecto.
- Usar herramientas de estadística descriptiva. ✅
- Relevar los datos disponibles.

**Opción Elegida:** Usar herramientas de estadística descriptiva.

**Justificación:** Durante el análisis exploratorio de datos (EDA), el objetivo es comprender las principales características del conjunto de datos mediante resúmenes estadísticos y visualizaciones. Esto incluye identificar tendencias, patrones y posibles anomalías en los datos. Usar herramientas de estadística descriptiva es fundamental en esta etapa para obtener una visión general clara y detallada del conjunto de datos con el que se está trabajando.

**Ejemplo de Código:**

```python
import pandas as pd
import seaborn as sns

# Supongamos que tenemos un DataFrame con datos para analizar
datos = {'edad': [25, 30, 22, 40, 28],
         'ingreso_anual': [30000, 45000, 28000, 50000, 32000]}
df = pd.DataFrame(datos)

# Realizar estadísticas descriptivas básicas
print(df.describe())

# Visualizar distribuciones
sns.histplot(df['edad'], kde=True)
sns.histplot(df['ingreso_anual'], kde=True)
```

### Pregunta 6: En la medida en que dispongamos de datos suficientes, estos van a respaldar las hipótesis que planteamos.

**Opciones de selección:**

- Falso ✅
- Verdadero

**Opción Elegida:** Falso

**Justificación:** Tener datos suficientes no garantiza automáticamente que respaldarán las hipótesis planteadas. Los datos pueden revelar tendencias o patrones inesperados que contradigan nuestras hipótesis iniciales. La ciencia de datos es un proceso iterativo donde las hipótesis pueden ser confirmadas o refutadas basándose en el análisis y la interpretación objetiva de los datos disponibles.

**Ejemplo de Código:**

```python
import numpy as np

# Supongamos que tenemos una hipótesis sobre la media poblacional
hipotesis_media_poblacional = 50

# Generamos datos simulados
datos_simulados = np.random.normal(45, 10, 1000) # Media real diferente a la hipotética

# Calculamos la media muestral
media_muestral = np.mean(datos_simulados)

print(f"Media muestral: {media_muestral}")

# Comparar con la hipótesis
if media_muestral == hipotesis_media_poblacional:
    print("La hipótesis se respalda con los datos.")
else:
    print("La hipótesis no se respalda con los datos.")
```

### Pregunta 7: Dada una hipótesis planteada, ¿qué significa operacionalizarla?

**Opciones de selección:**

- Relacionarla con los objetivos del proyecto.
- Expresarla de la forma más específica o desagregada posible.
- Expresarla en función de variables que podamos medir y contrastar con la evidencia. ✅
- Generar datos adicionales que nos sirvan de evidencia.
- Validarla con integrantes de otros equipos.

**Opción Elegida:** Expresarla en función de variables que podamos medir y contrastar con la evidencia.

**Justificación:** Operacionalizar una hipótesis significa traducirla en términos específicos y medibles para poder contrastarla con los datos disponibles. Esto implica definir claramente las variables involucradas y cómo serán medidas o evaluadas dentro del estudio. Es un paso crucial para poder realizar análisis cuantitativos y verificar si los datos respaldan o refutan la hipótesis planteada.

**Ejemplo de Código:**

```python
# Supongamos que nuestra hipótesis es que "El ejercicio regular reduce el estrés"

# Operacionalizar la hipótesis podría implicar definir:
# - "Ejercicio regular" como realizar actividad física moderada al menos 30 minutos al día, 5 días a la semana.
# - "Estrés" como puntuaciones en una escala validada de estrés percibido.

# Simularemos cómo podríamos contrastar esta hipótesis con datos

import numpy as np
import scipy.stats as stats

# Generamos datos simulados para dos grupos (con ejercicio regular vs. sin ejercicio regular)
estrés_con_ejercicio = np.random.normal(4, 1.5, 100) # Menor media suponiendo menor estrés
estrés_sin_ejercicio = np.random.normal(6, 1.5, 100) # Mayor media suponiendo mayor estrés

# Realizamos un test estadístico para comparar las medias
t_statistic, p_value = stats.ttest_ind(estrés_con_ejercicio, estrés_sin_ejercicio)

print(f"t-statistic: {t_statistic}, p-value: {p_value}")

if p_value < 0.05:
    print("Los datos respaldan la hipótesis.")
else:
    print("Los datos no respaldan la hipótesis.")
```

### Pregunta 8: Al momento de presentar conclusiones de un proyecto de datos a una audiencia gerencial, ¿cuál de estas opciones sería más útil?

**Opciones de selección:**

- Usar lenguaje más técnico.
- Exponer distintos temas en la misma presentación.
- Comenzar por un resumen de los resultados más relevantes. ✅
- Mostrar primero la metodología, después los resultados.
- Hacer la presentación lo más corta posible.

**Opción Elegida:** Comenzar por un resumen de los resultados más relevantes.

**Justificación:** Al presentar conclusiones a una audiencia gerencial, es crucial capturar su atención desde el principio y comunicar el valor del análisis realizado. Comenzar con un resumen ejecutivo que destaque los hallazgos más importantes permite a los gerentes comprender rápidamente los resultados clave y cómo estos pueden impactar en las decisiones empresariales.

**Ejemplo de Código:**

```python
# Este ejemplo es más conceptual y se enfoca en cómo estructurar una presentación efectiva.

resumen_resultados = """
Nuestro análisis revela tres hallazgos clave:
1. Existe una correlación positiva significativa entre el uso del producto X y la satisfacción del cliente.
2. Los clientes más jóvenes tienden a usar más frecuentemente el producto X.
3. La implementación del producto X podría aumentar las ventas hasta en un 20%.

Estos resultados sugieren acciones específicas para mejorar nuestro enfoque hacia el mercado objetivo.
"""

# Al preparar una presentación para gerencia:
# - Incluir gráficos claros y concisos para ilustrar los hallazgos clave.
# - Evitar detalles técnicos innecesarios.
# - Enfocarse en cómo los resultados pueden influir en decisiones estratégicas.
```

### Pregunta 9: En la medida en que tengamos datos suficientes, todas las preguntas pueden responderse con ellos.

**Opciones de selección:**

- Falso ✅
- Verdadero

**Opción Elegida:** Falso

**Justificación:** Aunque tener una cantidad suficiente de datos es crucial para realizar análisis robustos, no todas las preguntas pueden ser respondidas únicamente con datos. Algunas preguntas pueden requerir conocimiento contextual o experticia específica fuera del ámbito del conjunto de datos disponible. Además, algunas preguntas pueden ser filosóficas o teóricas por naturaleza y no susceptibles a ser respondidas directamente mediante análisis cuantitativo.

### Pregunta 10: ¿Cuál de estos factores es más probable que haga necesario rehacer etapas de un proyecto?

**Opciones de selección:**

- Operacionalizar hipótesis.
- Plantearnos las preguntas en un orden incorrecto. ✅
- Que nuestros clientes/stakeholders tengan poco compromiso.
- Que existan limitaciones de presupuesto.
- Escribir código poco eficiente o poco mantenible.

**Opción Elegida:** Plantearnos las preguntas en un orden incorrecto.

**Justificación:** Plantearse las preguntas en un orden incorrecto puede llevar a malentendidos sobre los objetivos del proyecto o a recopilar y analizar datos irrelevantes para las necesidades reales del proyecto. Esto puede resultar en tener que volver atrás y rehacer etapas del proyecto para alinearlas correctamente con los objetivos deseados y las preguntas clave que necesitan respuesta.

**Ejemplo Conceptual:**

En este caso no se proporciona un ejemplo específico de código debido a la naturaleza conceptual y estratégica del problema planteado. La solución implica revisión y ajuste en la planificación y ejecución del proyecto más que una solución codificada.