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

#Define colours for plotting
colours = {
    EMPTY: "white",
    S: "cornflowerblue",
    E: "orange",
    I: "green",
    R: "red"
}

#Create the agent class
class agent:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    #Method to move the agent 
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


#Create the simulation
class simulation:
    def __init__(self, width = 100, height = 100, num_agents = 250, s_prob = 0.95, e_prob = 0.05, sigma = 0.1, beta = 1, gamma = 0.005):
        self.width = width
        self.height = height
        self.lattice = np.zeros((height, width), dtype=int)
        self.num_agents = num_agents
        self.agents = []

        self.s_prob = s_prob
        self.e_prob = e_prob
        self.sigma = sigma
        self.beta = beta
        self.gamma = gamma

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

    #Method to check if an agent is infected
    def check_infected(self, agent):
        #Check if cells adjacent contain an infected agent while keeping hard wall boundary
        if agent.x > 0 and self.lattice[agent.y, agent.x - 1] == I:
            return True
        if agent.x < self.width - 1 and self.lattice[agent.y, agent.x + 1] == I:
            return True
        if agent.y > 0 and self.lattice[agent.y - 1, agent.x] == I:
            return True
        if agent.y < self.height - 1 and self.lattice[agent.y + 1, agent.x] == I:
            return True
        return False

    #Method to update the state of the agents
    def update_states(self):
        rng = np.random.default_rng()
        to_expose = []
        to_infect = []
        to_recover = []

        #Loop through the agents and determine whether they will be updated this time step, if so store in a corresponding list 
        for agent in self.agents:
            if agent.state == S and self.check_infected(agent):
                if rng.random() < self.beta:
                    to_expose.append(agent)
            elif agent.state == E:
                if rng.random() < self.sigma:
                    to_infect.append(agent)
            elif agent.state == I:
                if rng.random() < self.gamma:
                    to_recover.append(agent)
        
        #S-->E
        for agent in to_expose:
            agent.state = E
            self.lattice[agent.y, agent.x] = E
        
        #E-->I
        for agent in to_infect:
            agent.state = I
            self.lattice[agent.y, agent.x] = I
        
        #I-->R
        for agent in to_recover:
            agent.state = R
            self.lattice[agent.y, agent.x] = R



    #Method to plot the lattice
    def plot_lattice(self):
        x = [agent.x for agent in self.agents]
        y = [agent.y for agent in self.agents]
        states = [colours[agent.state] for agent in self.agents]
        
        fig, ax = plt.subplots(1,2, figsize=(14,6))
        for state, label in [(S, "Susceptible"), (E, "Exposed"), (I, "Infected"), (R, "Recovered")]:
                x = [agent.x for agent in self.agents if agent.state == state]
                y = [agent.y for agent in self.agents if agent.state == state]
                states = [colours[agent.state] for agent in self.agents if agent.state == state]

                ax[0].scatter(x, y, c = states, label = label)

        ax[0].set_xlim(0, self.width)
        ax[0].set_ylim(0, self.height)
        ax[0].set_aspect("equal", adjustable="box")

        ax[0].set_xlabel("X position")
        ax[0].set_ylabel("Y position")
        ax[0].set_title("")
        ax[0].legend(loc="center left", bbox_to_anchor=(1.02, 0.5), borderaxespad=0.0)

        plt.tight_layout()
        plt.show()

    #Method to animate the lattice
    def animate_lattice(self, steps, pause):
        fig, ax = plt.subplots(figsize=(14,7))
      
        def update(frame):
            self.move_agents()
            self.update_states()
            ax.clear()

            for state, label in [(S, "Susceptible"), (E, "Exposed"), (I, "Infected"), (R, "Recovered")]:
                x = [agent.x for agent in self.agents if agent.state == state]
                y = [agent.y for agent in self.agents if agent.state == state]
                states = [colours[agent.state] for agent in self.agents if agent.state == state]

                ax.scatter(x, y, c = states, label = label)

            ax.set_xlim(0, self.width)
            ax.set_ylim(0, self.height)
            ax.set_aspect("equal", adjustable="box")

            ax.set_xlabel("X position")
            ax.set_ylabel("Y position")
            ax.set_title("Monte Carlo simulation of an SEIR model")

            ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), borderaxespad=0.0)
            return ax,

        self.anim = FuncAnimation(fig, update, frames = steps, interval = pause*1000, blit = False)
        
        plt.show()

        
#Visualise the simulation
if __name__ == "__main__":
    sim = simulation(width = 100, height = 100, num_agents = 250)
    sim.place_agents()
    sim.animate_lattice(steps = 200, pause = 0.05)

