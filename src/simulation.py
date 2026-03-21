#Import required libraries and functions
import numpy as np
from seir_model import *


#Define initial values
s0 = 0.99
e0 = 0.01
i0 = 0
r0 = 0

time = 100
dt = 1
time_steps = int(time/dt)

#Create arrays to store the values at each time step
s_values = np.zeros(time_steps)
e_values = np.zeros(time_steps)
i_values = np.zeros(time_steps)
r_values = np.zeros(time_steps)
time_values = np.zeros(time_steps)

#Update the arrays to contain the intial values
s_values[0] = s0
e_values[0] = e0
i_values[0] = i0
r_values[0] = r0
time_values[0] = 0

#Create a loop that simulates each time step
for step in range(1,time_steps):
   s = s_values[step - 1]
   e = e_values[step - 1]
   i = i_values[step - 1]
   r = r_values[step - 1]
   
   s_rate = ds_dt(s, e, i, r)
   e_rate = de_dt(s, e, i, r)
   i_rate = di_dt(s, e, i, r)
   r_rate = dr_dt(s, e, i, r)

   s_values[step] = s + (s_rate * dt)
   e_values[step] = e + (e_rate * dt)
   i_values[step] = i + (i_rate * dt)
   r_values[step] = r + (r_rate * dt)

   time_values[step] = step * dt

print(s_values[:5])
print(i_values[:5])