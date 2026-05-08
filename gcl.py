1 import numpy as np
2 import matplotlib . pyplot as plt
3
4 a = 1664525
5 c = 1013904223
6 m = 2**32 - 1
7 semilla = 1
8
9 def glc (n , x0 = semilla ) :
10 X , U = [] , []
11 x = x0
12 for i in range ( n ) :
13 x = ( a * x + c ) % m
14 X . append ( x )
15 U . append ( x / m )
16 return X , U
17
18 n = 1000
19 X , U = glc ( n )
20 print ( f" Primeros 5 valores U: {U [:5]} ")
