#import required functions
from seir_model import *

def seir_RK45(t,y, beta, sigma, gamma):
    '''A function that takes in the time, the current values of the susceptible, exposed, infected and recovered populations, and the parameters beta, sigma and gamma. The function returns the rates of change of each population at that time step.'''
    s = y[0]
    e = y[1]
    i = y[2]
    r = y[3]

    dsdt = ds_dt(s, e, i, r, beta, sigma, gamma)
    dedt = de_dt(s, e, i, r, beta, sigma, gamma)
    didt = di_dt(s, e, i, r, beta, sigma, gamma)
    drdt = dr_dt(s, e, i, r, beta, sigma, gamma)

    return [dsdt,dedt,didt,drdt]
