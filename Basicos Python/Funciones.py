#FUNCIONES SIN PARAMETROS
def funcionMensaje(): # Definicion de la funcion
    print("linea de funcion 1")
    print("linea de funcion 2")  #Cuerpo de la funcion
    print("linea de funcion 3")

nombre= "francisco"

funcionMensaje() #llamado ala funcion
funcionMensaje()
print("el nombre del programador es:",nombre, "y el tipo de variable es:",type(nombre)) #puede haber lineas de codigo intermedias entre cada llamado de funcion
funcionMensaje() #una funcion puede ser llamada las veces que sea necesaria
    
#FUNCIONES CON PARAMETROS
def suma(nombre,num1,num2):
 print("hola",nombre,"El resultado de la suma es:",num1+num2)


suma("daniel",10,30)
suma("Francisco",3,15)


def resta(num1,num2):
    resultado=num1-num2
    return resultado
resultado_resta= resta(24,7)
print("El rsultado de la resta es:",resultado_resta)
