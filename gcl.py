import numpy as np
import matplotlib . pyplot as plt

#Valores escogidos para este caso
a = 1664525
c = 1013904223
m = 2**32 - 1
semilla = 1

#definición del generador lineal congruencial
def glc (n , x0 = semilla ) :
X , U = [] , []
x = x0
for i in range ( n ) :
x = ( a * x + c ) % m
X . append ( x )
U . append ( x / m )
return X , U

#Número de números pseudoaleatorios generados
n = 1000
X , U = glc ( n )
print ( f" Primeros 5 valores U: {U [:5]} ")

#Gráfica de la serie
1 plt . figure ( figsize =(10 , 5) )
2 plt . plot ( range (1 , 101) , U [:100] , ’b-’, marker =’o’,
3 markersize =2 , linewidth =0.8)
4 plt . xlabel (’Indice n’)
5 plt . ylabel (’Valor de $U_n$ ’)
6 plt . title (’Serie de datos obtenidos ’)
7 plt . grid ( True , alpha =0.3)
8 plt . ylim (0 , 1)
9 plt . show ()
