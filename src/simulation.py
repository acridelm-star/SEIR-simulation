
#Import required libraries and functions
import numpy as np
from seir_model import *

def simulation(s0, e0, i0, r0, time, dt):
   '''Simulation of an SEIR model that takes in the initial values of the susceptible, exposed, infected, and recovered populations,
   as well as the total time of the simulation and the time step. The function returns arrays containing the values of each population at each time step.'''
   
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
      
      #Get the current calues 
      s = s_values[step - 1]
      e = e_values[step - 1]
      i = i_values[step - 1]
      r = r_values[step - 1]
      
      #Calculate the rate 
      s_rate = ds_dt(s, e, i, r)
      e_rate = de_dt(s, e, i, r)
      i_rate = di_dt(s, e, i, r)
      r_rate = dr_dt(s, e, i, r)

      #Update the values
      s_values[step] = s + (s_rate * dt)
      e_values[step] = e + (e_rate * dt)
      i_values[step] = i + (i_rate * dt)
      r_values[step] = r + (r_rate * dt)

      time_values[step] = step * dt

   return time_values, s_values, e_values, i_values, r_values