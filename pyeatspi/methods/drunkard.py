import random
from matplotlib import pyplot as plt
import numpy as np

class Drunkard:
    """
    Using the same principles as the circle-ratio method, the drunkard method
    simulates a drunkard walking randomly in a square. 
    
    1. The drunkard starts at the center of the square and takes a step in 
    a random direction. 
    2. If the drunkard 'hits the wall' of the square, they bounce off and 
    continues in a new random direction. 
    3. Check whether the drunkard's point lies within the circle.
    
    The ratio of the points inside the circle times 4 over the total 
    number of steps taken is an estimate of pi. We simulate this by creating
    a markov chain with a stationary distribution over a [-1, 1] x [-1, 1] square.
    """

    def __init__(self, sample_size, viz, step_size = 0.2):
        self.sample_size = sample_size
        self.viz = viz
        self.step_size = step_size
        # for viz
        self.xs = []
        self.ys = []
        self.inside_xs = []
        self.inside_ys = []
        self.outside_xs = []
        self.outside_ys = []

    def estimate(self):
        num_inside = 0
        x, y = 0 ,0

        for _ in range(self.sample_size):
            dx = random.uniform(-self.step_size, self.step_size)
            dy = random.uniform(-self.step_size, self.step_size)
            proposal_x = x + dx
            proposal_y = y + dy

            # only accept the move if it is inside the square
            if -1 <= proposal_x <= 1 and -1 <= proposal_y <= 1:
                x, y = proposal_x, proposal_y

            # check if the point is inside the circle
            if x**2 + y**2 <= 1:
                num_inside += 1

            # these computations are only needed for viz
            if self.viz:
                self.xs.append(x)
                self.ys.append(y)
                if x**2 + y**2 <= 1:
                    self.inside_xs.append(x)
                    self.inside_ys.append(y)
                else:
                    self.outside_xs.append(x)
                    self.outside_ys.append(y)
        
        pi_est = 4 * num_inside / self.sample_size

        if self.viz:
            return self._viz(pi_est)
        else:
            return pi_est
    

    def _viz(self, pi_est):
        # Create the plot
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_aspect('equal')
        ax.set_xlim([-1.1, 1.1])
        ax.set_ylim([-1.1, 1.1])

        # Draw the unit circle
        circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
        ax.add_artist(circle)

        # Draw the square boundary
        ax.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], 'k-', linewidth=2)

        # Set major ticks at 0.5 increments
        ax.set_xticks(np.arange(-1, 1.1, 0.5))
        ax.set_yticks(np.arange(-1, 1.1, 0.5))

        # Plot the drunkard's path
        ax.plot(self.xs, self.ys, 'grey', alpha=0.2, label="Drunkard's Path")

        # Scatter points inside and outside the circle
        ax.scatter(self.inside_xs, self.inside_ys, color='#6FAF22', s=10, label="Inside Circle")
        ax.scatter(self.outside_xs, self.outside_ys, color='#7846B4', s=10, label="Outside Circle")

        # Mark the start and end points
        ax.scatter(self.xs[0], self.ys[0], color='green', s=100, label="Start", edgecolors='black')
        ax.scatter(self.xs[-1], self.ys[-1], color='black', s=100, label="End", edgecolors='white')

        # Labels and legend
        fig.suptitle("Drunkard's Walk Path with {} steps".format(self.sample_size))
        ax.set_title(f"Estimated value of pi = {pi_est:.4f}")
        ax.legend()
        plt.show()