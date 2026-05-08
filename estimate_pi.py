import gcl
import time

#Se define una función para estimar pi
def estimar_pi ( n ) :
start = time . time ()
_ , U = glc (2* n )
X = U [0::2]
Y = U [1::2]

dentro = sum (1 for i in range ( n ) if X [ i ]**2 + Y [ i ]**2 <= 1)
pi_est = 4 * dentro / n
tiempo = time . time () - start

return pi_est , dentro , tiempo

# Diferentes valores de n sobre los cuales probar la estimación del método
lanzamientos = [100 , 1000 , 10000 , 100000 , 1000000]
print ( f" Valor real : {np.pi :.10 f}\n")

for n in lanzamientos :
pi_est , dentro , t = estimar_pi ( n )
error = abs ( pi_est - np . pi )
print ( f"n={n: >7}: pi ={ pi_est :.6 f} , error ={ error :.6 f} , t={t:.3 f}s")

#Visualización de resultados
n_vis = 10000
pi_est , dentro , t = estimar_pi ( n_vis )
_ , U = glc (2* n_vis )
X = U [0::2]
Y = U [1::2]

colores = [’blue ’ if X [ i ]**2+ Y [ i ]**2 <=1 else ’red ’
for i in range ( n_vis ) ]

plt . figure ( figsize =(8 , 8) )
plt . scatter (X , Y , c = colores , s =1 , alpha =0.5)
theta = np . linspace (0 , np . pi /2 , 100)
plt . plot ( np . cos ( theta ) , np . sin ( theta ) , ’k-’, linewidth =2)
plt . xlim (0 , 1)
plt . ylim (0 , 1)
plt . xlabel (’X’)
plt . ylabel (’Y’)
plt . title ( f’Estimacion de $\\ pi$ (n={ n_vis }): $ {{\\ pi }}$={ pi_est :.4f}’)
plt . axis (’equal ’)
plt . show ()
