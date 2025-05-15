import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("iris.csv")

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

color_variable = df['petal_length']

sc = ax.scatter(
    df['sepal_length'],
    df["sepal_width"],
    df['petal_length'],
    c=color_variable,           
    cmap='viridis',             
    s=60,
    alpha=0.8,
    edgecolors='k'
)

cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Petal Length')

ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
ax.set_title('Grafico de dimensiones de Petalo y Sepalo de flor Iris')

plt.show()
