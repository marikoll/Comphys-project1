# -*- coding: utf-8 -*-
import numpy as np

n = 10

h = 1./(n+1)

x = np.linspace(0,1,n)
f = 100*np.exp(-10*x)
u = 1-(1-np.e**(-10))*x - np.exp(-10*x)
# matrise A i Av = d. A er tridiagonal matrise
a = np.zeros(n)-1 #np.random.rand(n-1) # under diagonalen
b = np.zeros(n)+2 #np.random.rand(n)   # diagonal
c = np.zeros(n)-1 #np.random.rand(n-1) # over diagonalen 

a[0]  = 0
c[-1] = 0

d = h**2*f # d i Av = d
print(d)

for i in range(1,n): # første steg i gausisk eliminasjon. renser a
    print(i)
    cof   = a[i]/b[i-1]
    a[i] -= cof*b[i-1]
    print(a[i])
    b[i] -= cof*c[i-1]
    d[i] -= cof*d[i-1]
    

    
for i in range(n-1): # neste steg i gausisk eliminasjon
    cof      = c[-1-i]/b[-1-i]
    c[-1-i] -= cof*b[-1-i]
    d[-2-i] -= cof*d[-1-i]
    
#d[0]  = 0
#d[-1] = 0

import matplotlib.pyplot as plt
plt.plot(x,u,x,d/b)
plt.show()