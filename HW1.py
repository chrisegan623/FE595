import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.1)   # start,stop,step

def graph(x,sin,cos,tan):
    plt.plot(x,sin,x,cos,x,tan)
    plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])
    plt.title("Sin, Cosine, and Tangent One Period")
    plt.show()


if __name__ == '__main__':
    graph(x,np.sin(x),np.cos(x),np.tan(x))
