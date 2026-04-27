import matplotlib.pyplot as plt
from simulation_RK45 import simulation_RK45
from simulation import simulation
import argparse

def compare_RK45_Euler(dt, beta, sigma, gamma):

    time, s, e, i, r = simulation(0.99, 0.01, 0, 0, 100, dt, beta, sigma, gamma)
    time_RK45, s_RK45, e_RK45, i_RK45, r_RK45 = simulation_RK45(0.99, 0.01, 0, 0, 100, dt, beta, sigma, gamma)

    fig, ax = plt.subplots(2,2, figsize = (12,6))

    ax[0,0].plot(time, s, label = "Euler")
    ax[0,0].plot(time_RK45, s_RK45, label = "RK45", color = "red")
    ax[0,0].set_title("Susceptible Population")
    ax[0,0].set_xlabel("Time (Days)")
    ax[0,0].set_ylabel("Population")
    ax[0,0].legend()

    ax[0,1].plot(time, e, label = "Euler")
    ax[0,1].plot(time_RK45, e_RK45, label = "RK45", color = "red")
    ax[0,1].set_title("Exposed Population")
    ax[0,1].set_xlabel("Time (Days)")
    ax[0,1].set_ylabel("Population")
    ax[0,1].legend()

    ax[1,0].plot(time, i, label = "Euler")
    ax[1,0].plot(time_RK45, i_RK45, label = "RK45", color = "red")
    ax[1,0].set_title("Infected Population")
    ax[1,0].set_xlabel("Time (Days)")
    ax[1,0].set_ylabel("Population")
    ax[1,0].legend()

    ax[1,1].plot(time, r, label = "Euler")
    ax[1,1].plot(time_RK45, r_RK45, label = "RK45", color = "red")
    ax[1,1].set_title("Recovered Population")
    ax[1,1].set_xlabel("Time (Days)")
    ax[1,1].set_ylabel("Population")
    ax[1,1].legend()

    plt.tight_layout()
    plt.show()
    return fig

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Compare the RK45 and Euler methods for solving the SEIR model")

    #Add arguments for the parameters
    parser.add_argument("--dt", default = 0.1, type = float)
    parser.add_argument("--beta", default = 1.0, type = float)
    parser.add_argument("--sigma", default = 1.0, type = float)
    parser.add_argument("--gamma", default = 0.1, type = float)

    #Parse the arguments
    args = parser.parse_args()

    compare_RK45_Euler(args.dt, args.beta, args.sigma, args.gamma)