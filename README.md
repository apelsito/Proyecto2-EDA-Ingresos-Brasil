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
2. Navega al directorio del proyecto:

   ```python
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```
3. Instala las librerías necesarias

   ```python
    pip install pandas
    pip install numpy
    pip install matplotlib
    pip install seaborn
    ```