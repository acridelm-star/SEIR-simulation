from part2_oop import simulation


if __name__ == "__main__":
    sim = simulation(width = 100, height = 100, num_agents = 250, s_prob = 0.95, e_prob = 0.05, sigma = 0.1, beta = 1, gamma = 0.005)
    sim.place_agents()
    sim.animate_lattice(steps = 2000, pause = 0.1)