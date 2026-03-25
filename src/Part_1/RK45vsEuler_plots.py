import matplotlib.pyplot as plt
from simulation_RK45 import simulation_RK45
from simulation import simulation

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
    plt.savefig(f"../plots/RK45/seir_simulation_RK45_individual_improved_dt.png")
    plt.show()
    return fig

compare_RK45_Euler(0.1, 1, 1, 0.1)
