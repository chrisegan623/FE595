import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)

tan_y = np.tan(x)
plt.plot(x, tan_y)
plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])
plt.title("Sin, Cosine, and Tangent One Period")
plt.show()
