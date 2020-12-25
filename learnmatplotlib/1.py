import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2
plt.plot(x,y2)

plt.figure(num=1111,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim(-1,2)
plt.ylim(-1,1)
plt.xlabel('x')
plt.ylabel('y')
plt.show()