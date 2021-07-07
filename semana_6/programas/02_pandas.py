"""
Trabajando con Pandas
"""

# In[]
# Importando la libreria pandas
import pandas as pd

# In[]
# creación de una serie de pandas desde una lista
a = [1, 7, 2]

b = pd.Series(a)

print(b)

# In[]
# retorno del primer valor
print(b[0])

# In[]
# agregando etiquetas
a = [1, 7, 2]

mivar = pd.Series(a, index = ["x", "y", "z"])

print(mivar)


# In[]
# usando un diccionario
calorias = {"day1": 420, "day2": 380, "day3": 390}

c = pd.Series(calorias)

print(c)

# si se quiere usar solo algunos del diccionario, se coloca con los index

# In[]
# creando un dataframe
datos = {
  "calorias": [420, 380, 390],
  "duracion": [50, 40, 45]
}

d = pd.DataFrame(datos)

print(d)

# In[]
# para obtener la primera fila se usa
print(d.loc[0])

# In[]
#busca por cabecera
print(d.loc[:,"calorias"])

# In[]
# busca una lista de índices
print(d.loc[[0, 1]])

# In[]
# leer columna
print(d.iloc[:,0]) # primera columna

# In[]
# Lee desde CSV a un Pandas DataFrame
df = pd.read_csv("titanic.csv", header=0)

# In[]
# Muestra los primeros 5 items
print(df.head())

"""Características: 
* pclass: clase del tripulante
* name: nombre completo del pasajero
* sex: género
* age: edad
* sibsp: # Número de hermanos/cónyuge a bordo
* parch: número de padres/hijos a bordo
* fare: costo del ticket
* survived: survial metric (0 - died, 1 - survived)

"""
# In[]
# muestra los últimos 5 items
print(df.tail(10))

# In[]
# para imprimir el dataframe completo
print(df.to_string()) 
# In[]
"""
# Análisis exploratorio

Uso de Pandas para explorar los datos
"""
# Describe las características
print(df.describe())

# In[]
df.info()

# In[]
# gráfica
df["Fare"].plot()

#plt.show()

# In[]
# Histogramas
df["Age"].hist()

# In[]
# Unique values
print(df["Sex"].unique())

# In[]
# Seleccionando datos por característica
df["Name"].head()

# In[]
# Filtrado
print(df[df["Sex"]=="female"].head(20)) # solo las mujeres aparecen

# In[]
# Sorting
df.sort_values("Age", ascending=False).head()

# In[]
# Grouping
survived_group = df.groupby("Survived")
survived_group.mean()

# In[]
# Seleccionando fila
df.iloc[0, :] # iloc obtiene filas (o columnas) en una posición en particular en el 
# índice (solo valores enteros)

# In[]
# Seleccionando un valor en especifico
df.iloc[0, 1]

# In[]
# Seleccionando por índice
df.loc[0] # loc obtiene filas (o columnas) con una etiqueta en particular
#desde el índice

# In[]
"""# Preprocessing"""

# Rows with at least one NaN value
df[pd.isnull(df).any(axis=1)].head()

# In[]
# Drop rows with Nan values
df = df.dropna() # removes rows with any NaN values
df = df.reset_index() # reset's row indexes in case any rows were dropped
df.head()

# In[]
# Dropping multiple columns
df = df.drop(["Name", "Sex"], axis=1) # we won't use text features for our initial basic models
df.head()

# In[]
# Map feature values
df['Sex'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
df.head()

# In[]
"""# Feature engineering"""

# Lambda expressions to create new features
def get_family_size(sibsp, parch):
    family_size = sibsp + parch
    return family_size

# In[]
df["family_size"] = df[["Sibsp", "Parch"]].apply(lambda x: get_family_size(x["Sibsp"], x["Parch"]), axis=1)
df.head()

# In[]
# Reorganize headers
df = df[['Pclass', 'Sex', 'Age', 'Sibsp', 'Parch', 'family_size', 'Fare', 
         'Survived']]
df.head()

# In[]
"""# Saving data"""

# Saving dataframe to CSV
df.to_csv("processed_titanic.csv", index=False)
