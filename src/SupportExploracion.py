import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

def traducir(column):
   
    traductor = {
    'CÓDIGO ÓRGÃO SUPERIOR': 'código del órgano superior',
    'NOME ÓRGÃO SUPERIOR': 'nombre del órgano superior',
    'CÓDIGO ÓRGÃO': 'código del órgano',
    'NOME ÓRGÃO': 'nombre del órgano',
    'CÓDIGO UNIDADE GESTORA': 'código de la unidad gestora',
    'NOME UNIDADE GESTORA': 'nombre de la unidad gestora',
    'CATEGORIA ECONÔMICA': 'categoría económica',
    'ORIGEM RECEITA': 'origen de los ingresos',
    'ESPÉCIE RECEITA': 'tipo de ingresos',
    'DETALHAMENTO': 'detalle',
    'VALOR PREVISTO ATUALIZADO': 'valor previsto actualizado',
    'VALOR LANÇADO': 'valor registrado',
    'VALOR REALIZADO': 'valor ejecutado',
    'PERCENTUAL REALIZADO': 'porcentaje ejecutado',
    'DATA LANÇAMENTO': 'fecha de registro',
    'ANO EXERCÍCIO': 'año fiscal'
    }
    traducida = traductor[column]
    rename_columna = {column : traducida}
    return rename_columna

def fill_year(df,year):
    df["año fiscal"].replace(np.nan,year,inplace=True)
    return

def year_to_int(df):
    df["año fiscal"] = df["año fiscal"].astype(int)
    return

def date_to_datetime(df):
    df["fecha de registro"]= pd.to_datetime(df["fecha de registro"],errors="coerce")
    return

def numeric_conversion(df):
    df['valor previsto actualizado'] = pd.to_numeric(df['valor previsto actualizado'].str.replace(',', '.'), errors='coerce')
    df['valor registrado'] = pd.to_numeric(df['valor registrado'].str.replace(',', '.'), errors='coerce')
    df['valor ejecutado'] = pd.to_numeric(df['valor ejecutado'].str.replace(',', '.'), errors='coerce')
    df['porcentaje ejecutado'] = pd.to_numeric(df['porcentaje ejecutado'].str.replace(',', '.'), errors='coerce')
    return

def numeric_conversion(df):
    """
    Convierte las columnas de valores monetarios y porcentaje a formato numérico en un DataFrame.
    Reemplaza las comas por puntos para los decimales y maneja valores no convertibles.

    La función convierte las columnas "valor previsto actualizado", "valor registrado", 
    "valor ejecutado" y "porcentaje ejecutado" a formato numérico (float). 
    Multiplica el "porcentaje ejecutado" por 100 para normalizarlo en una escala de 0 a 100.

    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos a procesar.

    Returns:
        pd.DataFrame: El DataFrame con las columnas especificadas convertidas a formato numérico.
                      Si la conversión falla para algún valor, se reemplaza con NaN.
    """
    df['valor previsto actualizado'] = pd.to_numeric(df['valor previsto actualizado'].str.replace(',', '.'), errors='coerce')
    df['valor registrado'] = pd.to_numeric(df['valor registrado'].str.replace(',', '.'), errors='coerce')
    df['valor ejecutado'] = pd.to_numeric(df['valor ejecutado'].str.replace(',', '.'), errors='coerce')
    df['porcentaje ejecutado'] = pd.to_numeric(df['porcentaje ejecutado'].str.replace(',', '.'), errors='coerce')
    df['porcentaje ejecutado'] *= 100
    return

def fill_organo_superior(df):
    """
    Rellena los valores nulos en la columna 'nombre del órgano superior' basándose en la correspondencia con 
    la columna 'código del órgano superior'.

    La función crea un diccionario de mapeo utilizando las filas que contienen tanto 'código del órgano superior' 
    como 'nombre del órgano superior' no nulos. A partir de este mapeo, se rellenan los valores nulos en 
    'nombre del órgano superior'.

    Args:
        df (pd.DataFrame): DataFrame con los datos a procesar. Debe contener las columnas 
                           'código del órgano superior' y 'nombre del órgano superior'.

    Returns:
        None: La función modifica el DataFrame original directamente.
    """
    # Nos quedamos sólo con valores válidos
    cod_nombre = df.dropna(subset=['código del órgano superior', 'nombre del órgano superior'])
    # Eliminamos duplicados, de forma que nos quedamos con valores únicos y lo volvemos al código el index
    sin_duplicados = cod_nombre.drop_duplicates(subset=["código del órgano superior"]).set_index("código del órgano superior")
    # Por último lo convertimos a diccionario
    diccionario_cod_name = sin_duplicados["nombre del órgano superior"].to_dict()
    #Reemplazamos los valores nulos por el valor correcto
    df["nombre del órgano superior"].fillna(df["código del órgano superior"].map(diccionario_cod_name), inplace=True)
    return

