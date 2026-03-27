#import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    def __init__(self, width = 100, height = 100, num_agents = 250, s_prob = 0.95, e_prob = 0.05, sigma = 0.1):
        self.width = width
        self.height = height
        self.lattice = np.zeros((height, width), dtype=int)
        self.num_agents = num_agents
        self.agents = []

        self.s_prob = s_prob
        self.e_prob = e_prob
        self.sigma = sigma


    #Method to randomly place agents on the lattice
    def place_agents(self):
        rng = np.random.default_rng()
        placed = 0
        
        while placed < self.num_agents:
            x = rng.integers(0, self.width)
            y = rng.integers(0, self.height)

            #Only place an agent if the cell is empty 
            if self.lattice[y, x] == EMPTY:
                
                #Determine whether S or E
                if rng.random() < self.s_prob:
                    state = S
                else:
                    state = E
                self.lattice[y, x] = state
                self.agents.append(agent(x, y, state))
                
                placed += 1
    
    #Method to see if an agent can move
    def attempt_move(self, agent, dx, dy):
        new_x = agent.x + dx
        new_y = agent.y + dy

        #Hard wall check - if coordinates are out of the lattice bounds, return False
        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
            return False
        
        #Check if the new cell is empty 
        if self.lattice[new_y, new_x] != EMPTY:
            return False
        elif self.lattice[new_y, new_x] == EMPTY:
            self.lattice[agent.y, agent.x] = EMPTY
            agent.move(dx, dy)
            self.lattice[agent.y, agent.x] = agent.state
            return True
    
    #Method to move the agents randomly if they are able to move 
    def move_agents(self):
        rng = np.random.default_rng()

        for agent in self.agents:

            direction = rng.choice(["up", "down", "left", "right"])

            if direction == "up":
                self.attempt_move(agent, 0, 1)
            elif direction == "down":
                self.attempt_move(agent, 0, -1)
            elif direction == "left":
                self.attempt_move(agent, -1, 0)
            elif direction == "right":
                self.attempt_move(agent, 1, 0)

    #Method to plot the lattice
    def plot_lattice(self):
        x = [agent.x for agent in self.agents]
        y = [agent.y for agent in self.agents]
        states = [agent.state for agent in self.agents]
        
        fig, ax = plt.subplots(1,2, figsize=(14,6))
        ax[0].scatter(x, y, c = states)

        ax[0].set_xlim(0, self.width)
        ax[0].set_ylim(0, self.height)
        ax[0].set_aspect("equal", adjustable="box")

        ax[0].set_xlabel("X position")
        ax[0].set_ylabel("Y position")
        ax[0].set_title("")

        plt.show()

    #Method to animate the lattice
    def animate_lattice(self, steps, pause):
       
        fig, ax = plt.subplots(figsize=(7,7))

        x = [agent.x for agent in self.agents]
        y = [agent.y for agent in self.agents]
        states = [agent.state for agent in self.agents]

        ax.scatter(x, y, c = states)

        
        def update(frame):
            self.move_agents()

            x = [agent.x for agent in self.agents]
            y = [agent.y for agent in self.agents]
            states = [agent.state for agent in self.agents]
            ax.clear()
            ax.scatter(x, y, c = states)

            ax.set_xlim(0, self.width)
            ax.set_ylim(0, self.height)
            ax.set_aspect("equal", adjustable="box")

            ax.set_xlabel("X position")
            ax.set_ylabel("Y position")
            ax.set_title("Monte Carlo simulation of an SEIR model")

            return ax,

        self.anim = FuncAnimation(fig, update, frames = steps, interval = pause*1000, blit = False)
        
        plt.show()

        
#Visualise the simulation
if __name__ == "__main__":
    sim = simulation(width = 100, height = 100, num_agents = 250)
    sim.place_agents()
    sim.animate_lattice(steps = 200, pause = 0.05)

