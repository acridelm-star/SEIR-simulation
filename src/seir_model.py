beta = 1
sigma = 1
gamma = 0.1

def ds_dt(s, e, i, r):
    return -beta * s * i

def de_dt(s, e, i, r):
    return (beta * i * s) - (sigma * e)

def di_dt(s, e, i, r):
    return (sigma * e) - (gamma * i)

def dr_dt(s, e, i, r):
    return gamma * i
