import numpy as np
import matplotlib.pyplot as plt

X, Y, Z =  np.meshgrid(x[10:190:5],y[10:190:5],z[10:190:5],indexing='ij')

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
# ax.quiver(X, Y, Z, Ax[10:190:5,10:190:5,10:190:5], Ay[10:190:5,10:190:5,10:190:5], Az[10:190:5,10:190:5,10:190:5],length=0.5,alpha=0.6,color='red')
ax.quiver(X, Y, Z, Bx[10:190:5,10:190:5,10:190:5], By[10:190:5,10:190:5,10:190:5], Bz[10:190:5,10:190:5,10:190:5],length=0.1,alpha=0.20,color='Blue')
# ax.quiver(X, Y, Z, Jx[10:190:5,10:190:5,10:190:5], Jy[10:190:5,10:190:5,10:190:5], Jz[10:190:5,10:190:5,10:190:5],length=0.0000001,alpha=0.7,color='Black')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(elev=0,azim=50)

#%%
for angle in range(0,100,10):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')
    # ax.quiver(X, Y, Z, Ax[10:190:5:2,10:190:5:2,10:190:5:2], Ay[10:190:5:2,10:190:5:2,10:190:5:2], Az[10:190:5:2,10:190:5:2,10:190:5:2],length=10,alpha=0.6,color='red')
    ax.quiver(X, Y, Z, Bx[10:190:5,10:190:5,10:190:5], By[10:190:5,10:190:5,10:190:5], Bz[10:190:5,10:190:5,10:190:5],alpha=0.10,color='Blue',label='B-field')
    # ax.quiver(X, Y, Z, Jx[10:190:5,10:190:5,10:190:5], Jy[10:190:5,10:190:5,10:190:5], Jz[10:190:5,10:190:5,10:190:5], length=0.000001,alpha=0.2,color='Black',label='J=1000000')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.legend()
    ax.view_init(elev=angle,azim=10)
