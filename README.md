# magnetic-field-calculator
Calculates the magnetic field in 3 dimensions starting with a current of shape and magnitude given by the user's choice.

Maxwell's equations for magnetic fields are:\
$\nabla \cdot \vec{B}=0$ and\
$\nabla \times \vec{B}= \mu_0\vec{J} + \mu_0\epsilon_0\partial_t\vec{E}$\
Which using magnetic vector potential $B=\nabla\times\vec{A}$ in coulomb gauge gives:\
$\nabla^2\vec{A}=-\mu_0\vec{J}$

**Version 1.1 ignores Electric field influence ($\partial_t\vec{E}=0$)**

Therefore:
```math
\begin{bmatrix}\nabla^2A_x\\\nabla^2A_y\\\nabla^2A_z\end{bmatrix}=\begin{bmatrix}-\mu_0J_x\\-\mu_0J_y\\-\mu_0J_z\end{bmatrix}
```
\
Using a second order finite difference formula such that:\
$\partial_x^2f=\frac{1}{12h^2}(-f_{i+2,j,k}+16f_{i+1,j,k}-30f_{i,j,k}+16f_{i-1,j,k}-f_{i-2,j,k})$\
Then:\
$\nabla^2A_x \approx \frac{1}{12h^2}(-Ax_{i+2,j,k}+16Ax_{i+1,j,k}-30Ax_{i,j,k}+16Ax_{i-1,j,k}-Ax_{i-2,j,k})$\
So:
```math
\begin{bmatrix}-Ax_{i+2,j,k}+16Ax_{i+1,j,k}-30Ax_{i,j,k}+16Ax_{i-1,j,k}-Ax_{i-2,j,k}\\-Ay_{i+2,j,k}+16Ay_{i+1,j,k}-30Ay_{i,j,k}+16Ay_{i-1,j,k}-Ay_{i-2,j,k}\\-Az_{i+2,j,k}+16Az_{i+1,j,k}-30Az_{i,j,k}+16Az_{i-1,j,k}-Az_{i-2,j,k}\end{bmatrix}=\begin{bmatrix}-12h^2\mu_0J_x\\-12h^2\mu_0J_y\\-12h^2\mu_0J_z\end{bmatrix}
```
And the solution for $\vec{A}$ at a given point:
```math
\begin{bmatrix}Ax_{i,j,k}\\Ay_{i,j,k}\\Az_{i,j,k}\end{bmatrix}=\begin{bmatrix}\frac{1}{30}(-Ax_{i+2,j,k}+16Ax_{i+1,j,k}+16Ax_{i-1,j,k}-Ax_{i-2,j,k}+12h^2\mu_0J_x)\\\frac{1}{30}(-Ay_{i+2,j,k}+16Ay_{i+1,j,k}+16Ay_{i-1,j,k}-Ay_{i-2,j,k}+12h^2\mu_0J_y)\\\frac{1}{30}(-Az_{i+2,j,k}+16Az_{i+1,j,k}+16Az_{i-1,j,k}-Az_{i-2,j,k}+12h^2\mu_0J_z)\end{bmatrix}
```
**USAGE**
1.open current density selector.py to choose your current shape and magnitude and save the resulting array\
2.import the current density array into potential calculator.py and run. Note this is a finite element algorithm and will take many iterations to produce a reasonable answer\
3. use field generator.py to compute the resulting magnetic field\
4. plot results in grapher.
