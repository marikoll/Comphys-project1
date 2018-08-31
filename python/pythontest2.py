import numpy as np

n = 10

x = np.linspace(0,1,n+2)
h = 1./(n+1)


# diagonalene i matrisen
a = np.zeros(n)-1
b = np.zeros(n)+2
c = np.zeros(n)-1

a[0]  = 0
c[-1] = 0

f = 100*np.exp(-10*x)
u = 1- (1-np.exp(-10))*x - np.exp(-10*x)

d = h**2*f
d[0]  = 0
d[-1] = 0
v = np.zeros(n)

for i in range(1,n):
	cof   = a[i]/b[i-1]
	a[i] -= cof*b[i-1]
	b[i] -= cof*c[i-1]
	d[i+1] -= cof*d[i]

for i in range(1,n):
	print(-i-1,-i)
	cof      = c[-i-1]/b[-i]
	c[-i-1] -= cof*b[-i]
	d[-i-2] -= cof*d[-i-1]

d[1:-1] = d[1:-1]/b

print(d)
import matplotlib.pyplot as plt
plt.plot(x,u,x,d)
plt.show()