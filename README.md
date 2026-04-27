# SEIR Disease modelling 

This project investigates the spread of disease using two models:
    - The SEIR model as a deterministic model using both Euler and Rk45 methods
    - A Brownian analogue of the SEIR model that uses a Monte Carlo approach allowing for the introduction of spatial dynamics

The project explores how the alteration of parameters affect the determination of an outbreak as well as how fast that outbreak occurs

## Project structure

Part_1/
analysis.py             #Comparison of parameters of the deterministic model 
plots.py                #RK45 model of SEIR
RK45vsEuler_plots.py    #Plots comparing the Euler method to RK45
seir_model_RK45.py      #Creation of the RK45 model
seir_model.py           #Creation of the Euler model
simulation_RK45.py      #Simulation of the RK45 model
simulation.py           #Simulation of the Euler model

Part_2/
part2_oop.py            #File containing all the OOP code to create the model and run the simulation
run_animation.py        #Create an animation of the simulation using the OOP
run_static.py           #Create a graph of the simulation 

## Requirements

- Python
- numpy
- matplolib
- scipy

## How to run 

### Part 1 (Deterministic Model)

The simulation can be ran using the command line with the output being a graph of the simulation.

Running plots.py will give a graph of the RK45 method under default conditions which are as follows
s0 = 0.95
e0 = 0.05
i0 = 0
r0 = 0
time = 100
dt = 1
beat = 1
sigma = 1
gamma = 1

More thorough analysis can be carried out using RK45vsEuler_plots.py and analysis.py 

RK45vsEuler_plots.py will provide an output of 4 seperate graphs illustrating the populations of S,E,I,R comparing the Euler method and RK45 it is controlled by command line arguments .

- dt 
- beta
- sigma 
- gamma

analysis.py is also controlled by command line arguments.

#### Available comparisons

- compare_parameters - takes input values of beta, gamma and sigma providing two graphs one with default conditions and one with the new conditions
- compare_beta - takes input value of beta and shows 4 graphs comparing each of the populations over time 
- compare_sigma - takes input value of sigma and shows 4 graphs comparing each of the populations over time 
- compare_gamma - takes input value of gamma and shows 4 graphs comparing each of the populations over time 
- beta_range - outputs the SEIR populations over time at 10 differing beta values 
- sigma_range - outputs the SEIR populations over time at 10 differing sigma values 
- gamma_range -  outputs the SEIR populations over time at 10 differing gamma values 

##### Example use
Run multi parameter comparison:
py analysis.py --comparison compare_parameters --beta 0.5 --sigma 0.8 --gamma 0.2

Compare gamma values:
py analysis.py --comparison compare_gamma --gamma 0.4

### Part 2 (Stochastic model)

Two scripts are provided

- run_static.py 
- run_animation.py 

Both take the same arguments
- width - width of the lattice (default 100)
- height - height of the lattice (default 100)
- num_agents - number of agents on the lattice (default 250)
- s_prob - the probability the agent starts susceptible, if not they are exposed (default 0.95)
- beta - the exposure rate (default 1)
- sigma - the incubation rate (default 0.1)
- gamma - the recovery rate (default 0.005)
- steps - the number of steps the simulation will run for (default 1000)

The scripts also have additional inputs that by default are off
- alpha - reinfection rate - allows R individuals to become E again
- delta - death rate - allows infected individuals to die 
- cure_enabled - enables a cure that will be found randomly after a minimum number of time steps (Takes boolean input)
- cure_min - sets the minimum number of timesteps before the cure can be found (only relevant if cure_enabled = True)

## Model description

The deterministic model solves the SEIR differential equations using numerical methods and population numbers of each S, E, I and R are plotted at each time step

The stochastic model represents individuals as agents on a lattice. Agents move randomly interacting with each other allowing for infection to spread 

Additional features in the stochastic model include
- Reinfection
- Death
- A "Cure"
