import numpy as np
import matplotlib.pyplot as plt
h=0.05
mu_0=1.2e-5
x = np.arange(0,10,h)
y = np.arange(0,10,h)
z=np.arange(0,10,h)     #Choose spatial configuration here, and spacestep (h)
allnodes=[]
for i in range(1,len(x)-2):
    for j in range(1,len(y)-2):
        for k in range(1,len(z)-2):
            calculatednodes.append([i,j,k])
np.save('your filepath',allnodes)                 #Creates a grid in space, saves it as a numpy array
allnodes=np.load('your filepath here') 

Jx=np.zeros((len(x),len(y),len(z)))
Jy=np.zeros((len(x),len(y),len(z)))       #creation of the spatial array which will contain currents
Jz=np.zeros((len(x),len(y),len(z)))

#as an example here is a multi coil setup, aligned with the z-axis, with a central current flowing though

Jz[50:150,50:150,:]=3000
Jz[60:140,60:140,:]=60000
Jz[70:130,70:130,:]=500000
Jz[80:120,80:120,:]=800000
Jz[90:110,90:110,:]=1000000
Jz[98:102,98:102,:]=8000000

Jx[50:150,48:52,98:102]=10000000
Jx[50:150,148:152,98:102]=-10000000
Jy[48:52,50:150,98:102]=-10000000
Jy[148:152,50:150,98:102]=10000000

Jx[50:150,48:52,68:72]=10000000
Jx[50:150,148:152,68:72]=-10000000
Jy[48:52,50:150,68:72]=-10000000
Jy[148:152,50:150,68:72]=10000000

Jx[50:150,48:52,128:132]=10000000
Jx[50:150,148:152,128:132]=-10000000
Jy[48:52,50:150,128:132]=-10000000
Jy[148:152,50:150,128:132]=10000000

Jx[50:150,48:52,158:162]=20000000
Jx[50:150,148:152,158:162]=-20000000
Jy[48:52,50:150,158:162]=-20000000
Jy[148:152,50:150,158:162]=20000000

Jx[70:130,68:72,188:192]=20000000
Jx[70:130,128:132,188:192]=-20000000
Jy[68:72,70:130,188:192]=-20000000
Jy[128:132,70:130,188:192]=20000000

Jx[90:110,88:92,191:195]=20000000
Jx[90:110,108:112,191:195]=-20000000
Jy[88:92,90:110,191:195]=-20000000
Jy[108:112,90:110,191:195]=20000000

Jx[70:130,68:72,8:12]=20000000
Jx[70:130,128:132,8:12]=-20000000
Jy[68:72,70:130,8:12]=-20000000
Jy[128:132,70:130,8:12]=20000000

Jx[90:110,88:92,5:10]=20000000
Jx[90:110,108:112,5:10]=-20000000
Jy[88:92,90:110,5:10]=-20000000
Jy[108:112,90:110,5:10]=20000000

Jx[50:150,48:52,38:42]=20000000
Jx[50:150,148:152,38:42]=-20000000
Jy[48:52,50:150,38:42]=-20000000
Jy[148:152,50:150,38:42]=20000000

np.save('your filepath here',Jx)
np.save('your filepath here',Jy)
np.save('your filepath here',Jz)
