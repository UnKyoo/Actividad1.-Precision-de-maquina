import numpy as np
import matplotlib.pyplot as plt #Se importa la libreria para poder trabajar con gráficos.

#Ejer1-Precisión de la representación numérica         #Versión 1.01
#Autor: Mendez Cervera Gilbert Alexander    #correo: mendezgilbert222304@outlook.com

#Inicialización de variables
epsilon = 1.0 #se inicializa epsilon igual a 1.0
iteracion = 0 #contador de iteraciones
N_Iteraciones= [] #lista para almacenar el número de iteraciones
Epsilon = [] #lista para almacenar el valor de epsilon en cada iteración 

#bucle while para calcular la precisión de la maquina
while 1.0 + epsilon != 1.0: #Se verifica hasta que sumar epsilon a 1.0 no haga diferencia en la precisión
    epsilon /= 2  # Se divide epsilon por 2 en cada iteración para encontrar el menor valor representable
    iteracion = iteracion + 1  # Se incrementa el contador de iteraciones
    N_Iteraciones.append(iteracion)  # Se almacena el número de iteración
    Epsilon.append(epsilon)  # Se almacena el valor actual de epsilon
    print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")  # Se imprime la iteración y el valor de epsilon

# Creación de la gráfica
plt.figure()  # Se crea una nueva figura
plt.plot(N_Iteraciones, Epsilon, label='Precisión de máquina', marker='o')  # Se grafica la evolución de epsilon
plt.xlabel('Iteracion')  # Se etiqueta el eje X
plt.ylabel('Epsilon')  # Se etiqueta el eje Y
plt.title('Precisión de máquina')  # Se pone un título al gráfico
plt.show() # Se enseña la gráfica

# Ajuste final del valor de epsilon
epsilon *= 2  # Se multiplica por 2 para obtener el último valor significativo de epsilon antes de que fuera insignificante
print(f"Precisión de máquina: {epsilon}")  # Se imprime el valor final de la precisión de máquina