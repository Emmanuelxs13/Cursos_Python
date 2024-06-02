import numpy as np 
import time
import sys

tamaño = 1000000

print("Vector numpy")
t_vector = time.time()
vector_numpy = np.arange(tamaño, dtype="int64")

suma_vector = vector_numpy.sum()
print("Tipo de objeto: " + str(type(vector_numpy)))
print("Suma vector numpy: " + str(suma_vector))
print("Tamaño del vector: " + str(sys.getsizeof(vector_numpy)/1024))
print("Tiempo de ejecución: " + str(time.time()-t_vector))

print("--------------------------------------")

print("Lista")
t_lista = time.time()
lista =list(range(tamaño))

suma_lista = sum(lista)
print("Tipo de objeto: " + str(type(lista)))
print("Suma vector numpy: " + str(suma_lista))
print("Tamaño del lista: " + str(sys.getsizeof(lista)/1024))
print("Tiempo de ejecución: " + str(time.time()-t_lista))


#Dimensionalidad

#0D
escalar_0d = 10

#1D
vector_1d = np.array([1,2,3,4,5,6])

#2D
matriz_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])

#3D
matriz_3d = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[11,12,13], [14,15,16], [17,18,19]]])