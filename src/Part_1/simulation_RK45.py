import numpy as np
from seir_model_RK45 import *
from scipy.integrate import solve_ivp

def simulation_RK45(s0, e0, i0, r0, time, dt, beta, sigma, gamma):
    '''Simulation of an SEIR model using the Runge-Kutta 4th order method. It takes in the initial values of the susceptible, exposed, infected, and recovered populations,
    as well as the total time of the simulation and the time step. The function returns arrays containing the values of each population at each time step.'''
    
    time_arr = np.arange(0, time, dt)
    timespan = (0, time)
    y = [s0, e0, i0, r0]
    

    def f(t, y):
        return seir_RK45(t, y, beta, sigma, gamma)
    
    solution = solve_ivp(f, timespan, y, method = "RK45", t_eval = time_arr)

    s_values = solution.y[0]
    e_values = solution.y[1]
    i_values = solution.y[2]
    r_values = solution.y[3]
    return solution.t, s_values, e_values, i_values, r_values