import random
import time
from matplotlib import pyplot as plt
import math

class LaplaceNeedle:
    """
    Implements a Monte Carlo Simulation of Laplace's extension to Buffon's 
    Needle problem.
    https://en.wikipedia.org/wiki/Buffon%27s_needle_problem.

    The plane contains two sets of parallel lines orthogonal to one another, 
    creating a standard perpendicular grid. We aim to find the probability 
    that the needle intersects at least one line on the grid. Then, rearranging
    the equation, we can conduct a simiulation to estimate pi.

    This is an anthetic variates method.
    """

    def __init__(self, sample_size, viz):
        self.sample_size = sample_size
        self.viz = viz
        self.needle_length = 0.5
        self.v_spacing = 1.0
        self.h_spacing = 1.0
        self.needles = [] # for viz

    def estimate(self):
        if self.viz:
            print("WARNING: Visualization is not available for Laplace's Needle method." + "\n" +
                  "Continuing without visualization.")
        
        hits = 0 
        for i in range(self.sample_size):
            # Randomly choose the midpoint (x,y) within one grid cell.
            x = random.uniform(0, self.h_spacing)
            y = random.uniform(0, self.v_spacing)

            # Randomly choose the angle phi uniformly between -pi/2 and pi/2.
            phi = random.uniform(-math.pi/2, math.pi/2)

            # Calculate the projection distances along the x and y axes.
            proj_x = (self.needle_length / 2) * abs(math.cos(phi))
            proj_y = (self.needle_length / 2) * abs(math.sin(phi))

            # Check for vertical intersection:
            crosses_vertical = (x <= proj_x) or (x >= self.v_spacing - proj_x)

            # Check for horizontal intersection:
            crosses_horizontal = (y <= proj_y) or (y >= self.h_spacing - proj_y)

            if crosses_vertical or crosses_horizontal:
                hits += 1
            
        # Estimate pi
        if hits == 0:
            raise ValueError("No needles crossed a line. Try increasing the sample size!")

        pi_est = (self.needle_length * (2 * (self.v_spacing + self.h_spacing) - self.needle_length)) \
            / (self.v_spacing * self.h_spacing * (hits / self.sample_size))
            
        return pi_est