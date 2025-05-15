import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("iris.csv")

colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

for species in df["species"].unique():
    subset = df[df['species'] == species]
    ax.scatter(

            #COMENTAR UNO DE LOS ATRIBUTOS
        subset['sepal_length'],
        subset["sepal_width"],
        subset['petal_length'], 
        #subset['petal_width'],

        color=colors[species], 
        label=species,
        s=60, 
        alpha=0.7,
        edgecolors='k'
    )

# Etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Visualización 3D del conjunto de datos Iris')

# Mostrar leyenda y gráfico
ax.legend(title='Species')
plt.show()