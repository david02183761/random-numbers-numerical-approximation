import numpy as np
import matplotlib . pyplot as plt

#Valores escogidos para este caso
a = 1664525
c = 1013904223
m = 2**32 - 1
semilla = 1

#Definición del generador lineal congruencial
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
plt . figure ( figsize =(10 , 5) )
plt . plot ( range (1 , 101) , U [:100] , ’b-’, marker =’o’,
markersize =2 , linewidth =0.8)
plt . xlabel (’Indice n’)
plt . ylabel (’Valor de $U_n$ ’)
plt . title (’Serie de datos obtenidos ’)
plt . grid ( True , alpha =0.3)
plt . ylim (0 , 1)
plt . show ()

#Creación de las parejas ordenadas (Ui,Uj) en el cuadrado [0,1]x[0,1]
mitad = len ( U ) // 2
U1 = U [: mitad ]
U2 = U [ mitad :2* mitad ]

plt . figure ( figsize =(8 , 8) )
plt . scatter ( U1 , U2 , alpha =0.5 , s =10 , c =’blue ’)
plt . xlabel (’$U_i$ ’)
plt . ylabel (’$U_j$ ’)
plt . title (’Parejas $(U_i , U_j )$ en $ [0 ,1]**2 $’)
plt . xlim (0 , 1)
plt . ylim (0 , 1)
plt . grid ( True , alpha =0.3)
plt . show ()
