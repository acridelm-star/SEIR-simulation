from part2_oop import simulation

if __name__ == "__main__":
    sim = simulation(width = 100, height = 100, num_agents = 250, s_prob = 0.95, 
                     sigma = 0.1, beta = 1, gamma = 0.005, alpha = 0.05, delta = 0.0025, cure_enabled = True, cure_min = 200)
    sim.place_agents()
    sim.run(steps = 1000)
    sim.plot_lattice()