import numpy as np
import matplotlib.pyplot as plt

x,y=map(int,input().split())
#x, y are the coordinates of the center of pressure
plt.figure(figsize=(5.2,9.2),dpi=80)
plt.scatter(x,y,s=50)
plt.xlim(-26,26)
plt.ylim(-47,47)
#plt.grid(b=True,axis='both',which='both')
plt.show()