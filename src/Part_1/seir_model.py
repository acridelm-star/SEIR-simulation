
#Define the SEIR equations 
def ds_dt(s, e, i, r, beta, sigma, gamma):
    return -beta * s * i

def de_dt(s, e, i, r, beta, sigma, gamma):
    return (beta * i * s) - (sigma * e)

def di_dt(s, e, i, r, beta, sigma, gamma):
    return (sigma * e) - (gamma * i)

def dr_dt(s, e, i, r, beta, sigma, gamma):
    return gamma * i
