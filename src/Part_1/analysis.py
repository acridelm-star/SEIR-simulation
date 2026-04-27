#Import libraries and functions
import numpy as np
import matplotlib.pyplot as plt
from simulation_RK45 import simulation_RK45
import argparse

def compare_beta(beta):
    '''A function that takes a new value of beta and runs the simulation with both the original value and the new value. Four plots are then returned comparing the susceptible, exposed, infected and recovered at different values of beta.'''
    #Run the simulation and store the results
    time, s, e, i, r = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, 0.1)
    time1, s1, e1, i1, r1 = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, beta, 1, 0.1)

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
    plt.show()
    return fig

def beta_range():
    ''''A function that creates graphs of the SEIR model for a range of beta values.'''

    beta_values = np.arange(0.1, 1.01, 0.1)
    
    fig, ax = plt.subplots(2,2, figsize = (12,8))

    for beta in beta_values:
        time, s, e, i, r = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, beta, 1, 0.1)
        beta_label = f"Beta = {beta:.1f}"

        ax[0,0].plot(time, s, label = beta_label)
        ax[0,1].plot(time, e, label = beta_label)
        ax[1,0].plot(time, i, label = beta_label)
        ax[1,1].plot(time, r, label = beta_label)

    ax[0,0].set_title("Susceptible Population")
    ax[0,0].set_xlabel("Time (Days)")
    ax[0,0].set_ylabel("Population")

    ax[0,1].set_title("Exposed Population")
    ax[0,1].set_xlabel("Time (Days)")
    ax[0,1].set_ylabel("Population")

    ax[1,0].set_title("Infected Population")
    ax[1,0].set_xlabel("Time (Days)")
    ax[1,0].set_ylabel("Population")

    ax[1,1].set_title("Recovered Population")
    ax[1,1].set_xlabel("Time (Days)")
    ax[1,1].set_ylabel("Population")
   
    plt.suptitle("SEIR for a range of Beta Values 0.1 to 1.0")
    plt.tight_layout(rect = [0, 0.07, 1, 0.95])
    handles, labels = ax[0,0].get_legend_handles_labels()
    fig.legend(handles, labels, loc = "lower center", bbox_to_anchor = (0.5, 0.015), fontsize = 11, ncol = 5)
    plt.show()
    return fig

def compare_sigma(sigma):
    '''A function that takes a new value of sigma and runs the simulation with both the original value and the new value. Four plots are then returned comparing the susceptible, exposed, infected and recovered at different values of sigma.'''
    #Run the simulation and store the results
    time, s, e, i, r = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, 0.1)
    time1, s1, e1, i1, r1 = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, 1, sigma, 0.1)

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
    plt.show()
    return fig

def sigma_range():
    '''A function that creates graphs of the SEIR model for a range of sigma values.'''

    sigma_values = np.arange(0.1, 1.01, 0.1)

    fig, ax = plt.subplots(2,2, figsize = (12,8))

    for sigma in sigma_values:
        time, s, e, i, r = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, 1, sigma, 0.1)
        sigma_label = f"Sigma = {sigma:.1f}"

        ax[0,0].plot(time, s, label = sigma_label)
        ax[0,1].plot(time, e, label = sigma_label)
        ax[1,0].plot(time, i, label = sigma_label)
        ax[1,1].plot(time, r, label = sigma_label)

    ax[0,0].set_title("Susceptible Population")
    ax[0,0].set_xlabel("Time (Days)")
    ax[0,0].set_ylabel("Population")

    ax[0,1].set_title("Exposed Population")
    ax[0,1].set_xlabel("Time (Days)")
    ax[0,1].set_ylabel("Population")

    ax[1,0].set_title("Infected Population")
    ax[1,0].set_xlabel("Time (Days)")
    ax[1,0].set_ylabel("Population")

    ax[1,1].set_title("Recovered Population")
    ax[1,1].set_xlabel("Time (Days)")
    ax[1,1].set_ylabel("Population")

    plt.suptitle("SEIR for a range of Sigma Values 0.1 to 1.0")
    plt.tight_layout(rect = [0, 0.07, 1, 0.95])
    handles, labels = ax[0,0].get_legend_handles_labels()
    fig.legend(handles, labels, loc = "lower center", bbox_to_anchor = (0.5, 0.015), fontsize = 11, ncol = 5)
    plt.show()
    return fig

def compare_gamma(gamma):
    ''''A function that takes a new value of gamma and runs the simulation with both the original value and the new value. Four plots are then returned comparing the susceptible, exposed, infected and recovered at different values of gamma.'''
    #Run the simulation and store the results
    time, s, e, i, r = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, 0.1)
    time1, s1, e1, i1, r1 = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, gamma)

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
    plt.show()
    return fig

def gamma_range():
    ''' A function that creates graphs of the SEIR model for a range of gamma values.'''

    gamma_values = np.arange(0.1, 1.01, 0.1)

    fig, ax = plt.subplots(2,2, figsize = (12,8))

    for gamma in gamma_values:
        time, s, e, i, r = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, gamma)
        gamma_label = f"Gamma = {gamma:.1f}"

        ax[0,0].plot(time, s, label = gamma_label)
        ax[0,1].plot(time, e, label = gamma_label)
        ax[1,0].plot(time, i, label = gamma_label)
        ax[1,1].plot(time, r, label = gamma_label)

    ax[0,0].set_title("Susceptible Population")
    ax[0,0].set_xlabel("Time (Days)")
    ax[0,0].set_ylabel("Population")

    ax[0,1].set_title("Exposed Population")
    ax[0,1].set_xlabel("Time (Days)")
    ax[0,1].set_ylabel("Population")

    ax[1,0].set_title("Infected Population")
    ax[1,0].set_xlabel("Time (Days)")
    ax[1,0].set_ylabel("Population")

    ax[1,1].set_title("Recovered Population")
    ax[1,1].set_xlabel("Time (Days)")
    ax[1,1].set_ylabel("Population")

    plt.suptitle("SEIR for a range of Gamma Values 0.1 to 1.0")
    plt.tight_layout(rect = [0, 0.07, 1, 0.95])
    handles, labels = ax[0,0].get_legend_handles_labels()
    fig.legend(handles, labels, loc = "lower center", bbox_to_anchor = (0.5, 0.015), fontsize = 11, ncol = 5)
    plt.show()
    return fig

def compare_parameters(beta, sigma, gamma):
    '''A function that takes the new values of beta, sigma and gamma and runs the simulation. a plot of the original values is returned alongside a plot of the new values.'''
    
    #Run the simulation and store the results
    time, s, e, i, r = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, 1, 1, 0.1)
    time1, s1, e1, i1, r1 = simulation_RK45(0.99, 0.01, 0, 0, 100, 0.1, beta, sigma, gamma)

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
    plt.show()
    return fig

#Allow for paramters to be input from the command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Run and visualise the SEIR model")

    parser.add_argument("--comparison", default = "compare_parameters",
                        choices = ["compare_parameters", "compare_beta", "compare_sigma", "compare_gamma", "beta_range", "sigma_range", "gamma_range"],
                        help = "Choose which comparison to run")

    
    #Add arguments for the parameters
    parser.add_argument("--beta", default = 1.0, type = float)
    parser.add_argument("--sigma", default = 1.0, type = float)
    parser.add_argument("--gamma", default = 0.1, type = float)

    args = parser.parse_args()

    #Parse the arguments
    if args.comparison == "compare_parameters":
        compare_parameters(args.beta, args.sigma, args.gamma)

    elif args.comparison == "compare_beta":
        compare_beta(args.beta)

    elif args.comparison == "compare_sigma":
        compare_sigma(args.sigma)

    elif args.comparison == "compare_gamma":
        compare_gamma(args.gamma)

    elif args.comparison == "beta_range":
        beta_range()

    elif args.comparison == "sigma_range":
        sigma_range()

    elif args.comparison == "gamma_range":
        gamma_range()