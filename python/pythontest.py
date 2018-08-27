# -*- coding: utf-8 -*-
import numpy as np

n = 10
h = 1./(n+1)

x = np.linspace(0,1,n)
f = 100*np.exp(-10*x)
u = 1-(1-np.e**(-10))*x - np.exp(-10*x)

a = np.random.rand(n-1)
b = np.random.rand(n)
c = np.random.rand(n-1)

sol = h**2*f

sol_mark = np.array(n)
sol_markymark= np.array(n)
print(a)
for i in range(n-1):
    cof     = a[i]/b[i]
    a[i]   -= cof*b[i]
    b[i+1] -= cof*c[i]
print(a)
import matplotlib.pyplot as plt
plt.plot(x,u)
plt.show()