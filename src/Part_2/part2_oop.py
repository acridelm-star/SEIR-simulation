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
D = 5

#Define colours for plotting
colours = {
    EMPTY: "white",
    S: "cornflowerblue",
    E: "orange",
    I: "green",
    R: "red",
    D: "black"
}

#Create the agent class
class agent:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.dead_frames = 0

    #Method to move the agent 
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


#Create the simulation
class simulation:
    def __init__(self, width = 100, height = 100, num_agents = 250, s_prob = 0.95, e_prob = 0.05, sigma = 0.1,
                  beta = 1, gamma = 0.005, alpha = 0.0, delta = 0.0, cure_enabled = False, cure_min = 100):
        
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
        self.alpha = alpha
        self.delta = delta

        self.current_step = 0
        self.cure_enabled = cure_enabled
        self.cure_found = False

        if self.cure_enabled:
            rng = np.random.default_rng()
            self.cure_step = rng.integers(cure_min, cure_min * 4)
        else:
            self.cure_step = None

        self.S_hist = []
        self.E_hist = []
        self.I_hist = []
        self.R_hist = []
        self.D_hist = []
        self.total_deaths = 0
        

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
            
            #Prevent dead agents from moving
            if agent.state == D:
                continue

            direction = rng.choice(["up", "down", "left", "right", "up_left", "up_right",
                                     "down_left", "down_right"])

            if direction == "up":
                self.attempt_move(agent, 0, 1)
            elif direction == "down":
                self.attempt_move(agent, 0, -1)
            elif direction == "left":
                self.attempt_move(agent, -1, 0)
            elif direction == "right":
                self.attempt_move(agent, 1, 0)
            elif direction == "up_left":
                self.attempt_move(agent, -1, 1)
            elif direction == "up_right":
                self.attempt_move(agent, 1, 1)
            elif direction == "down_left":
                self.attempt_move(agent, -1, -1)
            elif direction == "down_right":
                self.attempt_move(agent, 1, -1)

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
        
        if agent.x > 0 and agent.y > 0 and self.lattice[agent.y - 1, agent.x - 1] == I:
            return True
        if agent.x < self.width - 1 and agent.y > 0 and self.lattice[agent.y - 1, agent.x + 1] == I:
            return True
        if agent.x > 0 and agent.y < self.height - 1 and self.lattice[agent.y + 1, agent.x - 1] == I:
            return True
        if agent.x < self.width - 1 and agent.y < self.height - 1 and self.lattice[agent.y + 1, agent.x + 1] == I:
            return True
        
        return False
    
    #Method to activate the cure and reduce infection rates
    def activate_cure(self):
        self.beta = self.beta / 2
        self.alpha = self.alpha / 2
        self.delta = self.delta / 2
        self.gamma = self.gamma * 2
        self.cure_found = True
    
    #Method that checks if the cure needs to be activated
    def cure_check(self):
        if self.cure_enabled and (not self.cure_found) and self.current_step >= self.cure_step:
            self.activate_cure()

    #Method to update the state of the agents
    def update_states(self):
        rng = np.random.default_rng()
        to_expose = []
        to_infect = []
        to_recover = []
        to_reinfect = []
        to_die = []
        to_remove = []

        #Loop through the agents and determine whether they will be updated this time step, if so store in a corresponding list 
        for agent in self.agents:
            if agent.state == S and self.check_infected(agent):
                if rng.random() < self.beta:
                    to_expose.append(agent)
            elif agent.state == E:
                if rng.random() < self.sigma:
                    to_infect.append(agent)
            elif agent.state == I:
                r = rng.random()
                if r < self.gamma:
                    to_recover.append(agent)
                elif r < (self.gamma + self.delta):
                    to_die.append(agent)
            elif agent.state == R:
                if rng.random() < self.alpha and self.check_infected(agent):
                    to_reinfect.append(agent)
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

        #R-->E
        for agent in to_reinfect:
            agent.state = E
            self.lattice[agent.y, agent.x] = E

        #I-->D
        for agent in to_die:
            agent.state = D
            agent.dead_frames = 0
            self.lattice[agent.y, agent.x] = D

        self.total_deaths += len(to_die)

        #Keep dead agents visible briefly, then remove them from the lattice.
        for agent in self.agents:
            if agent.state == D:
                agent.dead_frames += 1
                if agent.dead_frames >= 10:
                    to_remove.append(agent)

        for agent in to_remove:
            self.lattice[agent.y, agent.x] = EMPTY
            self.agents.remove(agent)
            
    #Methods to count the number of agents in each state per step and record them for plotting 
    def count_states(self):
        s = 0
        e = 0
        i = 0
        r = 0
        d = 0
        for agent in self.agents:
            if agent.state == S:
                s += 1
            elif agent.state == E:
                e += 1
            elif agent.state == I:
                i += 1
            elif agent.state == R:
                r += 1
            elif agent.state == D:
                d += 1
        return s, e, i, r, d

    def record_states(self):
        s, e, i, r, d = self.count_states()
        self.S_hist.append(s)
        self.E_hist.append(e)
        self.I_hist.append(i)
        self.R_hist.append(r)
        self.D_hist.append(self.total_deaths)

    #Method to run the simulation for a given number of steps
    def run(self, steps):
            for i in range(steps):
                self.current_step += 1
                self.cure_check()
                self.move_agents()
                self.update_states()
                self.record_states()


    #Method to plot the lattice
    def plot_lattice(self):
        x = [agent.x for agent in self.agents]
        y = [agent.y for agent in self.agents]
        states = [colours[agent.state] for agent in self.agents]
        
        fig, ax = plt.subplots(1,2, figsize=(14,6))
        for state, label in [(S, "Susceptible"), (E, "Exposed"), (I, "Infected"), (R, "Recovered"), (D, "Dead")]:
                x = [agent.x for agent in self.agents if agent.state == state]
                y = [agent.y for agent in self.agents if agent.state == state]
                states = [colours[agent.state] for agent in self.agents if agent.state == state]

                ax[0].scatter(x, y, c = states, label = label)

        ax[0].set_xlim(0, self.width)
        ax[0].set_ylim(0, self.height)
        ax[0].set_aspect("equal", adjustable="box")

        ax[0].set_xlabel("X position")
        ax[0].set_ylabel("Y position")
        ax[0].set_title("Monte Carlo simulation of an SEIR model")
        ax[0].legend(loc="center left", bbox_to_anchor=(1.02, 0.5), borderaxespad=0.0)

        ax[1].plot(range(len(self.S_hist)), self.S_hist, label = "Susceptible", color = colours[S])
        ax[1].plot(range(len(self.E_hist)), self.E_hist, label = "Exposed", color = colours[E])
        ax[1].plot(range(len(self.I_hist)), self.I_hist, label = "Infected", color = colours[I])
        ax[1].plot(range(len(self.R_hist)), self.R_hist, label = "Recovered", color = colours[R])
        ax[1].plot(range(len(self.D_hist)), self.D_hist, label = "Dead", color = colours[D])

        ax[1].set_xlabel("Monte Carlo step")
        ax[1].set_ylabel("Number of Agents")
        ax[1].set_title("Monte Carlo simulation of an SEIR model")
        ax[1].legend()

        plt.tight_layout()
        plt.show()

    #Method to animate the lattice
    def animate_lattice(self, steps, pause):
        fig, ax = plt.subplots(1,2, figsize=(14,7))
      
        def update(frame):
            self.current_step += 1
            self.cure_check()
            self.move_agents()
            self.update_states()
            self.record_states()

            ax[0].clear()
            ax[1].clear()

            for state, label in [(S, "Susceptible"), (E, "Exposed"), (I, "Infected"), (R, "Recovered"), (D, "Dead")]:
                x = [agent.x for agent in self.agents if agent.state == state]
                y = [agent.y for agent in self.agents if agent.state == state]
                states = [colours[agent.state] for agent in self.agents if agent.state == state]

                ax[0].scatter(x, y, c = states, label = label)

            ax[0].set_xlim(0, self.width)
            ax[0].set_ylim(0, self.height)
            ax[0].set_aspect("equal", adjustable="box")

            ax[0].set_xlabel("X position")
            ax[0].set_ylabel("Y position")
            ax[0].set_title("Monte Carlo simulation of an SEIR model")

            ax[0].legend(loc="lower center", bbox_to_anchor=(0.5, -0.17), borderaxespad = 0.0, ncols = 5)

            num_steps = np.arange(len(self.S_hist))
            ax[1].plot(num_steps, self.S_hist, label = "Susceptible", color = colours[S])
            ax[1].plot(num_steps, self.E_hist, label = "Exposed", color = colours[E])
            ax[1].plot(num_steps, self.I_hist, label = "Infected", color = colours[I])
            ax[1].plot(num_steps, self.R_hist, label = "Recovered", color = colours[R])
            ax[1].plot(num_steps, self.D_hist, label = "Dead", color = colours[D])

            ax[1].set_xlabel("Monte Carlo step")
            ax[1].set_ylabel("Number of Agents")
            ax[1].set_title("Monte Carlo simulation of an SEIR model")
            ax[1].legend()


            return ax[0],ax[1]

        self.anim = FuncAnimation(fig, update, frames = steps, interval = pause, blit = False)
        
        plt.show()