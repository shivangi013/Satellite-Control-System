import matplotlib . pyplot as plt
import sympy as sp
import numpy as np
from scipy . optimize import curve_fit
from scipy import integrate

def Linear_System (x_0 ,x_1 ,t_1 ):
  t_0 = 0
  
  A = sp. Matrix ([[0 ,1 ,0 ,0] ,[3 ,0 ,0 ,2] ,[0 ,0 ,0 ,1] ,[0 , -2 ,0 ,0]])
  B = sp. Matrix ([[0 ,0] ,[1 ,0] ,[0 ,0] ,[0 ,1]])
  
  AT = sp. transpose (A)
  BT = sp. transpose (B)
  
  t,z,s =sp. symbols (’t z s ’)
  
  M = sp.exp(A*(t-z))
  M=M. subs (sp.exp(sp.I*(-t+z)) + sp.exp(-sp.I*(-t+z)), 2* sp.cos(-t+z))
  M=M. subs (sp.I*sp.exp(sp.I*(-t+z)) - sp.I*sp.exp(-sp.I*(-t+z)), -2* sp.sin(-t+z))
  M=M. subs ( -3* sp.exp(sp.I*(-t+z))/2 - 3* sp.exp(-sp.I*(-t+z))/2, -3* sp.cos(-t+z))
  M=M. subs ( -3* sp.I*sp.exp(sp.I*(-t+z))/2 + 3* sp.I*sp.exp(-sp.I*(-t+z))/2, 3* sp.sin(-t+z))
  M=M. subs (+ sp.exp(sp.I*(-t+z))/2 + sp.exp(-sp.I*(-t+z))/2, sp.cos(t-z))
  M=M. subs (-sp.I*sp.exp(sp.I*(-t+z))/2 + sp.I*sp.exp(-sp.I*(-t+z))/2, -sp.sin(t-z))
  M=M. subs (2* sp.I*sp.exp(sp.I*(-t+z)) - 2* sp.I*sp.exp(-sp.I*(-t+z)), 4* sp.sin(t-z))
  M=M. subs (3* sp.I*sp.exp(sp.I*(-t+z)) - 3* sp.I*sp.exp(-sp.I*(-t+z)), 6* sp.sin(t-z))
  M=M. subs (3* sp.exp(sp.I*(-t+z)) + 3* sp.exp(-sp.I*(-t+z)), 6* sp.cos(t-z))
  M=M. subs (2* sp.exp(sp.I*(-t+z)) + 2* sp.exp(-sp.I*(-t+z)), 4* sp.cos(t-z))
  M=M. simplify ()
  
  N = sp. transpose (M)
  f1 = M. subs (t, t_1)*B*BT*N. subs (t, t_1)
  W = sp. integrate (f1 ,(z,t_0 ,t_1))
  
  W=W. subs (sp.sin(t_1) ,(sp.sin(t_1)). evalf ())
  W=W. subs (sp.cos(t_1) ,(sp.cos(t_1)). evalf ())
  w=W. subs (sp.sin(t_1)**2 ,( sp.sin(t_1) **2) . evalf ())
  W=W. subs (sp.cos(t_1)**2 ,( sp.cos(t_1) **2) . evalf ())
  
  R = W.inv ()
  Q=BT*N. subs (t,t_1)
  Dummy_M = M. subs (z,t_0 )
  S = (x_1 - Dummy_M . subs (t,t_1)*x_0)
  u = Q*R*S
  U = u. subs (z,s)
  f2 = M. subs (z,s)*B*U
  x = sp. integrate (f2 ,(s,t_0 ,t))
  X_ = M. subs (z, t_0)* x_0 + x
  
  lam_x1 = sp. lambdify (t, X_ [0] , modules =[’ numpy ’])
  lam_x2 = sp. lambdify (t, X_ [1] , modules =[’ numpy ’])
  lam_x3 = sp. lambdify (t, X_ [2] , modules =[’ numpy ’])
  lam_x4 = sp. lambdify (t, X_ [3] , modules =[’ numpy ’])
  
  z_vals = np. linspace (0, t_1 , 100)
  x1_vals = lam_x1 ( z_vals )
  x2_vals = lam_x2 ( z_vals )
  x3_vals = lam_x3 ( z_vals )
  x4_vals = lam_x4 ( z_vals )
  
  plt. plot ( z_vals , x1_vals , label =" x1 ")
  plt. plot (z_vals , x2_vals , label =" x2 ")
  plt. plot (z_vals , x3_vals , label =" x3 ")
  plt. plot ( z_vals , x4_vals , label =" x4 ")
  plt. legend ()

def Controller (x_0 ,x_1 ,t_1 ):
  Linear_System (x_0 ,x_1 ,t_1)
  lam_u1 = sp. lambdify (z, u[0] , modules =[’ numpy ’])
  lam_u2 = sp. lambdify (z, u[1] , modules =[’ numpy ’])
  
  z_vals = np. linspace (0, 100 , 10000)
  u1_vals = lam_u1 ( z_vals )
  u2_vals = lam_u2 ( z_vals )
  
  ax = plt. axes ()
  plt. plot (z_vals , u1_vals , label =" u1 ")
  plt. plot (z_vals , u2_vals , label =" u2 ")
  plt. legend ()

x_0 = sp. Matrix ([1 , -1 ,0 ,1])
x_1 = sp. Matrix ([100 ,85 , -90 ,46])
t_1 = 100
