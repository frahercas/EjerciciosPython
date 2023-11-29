#validacio interna Kfold aprox 16.5% acertividad
import pandas as pd
from sklearn.model_selection import KFold #Se realiza la validacion externa de nuestros datos
from sklearn import linear_model
from sklearn.metrics import r2_score
import numpy as np
df= pd.read_excel('Data_Sin_Outliers.xlsx')
df=df.dropna(subset=["Temperatura"]) #Elegimos la variables que tenga "valor" en la variable RESPUESTA
df=df.sample(frac=1).head(100000)
df=df.reset_index()
X=df[["Lluvia_Diaria","Velocidad_Viento","Direccion_Viento","Lluvia_Actual","Presion_Atmosferica","Humedad"]] #Variables REGRESORAS
Y=df["Temperatura"] #Variable  RESPUESTA
kf=KFold(n_splits=100,shuffle=True)
print("numero de repeticiones= ",kf.get_n_splits(X))

regr=linear_model.LinearRegression()
resultados=[]
for train_index, test_index in kf.split(X):
    X_train,X_test=X.loc[train_index,],X.loc[test_index,]
    y_train,y_test= Y[train_index],Y[test_index]
    regr.fit(X_train, y_train)
    predicciones=regr.predict(X_test)
    print("R2",r2_score(y_test,predicciones))
    resultados.append(r2_score(y_test, predicciones))

print("r2 promedio",np.mean(resultados))    

