import matplotlib . pyplot as plt
import numpy as np
from scipy import integrate
import math

t=np. linspace (0 ,1 ,100)
G =6.67430*(10**( -11) )
M= 5.9722*(10**24)
m=1
u_1 =0
u_2 =0

def model1 (X,t,G,M,m,u_1 ,u_2 ):
  x1 ,x2 ,x3 ,x4=X
  dotx1 = x2
  dotx2 = x1 *( x4)**2 - G*M*m/( x1)**2 + u_1/m
  dotx3 = x4
  dotx4 = -2* x2*x4 /( x1) + u_2 /( x1)
  return np. array ([ dotx1 , dotx2 , dotx3 , dotx4 ])

plt. figure ( figsize =(10 ,10) )
ax = plt. axes ( projection = ’polar ’)
X0 = [1/2 ,0 ,0 , math . sqrt (G*M *8)]
S = integrate . odeint (model1 ,X0 ,t, args = (G,M,m,u_1 ,u_2))
x1 = [S[i ][0] for i in range ( len(S))]
x2 = [S[i ][1] for i in range ( len(S))]
x3 = [S[i ][2] for i in range ( len(S))]
x4 = [S[i ][3] for i in range ( len(S))]

plt. plot (x3 ,x1)
