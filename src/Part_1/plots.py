
#Import libraries and functions
import numpy as np
import matplotlib.pyplot as plt
from simulation_RK45 import simulation_RK45

#Run the simulation and store the results
time, s, e, i, r = simulation_RK45(0.95, 0.05, 0, 0, 100, 1, 1, 1, 0.1)

#Plot the results
fig, ax = plt.subplots()
ax.plot(time, s, label = "Susceptible")
ax.plot(time, e, label = "Exposed")
ax.plot(time, i, label = "Infected")
ax.plot(time, r, label = "Recovered")

#Format the graph
ax.set_xlabel("Time (Days)")
ax.set_ylabel("Population")
ax.legend()
plt.title("SEIR Model Simulation")

plt.show()