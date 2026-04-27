from part2_oop import simulation
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Run and animate the SEIR model")

    #Add arguments for the parameters
    parser.add_argument("--width", default = 100, type = int)
    parser.add_argument("--height", default = 100, type = int)

    parser.add_argument("--num_agents", default = 250, type = int)
    parser.add_argument("--s_prob", default = 0.95, type = float)

    parser.add_argument("--sigma", default = 0.1, type = float)
    parser.add_argument("--beta", default = 1.0, type = float)
    parser.add_argument("--gamma", default = 0.005, type = float)
    parser.add_argument("--alpha", default = 0.0, type = float)
    parser.add_argument("--delta", default = 0.0, type = float)

    parser.add_argument("--cure_min", default = 200, type = int)
    parser.add_argument("--cure_enabled", default = False, type = bool)
    
    parser.add_argument("--steps", default = 1000, type = int)
    
    args = parser.parse_args()

    sim = simulation(width = args.width, height = args.height, num_agents = args.num_agents, s_prob = args.s_prob,
                      sigma = args.sigma, beta = args.beta, gamma = args.gamma, alpha = args.alpha, delta = args.delta,
                        cure_enabled = args.cure_enabled, cure_min = args.cure_min)
    sim.place_agents()
    sim.animate_lattice(steps = args.steps, pause = 0.1)