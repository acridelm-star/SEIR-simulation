#Import libraries and functions
import numpy as np
import matplotlib.pyplot as plt
from simulation import simulation

def compare_beta(beta):
    '''A function that takes a new value of beta and runs the simulation with both the original value and the new value. Four plots are then returned comparing the susceptible, exposed, infected and recovered at different values of beta.'''
    #Run the simulation and store the results
    time, s, e, i, r = simulation(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, 0.1)
    time1, s1, e1, i1, r1 = simulation(0.99, 0.01, 0, 0, 100, 0.1, beta, 1, 0.1)

    #Plot the results
    fig, ax = plt.subplots(2,2, figsize = (12,6))

    ax[0,0].plot(time, s, label = "Beta = 1")
    ax[0,0].plot(time, s1, label = f"Beta = {beta}")
    ax[0,0].set_title("Susceptible Population")
    ax[0,0].set_xlabel("Time (Days)")
    ax[0,0].set_ylabel("Population")
    ax[0,0].legend()

    ax[0,1].plot(time, e, label = "Beta = 1")
    ax[0,1].plot(time1, e1, label = f"Beta = {beta}")
    ax[0,1].set_title("Exposed Population")
    ax[0,1].set_xlabel("Time (Days)")
    ax[0,1].set_ylabel("Population")
    ax[0,1].legend()

    ax[1,0].plot(time, i, label = "Beta = 1")
    ax[1,0].plot(time1, i1, label = f"Beta = {beta}")
    ax[1,0].set_title("Infected Population")
    ax[1,0].set_xlabel("Time (Days)")
    ax[1,0].set_ylabel("Population")
    ax[1,0].legend()

    ax[1,1].plot(time, r, label = "Beta = 1")
    ax[1,1].plot(time1, r1, label = f"Beta = {beta}")
    ax[1,1].set_title("Recovered Population")
    ax[1,1].set_xlabel("Time (Days)")
    ax[1,1].set_ylabel("Population")
    ax[1,1].legend()

    plt.tight_layout()
    plt.savefig(f"../plots/beta_changes/seir_simulation_beta_{beta}.png")
    plt.show()
    return fig

def compare_sigma(sigma):
    '''A function that takes a new value of sigma and runs the simulation with both the original value and the new value. Four plots are then returned comparing the susceptible, exposed, infected and recovered at different values of sigma.'''
    #Run the simulation and store the results
    time, s, e, i, r = simulation(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, 0.1)
    time1, s1, e1, i1, r1 = simulation(0.99, 0.01, 0, 0, 100, 0.1, 1, sigma, 0.1)

    #Plot the results
    fig, ax = plt.subplots(2,2, figsize = (12,6))

    ax[0,0].plot(time, s, label = "Sigma = 1")
    ax[0,0].plot(time1, s1, label = f"Sigma = {sigma}")
    ax[0,0].set_title("Susceptible Population")
    ax[0,0].set_xlabel("Time (Days)")
    ax[0,0].set_ylabel("Population")
    ax[0,0].legend()

    ax[0,1].plot(time, e, label = "Sigma = 1")
    ax[0,1].plot(time1, e1, label = f"Sigma = {sigma}")
    ax[0,1].set_title("Exposed Population")
    ax[0,1].set_xlabel("Time (Days)")
    ax[0,1].set_ylabel("Population")
    ax[0,1].legend()

    ax[1,0].plot(time, i, label = "Sigma = 1")
    ax[1,0].plot(time1, i1, label = f"Sigma = {sigma}")
    ax[1,0].set_title("Infected Population")
    ax[1,0].set_xlabel("Time (Days)")
    ax[1,0].set_ylabel("Population")
    ax[1,0].legend()

    ax[1,1].plot(time, r, label = "Sigma = 1")
    ax[1,1].plot(time1, r1, label = f"Sigma = {sigma}")
    ax[1,1].set_title("Recovered Population")
    ax[1,1].set_xlabel("Time (Days)")
    ax[1,1].set_ylabel("Population")
    ax[1,1].legend()

    plt.tight_layout()
    plt.savefig(f"../plots/sigma_changes/seir_simulation_sigma_{sigma}.png")
    plt.show()
    return fig

def compare_gamma(gamma):
    ''''A function that takes a new value of gamma and runs the simulation with both the original value and the new value. Four plots are then returned comparing the susceptible, exposed, infected and recovered at different values of gamma.'''
    #Run the simulation and store the results
    time, s, e, i, r = simulation(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, 0.1)
    time1, s1, e1, i1, r1 = simulation(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, gamma)

    #Plot the results
    fig, ax = plt.subplots(2,2, figsize = (12,6))

    ax[0,0].plot(time, s, label = "Gamma = 0.1")
    ax[0,0].plot(time1, s1, label = f"Gamma = {gamma}")
    ax[0,0].set_title("Susceptible Population")
    ax[0,0].set_xlabel("Time (Days)")
    ax[0,0].set_ylabel("Population")
    ax[0,0].legend()

    ax[0,1].plot(time, e, label = "Gamma = 0.1")
    ax[0,1].plot(time1, e1, label = f"Gamma = {gamma}")
    ax[0,1].set_title("Exposed Population")
    ax[0,1].set_xlabel("Time (Days)")
    ax[0,1].set_ylabel("Population")
    ax[0,1].legend()

    ax[1,0].plot(time, i, label = "Gamma = 0.1")
    ax[1,0].plot(time1, i1, label = f"Gamma = {gamma}")
    ax[1,0].set_title("Infected Population")
    ax[1,0].set_xlabel("Time (Days)")
    ax[1,0].set_ylabel("Population")
    ax[1,0].legend()

    ax[1,1].plot(time, r, label = "Gamma = 0.1")
    ax[1,1].plot(time1, r1, label = f"Gamma = {gamma}")
    ax[1,1].set_title("Recovered Population")
    ax[1,1].set_xlabel("Time (Days)")
    ax[1,1].set_ylabel("Population")
    ax[1,1].legend()

    plt.tight_layout()
    plt.savefig(f"../plots/gamma_changes/seir_simulation_gamma_{gamma}.png")
    plt.show()
    return fig

def compare_parameters(beta, sigma, gamma):
    '''A function that takes the new values of beta, sigma and gamma and runs the simulation. a plot of the original values is returned alomgside a plot of the new values.'''
    
    #Run the simulation and store the results
    time, s, e, i, r = simulation(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, 0.1)
    time1, s1, e1, i1, r1 = simulation(0.99, 0.01, 0, 0, 100, 0.1, beta, sigma, gamma)

    #Plot the results
    fig, ax = plt.subplots(1,2, figsize = (14,6))

    ax[0].plot(time, s, label = "Susceptible")
    ax[0].plot(time, e, label = "Exposed")
    ax[0].plot(time, i, label = "Infected")
    ax[0].plot(time, r, label = "Recovered")
    ax[0].set_title("Original Parameters")
    ax[0].set_xlabel("Time (Days)")
    ax[0].set_ylabel("Population")
    ax[0].legend()

    ax[1].plot(time1, s1, label = "Susceptible")
    ax[1].plot(time1, e1, label = "Exposed")
    ax[1].plot(time1, i1, label = "Infected")
    ax[1].plot(time1, r1, label = "Recovered")
    ax[1].set_title("Modified Parameters")
    ax[1].set_xlabel("Time (Days)")
    ax[1].set_ylabel("Population")
    ax[1].legend()

    plt.tight_layout()
    plt.savefig(f"../plots/all_parameters/seir_simulation_parameters_{beta}_{sigma}_{gamma}.png")
    plt.show()
    return fig

compare_parameters(0.2, 1, 0.5)