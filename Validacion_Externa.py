#validacion interna/externa aprox 16.3% de acertividad
"""
la "validacion externa aleatoria" es dividir nuestros datos en un conjunto 'train' y un conjunto 'test'
"""
import pandas as pd
from sklearn.model_selection import train_test_split #Se realiza la validacion externa de nuestros datos
from sklearn import linear_model
from sklearn.metrics import r2_score
df= pd.read_excel('Data_Sin_Outliers.xlsx')
df=df.dropna(subset=["Temperatura"]) #Elegimos la variables que tenga "valor" en la variable RESPUESTA
df=df.sample(frac=1).head(100000)
X=df[["Lluvia_Diaria","Velocidad_Viento","Direccion_Viento","Lluvia_Actual","Presion_Atmosferica","Humedad"]] #Variables REGRESORAS
Y=df["Temperatura"] #Variable  RESPUESTA
X_train, X_test, y_train, y_test= train_test_split(X, Y, test_size=.25)
#codigo para ajustar una Regresion interna donde el train y el test es el mismo ejemplo
regrINTERNA= linear_model.LinearRegression()
regrINTERNA.fit(X, Y)
prediccionesINTERNA=regrINTERNA.predict(X)
print("R2 interna",r2_score(Y,prediccionesINTERNA))
#codigo para ajustor una Regresion externa donde usaremos los objetos creados con la funcion 'train_test_split'
regrEXTERNA= linear_model.LinearRegression()
regrEXTERNA.fit(X_train, y_train)
prediccionesEXTERNA=regrEXTERNA.predict(X_test)
print("R2 externa",r2_score(y_test,prediccionesEXTERNA))
