from .methods.buffonsneedle import BuffonsNeedle
from .methods.circleratio import CircleRatio
from .methods.laplaceneedle import LaplaceNeedle
from .methods.mcintegral import MCIntegral
from .methods.drunkard import Drunkard

import numpy as np

def compare_std(sample_size: int, simulation_size: int, methods: list = None):
    """
    Compare the variance of the different methods of estimating pi.

    Args:
        sample_size (int): The number of samples to use in the each estimation.
        simulation_size (int): The number of simulations to run for each method.
        methods (list): A list of the methods to compare. If None, all methods
        will be compared

    Returns:
        dict: A dictionary of the standard error of each method.
    """

    all_methods = {"mc-integral": MCIntegral, 
                   "circle-ratio": CircleRatio,
                   "drunkard": Drunkard, 
                   "buffon": BuffonsNeedle, 
                   "laplace": LaplaceNeedle}
    
    # Filter methods if a selection is provided
    if methods:
        methods_to_use = {name: all_methods[name] for name in methods if name in all_methods}
    else:
        methods_to_use = all_methods
        
    if sample_size*simulation_size > 100000:
        print("WARNING: Large sample sizes or simulation sizes may take a long time to run.")
    
    variances = {}

    for method in methods_to_use:
        estimates = np.zeros(simulation_size)
        for i in range(simulation_size):
            estimator = methods_to_use[method](sample_size=sample_size, viz=False)
            pi = estimator.estimate()
            estimates[i] = pi
        variances[method] = np.std(estimates)

    print("\nComparison of Standard Deviation for Pi Estimation Methods:")
    print("=" * 59)
    for method_name, variance in variances.items():
        print(f"{method_name:<15}  {variance:.6f}")
    
    return variances
