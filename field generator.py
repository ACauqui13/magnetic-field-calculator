#%%
Ax=np.load('your filepath.npy')
Ay=np.load('your filepath.npy')
Az=np.load('your filepath.npy')
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
