# Autor: Julio César O. Baleon
# Fecha: 15 de junio de 2023
# Nombre: Script de python para IntEggral
# Descripcion: Script que realiza integraciones numericas y volumenes de revolucion

import eel # Paqueteria para habilitar la webApp   #

# Funciones matematicas y constante pi
from math import cos 
from math import sin as sen 
from math import tan 
from math import log 
from math import exp 
from math import pi 

eel.init('web') # Indica la ruta de los archivos de la webApp #

@eel.expose     # Expone funcion integrar() para ser llamado por javascript #
#Definimos la función para el área.
def integrar(ecuacion1, ecuacion2, lim_a, lim_b):
    #Definimos los límites (inferior y superior)
    a = eval(lim_a) 
    b = eval(lim_b)
    #Definimos el número de rectangulos (n - 1)
    n = 10001   #10000 rectangulos
    #Calculamos la base de los rectangulos (limite superior - limite inferior) / (n - 1)
    h = (b - a) / (n - 1)
    #Definimos la lista de los puntos x a integrar
    lista = [a + h * x for x in range(int(a), n)]
    #Definimos la formula de integración de área entre curvas (f(x) - g(x))
    integral = "({}) - ({})".format(ecuacion1, ecuacion2)
    #Definimos el área 
    area = 0
    #Comenzamos la integración
    for x in lista:
        area += eval(integral)*h
    #Obtenemos el resultado del área y lo redondeamos para que tenga 3 decimales
    return "Área = {}".format(round(area, 3))   # Se envia el resultado a la webApp

@eel.expose     # Expone funcion volumen() para ser llamado por javascript #

def volumen(ecuacion1, ecuacion2, lim_a, lim_b):
    #Definimos los límites (inferior y superior)
    a = eval(lim_a)
    b = eval(lim_b)
    #Definimos el número de rectangulos (n - 1)
    n = 10001   #10000 rectangulos
    #Calculamos la base de los rectangulos (limite superior - limite inferior) / (n - 1)
    h = (b - a)/(n - 1)
    #Definimos la lista de los puntos x a integrar
    lista = [a + h * x for x in range(int(a), n)]
    #Definimos la formula de integración de solidos de revolucion (f(x)**2 - g(x)**2)
    integral = "({}) ** 2 - ({}) ** 2".format(ecuacion1, ecuacion2)
    #Definimos el área
    area = 0
    #Comenzamos la integración
    for x in lista:
        area += eval(integral)*h
    #Calculamos el volumen multiplicando por pi y redondeamos para que tenga 3 decimales
    volumen = round((area * pi), 3)
    #Obtenemos el resultado del volumen
    return "Volumen = {}".format(volumen)   # Se envia el resultado a la webApp

eel.start('ordinario.html') # Inicializa la webApp #
