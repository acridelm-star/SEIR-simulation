#import libraries
import numpy as np
import matplotlib.pyplot as plt

#Define state in lattice
EMPTY = 0
S = 1
E = 2
I = 3
R = 4

#Create the agent class
class agent:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.time_in_state = 0

    #Method to move the agent 
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


#Create the simulation
class simulation:
    def __init__(self, width = 100, height = 100, num_agents = 250):
        self.width = width
        self.height = height
        self.lattice = np.zeros((height, width))
        self.num_agents = num_agents
        self.agents = []

    #Method to randomly place agents on the lattice
    def place_agents(self):
        rng = np.random.default_rng()
        placed = 0
        
        while placed <self.num_agents:
            x = rng.integers(0, self.width)
            y = rng.integers(0, self.height)

            #Only place an agent if the cell is empty 
            if self.lattice[y, x] == EMPTY:
                self.lattice[y, x] = S
                self.agents.append(agent(x, y, S))
                placed += 1

    #Method to plot the lattice
    def plot_lattice(self):
        x = [agent.x for agent in self.agents]
        y = [agent.y for agent in self.agents]
        states = [agent.state for agent in self.agents]
        
        fig, ax = plt.subplots(1,2, figsize=(14,6))
        ax[0].scatter(x, y)

        ax[0].set_xlim(0, self.width)
        ax[0].set_ylim(0, self.height)
        ax[0].set_aspect("equal", adjustable="box")

        ax[0].set_xlabel("X position")
        ax[0].set_ylabel("Y position")
        ax[0].set_title("")

        plt.show()

#Visualise the simulation
if __name__ == "__main__":
    sim = simulation(width=100, height=100, num_agents=250)
    sim.place_agents()
    sim.plot_lattice()