import random
from matplotlib import pyplot as plt
import math

class BuffonsNeedle:
    """
    Implements a Monte Carlo Simulation of Buffon's Needle problem, which 
    can estimate the value of pi. See
    https://en.wikipedia.org/wiki/Buffon%27s_needle_problem.

    In the words of Buffon: Suppose we have a floor made of parallel 
    strips of wood, each the same width, and we drop a needle onto the
    floor. What is the probability that the needle will lie across a 
    line between two strips?
    """

    def __init__(self, sample_size, viz):
        self.sample_size = sample_size
        self.viz = viz
        self.needle_length = 0.5
        self.line_spacing = 1.0
        self.needles = [] # for viz

    
    def estimate(self):
        hits = 0

        for i in range(self.sample_size):
            # Generate random number starting point
            x = random.uniform(0, 4)
            theta = random.uniform(0, math.pi)

            # Compute needle end point
            x_end = x + (self.needle_length / 2) * math.sin(theta)
            x_start = x - (self.needle_length / 2) * math.sin(theta)
            
            # Check if it crosses a line
            if math.floor(x_start / self.line_spacing) != math.floor(x_end / self.line_spacing):
                hits += 1
                crossed = True
            else:
                crossed = False

            # These computations are only needed for viz
            if self.viz:
                y = random.uniform(0, 4)
                y_start = y - (self.needle_length / 2) * math.cos(theta)
                y_end = y + (self.needle_length / 2) * math.cos(theta)
                # Add the needle to the list for viz
                self.needles.append((x_start, x_end, y_start, y_end, crossed))

        if hits == 0:
            raise ValueError("No needles crossed a line. Try increasing the sample size!")
        
        # Estimate Pi
        pi_est = (2 * self.needle_length * self.sample_size) / (self.line_spacing * hits)

        if self.viz:
            self._viz(pi_est)
        else:
            return pi_est


    def _viz(self, pi_est):
        fig, ax = plt.subplots(figsize=(8, 6))

        # Draw vertical lines
        for i in range(int(4 / self.line_spacing) + 1):
            ax.axvline(i * self.line_spacing, color="black", linestyle="--", alpha=0.6)

        # Plot each needle
        for x_start, x_end, y_start, y_end, crossed in self.needles:
            color = "#7846B4" if crossed else "#6FAF22"
            ax.plot([x_start, x_end], [y_start, y_end], color=color, lw=2)

        # Label the plot
        fig.suptitle('Buffon\'s Needle Simulation with {} samples'.format(self.sample_size))
        ax.set_title(f"Estimated value of pi = {pi_est:.4f}")
        ax.set_xlabel("X Position")
        ax.set_ylabel("Y Position")
        plt.show()
