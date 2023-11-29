import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LinearRegression
import numpy as np

def cargar_datos():
    df = pd.read_excel('variables_meteorologicas.xlsx')
    # Filtrar filas con valores no nulos en la variable objetivo
    df = df.dropna(subset=["Lluvia_Diaria"])
    # Seleccionar aleatoriamente 100,000 filas
    df = df.sample(frac=1).head(100000)
    return df.reset_index()

def ajustar_modelo(X_train, y_train):
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    return regr

def main():
   
    df = cargar_datos() # Cargar datos

    # Definir variables
    X = df[["Temperatura",  "Presion_Atmosferica", "Humedad"]]
    Y = df["Lluvia_Diaria"]

    # Inicializar resultados
    resultados = []

    # Validación Cruzada Leave-One-Out (LOO)
    loo = LeaveOneOut()
    for train_index, test_index in loo.split(X):
        X_train, X_test = X.loc[train_index, ], X.loc[test_index, ]
        y_train, y_test = Y[train_index], Y[test_index]

        # Ajustar modelo
        modelo = ajustar_modelo(X_train, y_train)

        # Realizar predicciones
        predicciones = modelo.predict(X_test)

        # Calcular y almacenar el error cuadrático
        error_cuadratico = (y_test - predicciones[0])**2
        resultados.append(error_cuadratico)

        print("ERROR: ", error_cuadratico)

    # Calcular el error promedio
    error_promedio = np.mean(resultados)
    print("ERROR PROMEDIO: ", error_promedio)

if __name__ == "__main__":
    main()


