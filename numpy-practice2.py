import numpy as np
x = np.zeros((2,3), dtype=int)
#print(x)


y =  np.ones((4,5), dtype=float)
#print(y)


z = np.ones((4,5,3), dtype=int)
print(z)


a =  np.arange(10)
print(a)



b =  np.arange(5,15)
print(b)


c = np.arange(2,20,3)
print(c)


d =  np.arange(2,3, 0.1)
print(d)


e = np.linspace(1., 4., 6)
print(e)

f = np.full((2, 2), 8)
print(f)


g = np.eye(5)
print(g)

h = np.random.random((4, 5))
print(h)