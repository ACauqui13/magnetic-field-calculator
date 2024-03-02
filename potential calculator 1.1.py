
import numpy as np
import matplotlib.pyplot as plt




#%%
calculatednodes=np.load('C:/Users/User/Desktop/plasmas/calculatednodes.npy')
#%%
Bx=np.zeros((len(x),len(y),len(z)))
By=np.zeros((len(x),len(y),len(z)))
Bz=np.zeros((len(x),len(y),len(z)))
#%%
Ax=np.zeros((len(x),len(y),len(z)))
Ay=np.zeros((len(x),len(y),len(z)))
Az=np.zeros((len(x),len(y),len(z)))

#%% backward differences
for a in range(0,1000):
    for [i,j,k] in calculatednodes:
        axnew=1/3*(2*Ax[i-1,j,k]-Ax[i-2,j,k]+2*Ax[i,j-1,k]-Ax[i,j-2,k]+2*Ax[i,j,k-1]-Ax[i,j,k-2]-h**2*mu_0*Jx[i,j,k])
        aynew=1/3*(2*Ay[i-1,j,k]-Ay[i-2,j,k]+2*Ay[i,j-1,k]-Ay[i,j-2,k]+2*Ay[i,j,k-1]-Ay[i,j,k-2]-h**2*mu_0*Jy[i,j,k])
        aznew=1/3*(2*Az[i-1,j,k]-Az[i-2,j,k]+2*Az[i,j-1,k]-Az[i,j-2,k]+2*Az[i,j,k-1]-Az[i,j,k-2]-h**2*mu_0*Jz[i,j,k])
        tol=(abs(Ax[i,j,k]-axnew),Ay[i,j,k]-aynew,Az[i,j,k]-aznew)
        Ax[i,j,k]=axnew
        Ay[i,j,k]=aynew
        Az[i,j,k]=aznew
#%% Central difference ****
for a in range(0,1000):
    for [i,j,k] in calculatednodes:
        axnew=1/6*(Ax[i+1,j,k]+Ax[i-1,j,k]+Ax[i,j+1,k]+Ax[i,j-1,k]+Ax[i,j,k+1]+Ax[i,j,k-1]+h**2*mu_0*Jx[i,j,k])
        aynew=1/6*(Ay[i+1,j,k]+Ay[i-1,j,k]+Ay[i,j+1,k]+Ay[i,j-1,k]+Ay[i,j,k+1]+Ay[i,j,k-1]+h**2*mu_0*Jy[i,j,k])
        aznew=1/6*(Az[i+1,j,k]+Az[i-1,j,k]+Az[i,j+1,k]+Az[i,j-1,k]+Az[i,j,k+1]+Az[i,j,k-1]+h**2*mu_0*Jz[i,j,k])
        tol=(abs(Ax[i,j,k]-axnew),Ay[i,j,k]-aynew,Az[i,j,k]-aznew)
        Ax[i,j,k]=axnew
        Ay[i,j,k]=aynew
        Az[i,j,k]=aznew

#%% forward difference
for a in range(0,1000):
    for [i,j,k] in calculatednodes:
        axnew=1/3*(-Ax[i+2,j,k]+2*Ax[i+1,j,k]-Ax[i,j+2,k]+2*Ax[i,j+1,k]-Ax[i,j,k+2]+2*Ax[i,j,k+1]-h**2*mu_0*Jx[i,j,k])
        aynew=1/3*(-Ay[i+2,j,k]+2*Ay[i+1,j,k]-Ay[i,j+2,k]+2*Ay[i,j+1,k]-Ay[i,j,k+2]+2*Ay[i,j,k+1]-h**2*mu_0*Jy[i,j,k])
        aznew=1/3*(-Az[i+2,j,k]+2*Az[i+1,j,k]-Az[i,j+2,k]+2*Az[i,j+1,k]-Az[i,j,k+2]+2*Az[i,j,k+1]-h**2*mu_0*Jz[i,j,k])
        tol=(abs(Ax[i,j,k]-axnew),Ay[i,j,k]-aynew,Az[i,j,k]-aznew)
        Ax[i,j,k]=axnew
        Ay[i,j,k]=aynew
        Az[i,j,k]=aznew
        
#%% Central difference 2nd order O(h^4) <------
maxtol=1
for a in range(0,100):
    for [i,j,k] in calculatednodes:
        axnew=1/90*(-Ax[i+2,j,k]+16*Ax[i+1,j,k]+16*Ax[i-1,j,k]-Ax[i-2,j,k]-Ax[i,j+2,k]+16*Ax[i,j+1,k]+16*Ax[i,j-1,k]-Ax[i,j-2,k]-Ax[i,j,k+2]+16*Ax[i,j,k+1]+16*Ax[i,j,k-1]-Ax[i,j,k-2]+12*h**2*mu_0*Jx[i,j,k])
        aynew=1/90*(-Ay[i+2,j,k]+16*Ay[i+1,j,k]+16*Ay[i-1,j,k]-Ay[i-2,j,k]-Ay[i,j+2,k]+16*Ay[i,j+1,k]+16*Ay[i,j-1,k]-Ay[i,j-2,k]-Ay[i,j,k+2]+16*Ay[i,j,k+1]+16*Ay[i,j,k-1]-Ay[i,j,k-2]+12*h**2*mu_0*Jy[i,j,k])
        aznew=1/90*(-Az[i+2,j,k]+16*Az[i+1,j,k]+16*Az[i-1,j,k]-Az[i-2,j,k]-Az[i,j+2,k]+16*Az[i,j+1,k]+16*Az[i,j-1,k]-Az[i,j-2,k]-Az[i,j,k+2]+16*Az[i,j,k+1]+16*Az[i,j,k-1]-Az[i,j,k-2]+12*h**2*mu_0*Jz[i,j,k])
        # tol=(abs(Ax[i,j,k]-axnew),abs(Ay[i,j,k]-aynew),abs(Az[i,j,k]-aznew))
        Ax[i,j,k]=axnew
        Ay[i,j,k]=aynew
        Az[i,j,k]=aznew
        # if max(tol)<maxtol and max(tol)!=0:
            # maxtol=max(tol)
np.save('C:/Users/User/Desktop/plasmas/Ax.npy',Ax)
np.save('C:/Users/User/Desktop/plasmas/Ay.npy',Ay)
np.save('C:/Users/User/Desktop/plasmas/Az.npy',Az) 
#%% central difference 2nd order O(h^4) segmented
for a in range(0,1000):
    for i in range(35,155):
        for j in range(35,155):
            for k in range(0,198):
                Ax[i,j,k]=1/90*(-Ax[i+2,j,k]+16*Ax[i+1,j,k]+16*Ax[i-1,j,k]-Ax[i-2,j,k]-Ax[i,j+2,k]+16*Ax[i,j+1,k]+16*Ax[i,j-1,k]-Ax[i,j-2,k]-Ax[i,j,k+2]+16*Ax[i,j,k+1]+16*Ax[i,j,k-1]-Ax[i,j,k-2]+12*h**2*mu_0*Jx[i,j,k])
                Ay[i,j,k]=1/90*(-Ay[i+2,j,k]+16*Ay[i+1,j,k]+16*Ay[i-1,j,k]-Ay[i-2,j,k]-Ay[i,j+2,k]+16*Ay[i,j+1,k]+16*Ay[i,j-1,k]-Ay[i,j-2,k]-Ay[i,j,k+2]+16*Ay[i,j,k+1]+16*Ay[i,j,k-1]-Ay[i,j,k-2]+12*h**2*mu_0*Jy[i,j,k])
                Az[i,j,k]=1/90*(-Az[i+2,j,k]+16*Az[i+1,j,k]+16*Az[i-1,j,k]-Az[i-2,j,k]-Az[i,j+2,k]+16*Az[i,j+1,k]+16*Az[i,j-1,k]-Az[i,j-2,k]-Az[i,j,k+2]+16*Az[i,j,k+1]+16*Az[i,j,k-1]-Az[i,j,k-2]+12*h**2*mu_0*Jz[i,j,k])
        # if max(tol)<maxtol and max(tol)!=0:
# np.save('C:/Users/User/Desktop/plasmas/Ax.npy',Ax)
# np.save('C:/Users/User/Desktop/plasmas/Ay.npy',Ay)
# np.save('C:/Users/User/Desktop/plasmas/Az.npy',Az)        # maxtol=max(tol)
#%%
np.save('C:/Users/User/Desktop/plasmas/Ax.npy',Ax)
#%%
np.save('C:/Users/User/Desktop/plasmas/Ay.npy',Ay)
#%%
np.save('C:/Users/User/Desktop/plasmas/Az.npy',Az)
#%%
Ax=np.load('C:/Users/User/Desktop/plasmas/Ax.npy')

Ay=np.load('C:/Users/User/Desktop/plasmas/Ay.npy')

Az=np.load('C:/Users/User/Desktop/plasmas/Az.npy')
#%% B-field

for [i,j,k] in calculatednodes:
    Bx[i,j,k]=(-Az[i,j+2,k]+8*Az[i,j+1,k]-8*Az[i,j-1,k]+Az[i,j-2,k]+Ay[i,j,k+2]-8*Ay[i,j,k+1]+8*Ay[i,j,k-1]-Ay[i,j,k-2])/(12*h)
    By[i,j,k]=-(-Az[i+2,j,k]+8*Az[i+1,j,k]-8*Az[i-1,j,k]+Az[i-2,j,k]+Ax[i,j,k+2]-8*Ax[i,j,k+1]+8*Ax[i,j,k-1]-Ax[i,j,k-2])/(12*h)
    Bz[i,j,k]=(-Ay[i+2,j,k]+8*Ay[i+1,j,k]-8*Ay[i-1,j,k]+Ay[i-2,j,k]+Ax[i,j+2,k]-8*Ax[i,j+1,k]+8*Ax[i,j-1,k]-Ax[i,j-2,k])/(12*h)
    
# Bx[20:80,20,50]=0
# By[20:80,20,50]=0
# Bz[20:80,20,50]=0
np.save('C:/Users/User/Desktop/plasmas/Bx.npy',Bx)
np.save('C:/Users/User/Desktop/plasmas/By.npy',By)
np.save('C:/Users/User/Desktop/plasmas/Bz.npy',Bz) 
#%%
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
