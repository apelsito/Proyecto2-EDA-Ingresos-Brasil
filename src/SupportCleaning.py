import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


def fill_organo(df,diccionario):

    codigos_organo = diccionario
    #Reemplazamos los valores nulos por el valor correcto
    df["nombre del órgano"].fillna(df["código del órgano"].map(codigos_organo), inplace=True)

    # Invertimos el diccionario para mapear nombres a códigos 
    diccionario_inverso = {valor: clave for clave, valor in codigos_organo.items()} 
    #Básicamente cogemos el valor y la clave y lo volvemos clave -> valor y valor -> clave así podemos hacer la tarea a la inversa

    # Rellenamos los valores nulos en 'código del órgano superior' usando el nombre
    df["código del órgano"].fillna(df["nombre del órgano"].map(diccionario_inverso), inplace=True)
    return

def fill_unidad_gestora(df,diccionario):

    codigos_unidadgestora = diccionario
    #Reemplazamos los valores nulos por el valor correcto
    df["nombre de la unidad gestora"].fillna(df["código de la unidad gestora"].map(codigos_unidadgestora), inplace=True)

    # Invertimos el diccionario para mapear nombres a códigos 
    diccionario_inverso = {valor: clave for clave, valor in codigos_unidadgestora.items()} 
    #Básicamente cogemos el valor y la clave y lo volvemos clave -> valor y valor -> clave así podemos hacer la tarea a la inversa

    # Rellenamos los valores nulos en 'código del órgano superior' usando el nombre
    df["código de la unidad gestora"].fillna(df["nombre de la unidad gestora"].map(diccionario_inverso), inplace=True)
    return

def fill_missing_organo_superior(df,diccionario):

    codigos_organo= diccionario
    codigos_organo_superior = { 
        20000: 'Presidência da República',
        22000: 'Ministério da Agricultura, Pecuária e Abastec',
        24000: 'Ministério da Ciência, Tecnologia, Inovações ',
        25000: 'Ministério da Economia',
        26000: 'Ministério da Educação',
        30000: 'Ministério da Justiça e Segurança Pública',
        32000: 'Ministério de Minas e Energia',
        33000: 'Ministério da Previdência Social',
        35000: 'Ministério das Relações Exteriores',
        36000: 'Ministério da Saúde',
        37000: 'Controladoria-Geral da União',
        38000: 'Ministério do Trabalho e Emprego',
        39000: 'Ministério da Infraestrutura',
        41000: 'Ministério das Comunicações',
        44000: 'Ministério do Meio Ambiente',
        49000: 'Ministério do Desenvolvimento Agrário',
        51000: 'Ministério do Esporte',
        52000: 'Ministério da Defesa',
        53000: 'Ministério do Desenvolvimento Regional',
        54000: 'Ministério do Turismo',
        55000: 'Ministério da Cidadania',
        57000: 'Ministério das Mulheres, Igualdade Racial, da',
        58000: 'Ministério da Pesca e Aquicultura',
        63000: 'Advocacia-Geral da União',
        81000: 'Ministério da Mulher, Família e Direitos Huma'
    }
    #Reemplazamos los valores nulos por el valor correcto
    df["código del órgano superior"].fillna(df["código del órgano"].map(codigos_organo), inplace=True)

    #Reemplazamos los nombres nulos volviendo a mirar el código recien añadido
    df["nombre del órgano superior"].fillna(df["código del órgano superior"].map(codigos_organo_superior), inplace=True)
    return

def fill_missing_organo(df,diccionario,diccionario__nombre_organo):

    codigos_unidad_gestora = diccionario

    #Reemplazamos los valores nulos por el valor correcto
    df["código del órgano"].fillna(df["código de la unidad gestora"].map(codigos_unidad_gestora), inplace=True)

    #Reemplazamos los nombres nulos volviendo a mirar el código recien añadido
    df["nombre del órgano"].fillna(df["código del órgano"].map(diccionario__nombre_organo), inplace=True)
    return

def calcular_porcentaje(fila):
    
    if fila["valor previsto actualizado"] > 0:
        operacion = (fila["valor ejecutado"] / fila["valor previsto actualizado"]) * 100
        return operacion
    elif fila["valor registrado"] > 0:
        operacion = (fila["valor ejecutado"] / fila["valor registrado"]) * 100
        return operacion
    else:
        return 0
    