import random
from matplotlib import pyplot as plt

class CircleRatio:
    def __init__(self, sample_size, viz):
        self.sample_size = sample_size
        self.viz = viz
        self.inside_x = []
        self.inside_y = []
        self.outside_x = []
        self.outside_y = []
    
    def estimate(self):
        """
        Estimate pi to a given sample size using the following method.

        1. Simulate random (x, y) points in a 2-D plane with domain as a 
        square of side 2r units centered on (0,0). 
        2. Place a circle of radius r units centered on (0,0) inside the square.
        2. Calculate the ratio of number points that lie inside the circle 
        and total number of generated points.

        We know the area of a circle is pi*r^2 and the area of a square is 4*r^2.
        Therefore, the ratio of the areas is pi/4. So, we can estimate pi by
        multiplying the ratio by 4.
        """
        circle_points = 0
        
        if self.viz:
            for _ in range(self.sample_size):
                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)

                if x**2 + y**2 <= 1:
                    circle_points += 1
                    self.inside_x.append(x)
                    self.inside_y.append(y)
                else:
                    self.outside_x.append(x)
                    self.outside_y.append(y)
        else:
            for i in range(self.sample_size):
                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)

                if x**2 + y**2 <= 1:
                    circle_points += 1

        pi_est = 4 * circle_points / self.sample_size

        if self.viz:
            self._viz(pi_est)
        else:
            return pi_est
    
    def _viz(self, pi_est):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter(self.inside_x, self.inside_y, color="blue", s=5, alpha = 0.8, label="Inside circle")
        ax.scatter(self.outside_x, self.outside_y, color="red", s=5, alpha = 0.8, label="Outside circle")

        # Draw the unit circle outline
        circle = plt.Circle((0, 0), 1, color="black", fill=False, linewidth=2)
        ax.add_artist(circle)

        ax.set_aspect('equal', 'box')
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        ax.set_title(f"Estimated value of pi = {pi_est:.4f}")
        ax.legend()
        plt.show()

        return pi_est