PrimerLista=["Mariano","orion","ramirillo","nova","juan","antonio","carlos"]
print(PrimerLista[:])  #Esta notacíon imprime todos los elementos que contiene la lista
print(PrimerLista[2]) #Accede a un elemento en especifico de la lista poniendo el indice entre las llaves
print(PrimerLista[0:4]) #porciones de lsita, excluye el elemnto del segundo indice
print(PrimerLista[2:6]) #Porciones de lista

PrimerLista.append("Panchito") #con .append se pueden agregar elementos a la lista pero solo al final de la lista
print(PrimerLista[:])

PrimerLista.insert(3,"Margarita") #Con .insert se insertan elementos en la lista en algun indice en especifico
print(PrimerLista[:])

PrimerLista.extend(["flor","Angelica","Madelein"])   #con .extend concatenamos otra lista a la ya existente
print(PrimerLista[:])

NumeroIndex= PrimerLista.index("nova")  #Podemos saber el ndice de un elemento especifico de la lista
print("En el indice numero:",NumeroIndex,"se encuentra el elemento",PrimerLista[NumeroIndex])

print("jorge" in PrimerLista) #Verifica si un elemento se encuentra o  no en una lista devuelve true o false

Segundalista=["Moro", 3.14165, False, 24] #Las listas en Python pueden almacenar diferentes tipos de datos
Segundalista.extend(["baldore",2.54])
print(Segundalista[:])

Segundalista.remove("baldore")  #Elimina algun elemento en especifico de la lista
print(Segundalista[:])

Segundalista.pop()  #Con .pop podemos eliminar el ultimo elemento de la lista
print(Segundalista[:])

Tercerlista=PrimerLista+Segundalista # el operador suma en listas sirve para concatenar listas
print(Tercerlista[:])

Listacuatro=["julio", 33, True]*3 #el operador de multiplicaion sirve como repetidor en una lista
print(Listacuatro[:])
