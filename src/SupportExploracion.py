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