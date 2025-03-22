import random
import math
import numpy as np
import matplotlib.pyplot as plt

class Newtons:
    """
    Estimate the value of pi using Newton's method.

    The function uses the fact that sin(pi) = 0, so finding a 
    root of sin(x) near the initial guess will give an approximation of pi.
    """

    def __init__(self, sample_size, viz, inital_guess = 2.0, tolerance = 1e-6):
        self.sample_size = sample_size
        self.viz = viz
        self.inital_guess = inital_guess
        self.tolerance = tolerance

    def estimate(self):
        if self.inital_guess >= 6*math.pi or self.inital_guess <= math.pi/2:
            raise ValueError("Initial guess must be between pi/2 and 6*pi.")

        x = self.inital_guess
        iterations = [x]
        for i in range(self.sample_size):
            fx = math.sin(x)
            dfx = math.cos(x)

            if abs(fx) < self.tolerance:
                break

            x = x - fx / dfx
            iterations.append(x)
        
        if self.viz:
            return self._viz(x, iterations)
        else:
            return x
        
    def _viz(self, pi_est, iterations):
        # Generate a range of x values covering the area of interest
        x_vals = np.linspace(0, 4*math.pi, 4000)
        y_sin = np.sin(x_vals)
        y_cos = np.cos(x_vals)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_sin, label='sin(x)', color='#6FAF22')
        plt.plot(x_vals, y_cos, label='cos(x)', color='#7846B4', alpha = 0.5)
        
        # Compute the function values at the iteration points for sin(x)
        iter_y = [math.sin(x) for x in iterations]
        
        # Plot iteration points and connect them with a dotted line
        plt.plot(iterations, iter_y, 'ko', label='Iteration Points')
        plt.plot(iterations, iter_y, 'k--', label='Newton Path', alpha = 0.2)
        
        # Highlight the final and inital estimates with a larger marker
        plt.plot(iterations[-1], math.sin(iterations[-1]), 'ko', markersize=10, label='Final Estimate')
        plt.plot(iterations[0], math.sin(iterations[0]), 'go', markersize=10, label='Initial Guess')
        
        plt.xlabel('x')
        plt.ylabel('Function value')
        plt.suptitle("Newton's Method with {} Iterations".format(len(iterations)))
        plt.title(f"Estimated value of pi = {pi_est:.4f}")        
        plt.legend()
        plt.grid(True)
        plt.show()