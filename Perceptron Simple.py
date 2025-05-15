import pandas as pd

lista_pesos=[0.5,0.5,0.5,0.5]
aprendizaje=0.15
umbral=0.6
cont_errores=0
ajustes=0
iteraciones=0
#-------------------------------------------------------------------------------

def importar_datos(fuente):
    dataframe=pd.read_csv(fuente)
    datos=[]
    for fila in dataframe.itertuples(index=False):
        entrada = [fila.sepal_length, fila.sepal_width, fila.petal_length, fila.petal_width]
        if fila.species=="setosa":
            salida=1 
        else:
            salida=-1
        datos.append((entrada, salida))
    return datos

lista_datos=importar_datos("iris-training.csv")

#-------------------------------------------------------------------------------

while True:
    cont_errores=0
    for lista_entradas, salida_esperada in lista_datos:
        suma=sum(entrada * peso for entrada, peso in zip(lista_entradas,lista_pesos))
        salida_obtenida=1 if suma >= umbral else -1

        
        print(f"Pesos: {lista_pesos}\tResultado: {salida_obtenida}\tSalida Esperada: {salida_esperada}")

        error=salida_esperada-salida_obtenida
        if error!=0:
            cont_errores+=1
            for i,entrada_valor in enumerate(lista_entradas):
                ajustes+=1
                lista_pesos[i] += aprendizaje * error * entrada_valor
                lista_pesos[i]=round(lista_pesos[i],3)

    iteraciones+=1            
    if cont_errores==0:
        print("\n\n\tEWNTRENAMIENTO COMPLETO\nPesos: " + str(lista_pesos))
        print("Cantidad de Errores: " + str(cont_errores) + "\nCantidad de Ajustes: " + str(ajustes) + "\nIteraciones: " + str(iteraciones))
        break
    

input("\n\tIniciar Testing?")

lista_datos=importar_datos("iris-testing.csv")

casos_fallidos=[]
for lista_entradas, salida_esperada in lista_datos:
    suma=sum(entrada * peso for entrada, peso in zip(lista_entradas,lista_pesos))
    salida_obtenida=1 if suma >= umbral else -1
    print(f"Resultado: {salida_obtenida}\tSalida Esperada: {salida_esperada}")
    
    if salida_esperada-salida_obtenida!=0:
        casos_fallidos.append(lista_entradas)


print("\n\tTESTING COMPLETADO\n")
if len(casos_fallidos)!=0:
    print("Errores de Reconocimiento:\n" + str(len(casos_fallidos)))
    for i, caso in enumerate(casos_fallidos):
        print(caso)

else:
    print("No se encontraron errores de reconocimiento :D")