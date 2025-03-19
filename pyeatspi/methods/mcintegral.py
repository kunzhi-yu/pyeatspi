import random
import math

class MCIntegral:
    """
    We know \int_{1}_{0} sqrt(1 - x**2) = pi/4. So we can estimate pi by
    Monte Carlo integral estimate of the LHS of the equation.

    Inspired by HW2 part 1.
    """

    def __init__(self, sample_size, viz):
        self.sample_size = sample_size
        self.viz = viz

    def estimate(self):
        if self.viz:
            print("WARNING: Visualization is not available for Monte Carlo Integration method." + "\n" +
                  "Continuing without visualization.")

        sum = 0
        for i in range(self.sample_size):
            u = random.uniform(0, 1)
            y = math.sqrt(1 - u**2)
            sum += y
        
        pi_est = 4 * sum / self.sample_size

        return pi_est
