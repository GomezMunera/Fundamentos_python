# -*- coding: utf-8 -*-
"""
prueba panda
"""

import pandas as pd

# Lee desde CSV a un Pandas DataFrame
df = pd.read_csv("TSLA.csv", header=0)

lowes_valor = df["Low"].min()
ind_menor = df.index[df['Low'] == lowes_valor].tolist()
#ind_menor = df.index[df['Low'] == lowes_valor]

print("indice menor: ", ind_menor[0])

# forma 2
#print("Índice menor con la forma 2: ",df.loc[df['Low'] == lowes_valor])

high_valor = df["High"].max()
ind_mayor = df.index[df['High'] == high_valor].tolist()
print("indice mayor: ", ind_mayor[0])

#%%
df["Date"][0]

#%% pruebas condicionales
# verifica las codiciones para asignar a la columna concepto
dfp.loc[df.Close < 200, 'Concepto'] = 'MUY BAJO'
dfp.loc[df.Close >= 600, 'Concepto'] = 'MUY ALTO'

#%%

import numpy as np

dfp = pd.DataFrame()
dfp['Date'] = None
dfp = dfp.assign(Concepto=None)
print(dfp)

dfp["Date"] = df["Date"]

conditions = [
    (df["Close"] < 200),
    (df["Close"] >= 200) & (df["Close"] < 300),
    (df["Close"] >= 300) & (df["Close"] < 500),
    (df["Close"] >= 500) & (df["Close"] < 600),
    (df["Close"] >= 600)]

choice =['MUY BAJO','BAJO','MEDIO','ALTO','MUY ALTO']

dfp["Concepto"] = np.select(conditions, choice)

#%%

dfp


dfsal = df["Date"]
dfsal["Concepto"]
dfsal.to_csv("analisis_archivo.csv", sep="\t",index=False) 
print(dfsal.head())

#%%
"""
guardando csv con pandas
"""
# Saving dataframe to CSV
df.to_csv("processed_titanic.csv", index=False)
