# 📝 Análisis de la Ejecución de Ingresos Públicos en Brasil 📊

Este proyecto analiza los ingresos públicos de Brasil entre 2013 y 2021 📊. El objetivo es identificar las diferencias entre lo previsto y lo ejecutado, examinar su distribución por categorías económicas y detectar tendencias temporales 📅.

## Descripción del Proyecto

Este proyecto analiza la ejecución de los ingresos públicos en Brasil entre 2013 y 2021 📅, destacando las diferencias entre los ingresos previstos y ejecutados 💸. Se realizaron procesos de limpieza de datos 🧹 y análisis exploratorio 🔍 para identificar patrones de subejecución y sobre ejecución en diversas categorías económicas 📊.

Las visualizaciones 📈 proporcionan una comprensión clara de la distribución de los ingresos y revelan oportunidades para mejorar la planificación y gestión de los ingresos públicos en el futuro 💼.

## Estructura del Proyecto 🗂️
Los archivos están estructurados de la siguiente forma:

        
        🗂️ Estructura del Proyecto🗂️
        ├── datos/               # Datos crudos y procesados
        ├    ├─ output/          # Excel Generado tras las fases de limpieza
        ├    ├─ raw/             # Datos entregados por el gobierno de Brasil
        ├── jupyter_notebooks/   # Notebooks de Jupyter con los trabajos realizados
        ├── src/                 # Scripts de procesamiento y correción de datos
        ├── README.md            # Descripción del proyecto      
## Instalación y Requisitos 🛠️

### Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- Python 3.x 🐍
- Jupyter Notebook 📓
- Bibliotecas de Python:
  - `pandas` para manipulación de datos 🧹
  - `numpy` para cálculos numéricos 🔢
  - `matplotlib` y `seaborn` para visualización de datos 📊

### Instalación 🛠️

1. Navega al directorio del proyecto:

   ```python
    cd ejecucion-ingresos-brasil
    ```
2. Instala las librerías necesarias

   ```python
    pip install pandas
    pip install numpy
    pip install matplotlib
    pip install seaborn
    ```
## Fase 1: Análisis Inicial y Unión de Datos 🧹📊
En esta fase, el objetivo fue analizar y preparar los datos de ingresos públicos de Brasil entre 2013 y 2021 para futuras fases del proyecto. Se identificaron varios problemas, como delimitadores incorrectos (``;`` en lugar de ``,``) y la presencia de numerosos valores nulos en columnas clave. Los pasos realizados fueron:

- **Conversión de columnas**: Se tradujeron todos los nombres de columnas al español y se pasaron a minúsculas para unificar el formato 🔄.

- **Relleno y corrección de datos temporales**: Se completó la columna de "año fiscal" y se convirtió la columna "fecha de registro" al formato datetime para asegurar coherencia en las fechas 📅.

- **Conversión de valores financieros**: Se detectó que varias columnas financieras ("valor previsto actualizado", "valor registrado", "valor ejecutado") eran de tipo object, por lo que se convirtieron a valores numéricos para permitir un análisis más preciso 💸.

- **Reducción de valores nulos**: Se identificó una gran cantidad de valores nulos en columnas como "código del órgano superior" y "unidad gestora". Se creó un diccionario de valores únicos que permitió rellenar gran parte de los datos faltantes, reduciendo considerablemente el número de nulos en todas las tablas 🛠️.

- **Resultados**: Al final de esta fase, logramos reducir drásticamente los valores nulos en columnas clave. Por ejemplo, en 2013, el "código del órgano superior" pasó de tener 216 valores nulos a solo 79, y el "nombre de la unidad gestora" de 220 a 5 valores nulos. Este proceso se replicó para todos los años, obteniendo una reducción significativa en cada conjunto de datos 🔍.

Finalmente, una vez que se completó esta limpieza, se unieron los datos de todos los años en un solo conjunto, preparando la base para la siguiente fase del proyecto, donde continuaremos limpiando y perfeccionando los datos ✨.


## Fase 2: Limpieza de los Datos 🧹🧽
El enfoque principal de esta fase fue seguir reduciendo los valores nulos y eliminar columnas no necesarias en el dataset unificado. Los pasos importantes fueron:

- **Reducción de valores nulos en "órgano" y "unidad gestora"**: Se creó un diccionario utilizando los nombres y códigos de los órganos como índices. Este diccionario fue utilizado para rellenar los valores faltantes, asegurando que solo queden nulos cuando tanto el nombre como el código estén vacíos 🔧.

- **Relleno de valores faltantes**: Se desarrollaron funciones para sustituir los valores nulos por datos válidos utilizando diccionarios generados previamente. Esto redujo significativamente los nulos en las columnas de "código del órgano" y "nombre del órgano" 📋.

- **Clasificación de ingresos sin información**: Las columnas de "categoría económica", "origen de los ingresos" y "tipo de ingresos" presentaban una gran cantidad de valores nulos. Para estandarizar estos registros, los valores faltantes se reemplazaron por la etiqueta "Sem informação", clasificando estos casos como desconocidos 📊.

- **Resultados**: Gracias a estas operaciones, las columnas críticas como "código del órgano" y "nombre del órgano" quedaron sin valores nulos. Del mismo modo, se estandarizaron los registros sin información, preparando el dataset para un análisis más detallado en fases posteriores 🛠️.

Este proceso dejó los datos en un estado mucho más limpio y listo para las siguientes fases de análisis.

## Fase 3: Análisis Exploratorio de Datos (EDA) 🔍📊
En esta fase, el objetivo principal fue explorar los datos limpios para entender mejor las tendencias de los ingresos públicos en Brasil entre 2013 y 2021. Se analizaron las categorías de ingresos más relevantes, se evaluaron discrepancias entre lo previsto y lo ejecutado, y se identificaron patrones a lo largo del tiempo.

- **Distribución de Ingresos por Categoría Económica 💼💸**: Se enfocó en las principales categorías de ingresos, identificando que Operações de crédito - mercado interno, Contribuições sociais e Impostos fueron las más relevantes en términos de participación total de los ingresos públicos. Se analizó la diferencia promedio entre ingresos previstos y realizados, observando que algunas categorías, como Receitas de Capital - intra-orçamentárias, mostraron sobre ejecución, mientras que otras, como Receitas de Capital, quedaron por debajo de lo previsto.

- **Análisis Temporal 📅📈**: Se estudiaron las variaciones mensuales y anuales de los ingresos, mostrando fluctuaciones importantes a lo largo del tiempo. Los ingresos de *Receitas Correntes y Receitas de Capital* se distribuyeron de manera **desigual entre 2013 y 2021**, destacando periodos de mayores ingresos y otros con caídas significativas.

- **Identificación de Discrepancias ⚠️📊**: Se identificaron discrepancias notables entre los valores previstos y los realizados, revelando subejecuciones en ciertas categorías. Además, se detectaron registros con información incompleta o incorrecta, como los ingresos clasificados como *"Sem informação"*, que representaban posibles fuentes de distorsión en el análisis general.

Este análisis exploratorio 🔍 permitió obtener un panorama claro de las principales fuentes de ingresos y sus variaciones a lo largo del tiempo. Además, se detectaron y resaltaron discrepancias importantes, proporcionando una base sólida para profundizar en análisis más específicos y formular recomendaciones en fases posteriores 🚀.

## Fase 4: Visualización de Datos 📊✨
En esta fase, se generaron visualizaciones gráficas para facilitar la comprensión de las tendencias de los ingresos públicos de Brasil entre 2013 y 2021. Estas gráficas permitieron identificar patrones y discrepancias importantes en los datos.

- **Comparaciones Temporales**: Se visualizaron los ingresos por mes y por categoría económica para cada año, lo que permitió analizar la evolución de los ingresos y detectar tendencias a lo largo del tiempo 📅📈.

- **Distribución por Categorías**: Gráficas que desglosan los ingresos por cada categoría económica en todos los años analizados, mostrando cómo fluctuaron los ingresos y qué categorías fueron más significativas 💼.

- **Análisis Año a Año**: Para cada año de 2013 a 2021, se crearon gráficos detallados por mes y categoría, ayudando a identificar picos y caídas significativas en la recaudación mensual 🔍.

Estas visualizaciones proporcionaron una visión clara de las variaciones en los ingresos y ayudaron a identificar discrepancias importantes entre lo previsto y lo ejecutado en las distintas categorías económicas 📊.

## Fase 5: Conclusiones y Recomendaciones 📝🔍

### Resumen de Hallazgos:
1. **Discrepancias entre lo previsto y lo realizado**:

- 📉 **Categorías con mayor discrepancia**: Las Receitas de Capital y Receitas de Capital - intra-orçamentárias presentaron importantes discrepancias, con casos de sobre ejecución y subejecución respecto a lo previsto.
- 📊 **Períodos críticos**: Los años 2015 y 2020 fueron especialmente desafiantes, con diferencias significativas entre los ingresos previstos y realizados, coincidiendo con la crisis económica y la pandemia, lo que afectó gravemente las proyecciones.
2. **Tendencias observadas en la ejecución de ingresos:**

- 📅 **Estacionalidad**: Se observaron picos y caídas en los ingresos a lo largo del año, especialmente hacia finales de cada ejercicio, posiblemente asociados a la recaudación de impuestos y ajustes fiscales.
- 📈 **Evolución desigual entre categorías**: Mientras que Operações de crédito - mercado interno y Contribuições sociais mantuvieron una ejecución más estable, otras como Impostos y Outras receitas presentaron fluctuaciones más significativas.
3. **Problemas de calidad de datos**:

- **❗ Cantidad de valores nulos**: Un hallazgo preocupante fue la alta cantidad de valores nulos en columnas clave, como código del órgano superior y unidad gestora. Esto dificulta la robustez de las conclusiones y plantea la necesidad de mejorar la calidad de los datos. Los datos no se pueden considerar completamente sólidos hasta que se resuelvan estos problemas.
### Propuestas de Mejora:
1. **Mejorar la precisión en la planificación de ingresos:**

- 🔄 **Ajustar proyecciones basadas en datos históricos**: Utilizar modelos que integren datos recientes para ajustar las previsiones, considerando los eventos que han afectado significativamente la recaudación.
- 📅 **Refinar las estimaciones estacionales**: Incorporar los ciclos estacionales identificados en las proyecciones para mejorar la precisión en la planificación de ingresos mes a mes.
2. **Fortalecer la gestión de categorías con alta variabilidad:**

- 📊 Revisión de categorías como Receitas de Capital y Impostos: Profundizar en el análisis de estas categorías para identificar las causas de las fluctuaciones y mejorar las estrategias de recaudación.
- 🛠️ Mejorar los sistemas de seguimiento y actualización de datos: Implementar sistemas que permitan monitorear los ingresos en tiempo real, facilitando ajustes rápidos y precisos en las proyecciones.
3. **Mejorar la calidad y completitud de los datos:**

- **❗ Revisión exhaustiva de los datos:** Se necesita una revisión rigurosa de la calidad de los datos antes de la planificación, ya que la cantidad de valores nulos ha sido alarmante. Es crucial recopilar datos más completos y exactos para garantizar que las conclusiones y análisis sean robustos y confiables.
- **📊 Optimizar la recolección de datos:** Asegurar que los organismos responsables de suministrar los datos cumplan con estándares más estrictos para reducir la cantidad de nulos y mejorar la calidad de los conjuntos de datos futuros.
4. **Aumentar la transparencia y comunicación en la ejecución de ingresos:**

- 📢 **Comunicación de expectativas realistas:** Mantener una comunicación más clara sobre las variaciones que puedan surgir durante el año fiscal, ayudando a gestionar mejor las expectativas de los actores involucrados.

Con estas acciones, se podrá mejorar la calidad de los datos, reducir las discrepancias entre lo proyectado y lo realizado, y aumentar la precisión en la planificación y ejecución de los ingresos públicos.

# Contribuciones 🤝

Las contribuciones a este proyecto son muy bienvenidas. Si tienes alguna sugerencia, mejora o corrección, no dudes en ponerte en contacto o enviar tus ideas.

Cualquier tipo de contribución, ya sea en código, documentación o feedback, será valorada. ¡Gracias por tu ayuda y colaboración!

# Autores y Agradecimientos ✍️
## Autor ✒️
**Gonzalo Ruipérez Ojea** - [@apelsito](https://github.com/juanperez) en github
## Agradecimientos
Quiero expresar mi agradecimiento a **Hackio** y su equipo por brindarme la capacidad y las herramientas necesarias para realizar este proyecto con solo una semana de formación. Su apoyo ha sido clave para lograr este trabajo.