# PyEatsPi - A Python Package for Estimating Pi

## Overview
Pyeatspi is a Python package that provides seven different methods for estimating the mathematical constant pi, with a focus on Monte-Carlo simulation methods.

Users can easily estimate Pi using a simple function call, analyze the estimation variance, and visualize the process where appropriate. The [demo file](demo.ipynb) provides a detailed usage demostration.

## Installation
Clone this repository:

```sh
git clone https://github.com/kunzhi-yu/pyeatspi.git
cd pyeatspi
```

## Usage

### Basic Example
```python
import pyeatspi

# Estimate Pi using Buffon's Needle Method with 1000 samples
pi_value = piest.estimate(samples=1000,
                          method="buffons",
                          viz=True)

print("Estimated Pi: ", pi_value)

# Compare the monte-carlo standard deviation between two methods
stds = pyeatspi.compare_std(sample_size = 10000, 
                            simulation_size = 100, 
                            methods = ["buffon", "laplace"])
print(stds)
```

### Estimate Method

The following methods are avaliable to estimate Pi. Where `viz = True`, visualization is avaliable. Other method-specific arguments are avaliable too.
```python
# Monte Carlo Methods
pi = pyeatspi.estimate(samples=1000, method="mc-integral")
pi = pyeatspi.estimate(samples=5000, method="circle-ratio", viz=True)
pi = pyeatspi.estimate(samples=5000, method="drunkard", viz=True,
                       step_size=0.2, burn_in=0)
pi = pyeatspi.estimate(samples=5000, method="buffon", viz=True)
pi = pyeatspi.estimate(samples=5000, method="laplace")

# Iterative Method
pi = pyeatspi.estimate(samples=5000, method="newtons", 
                       viz=True, inital_guess=2, tolerance=1e-6)

# Exact Method
pi = pyeatspi.estimate(samples=5000, method="chudnovsky")
```

Parameters:
- `samples` *(int)*: The number of samples to use for estimation. However, for the Chudnovsky method, samples represent the number of decimals to estimate to.
- `method` *(str)*: One of the methods provided above.
- `viz` *(bool, optional)*: Whether to visualize the process (only for `"circle-ratio"`, `"drunkard"`, `"buffon"`, and `"newtons"` methods).

### Compare_variance Method

The `compare_std` method compares the standard deviation of any combination of monte-carlo methods (Newton's and Chudnovsky methods excluded). A list of methods may be provided, or if left blank, all methods will be compared. The method returns a dictionary of method-standard deviation pairs.

```python
# Compare the variance between three methods
stds = pyeatspi.compare_std(sample_size=10000, simulation_size=100, methods=["buffon", "laplace", "drunkard"])

# Compare the variance of all methods
stds = pyeatspi.compare_std(sample_size=10000, simulation_size=100)
```

## Methods Explained

For a detailed explaination of all the methods, please see [demo.ipynb](demo.ipynb)!

## Author
Developed by **Alex Yu**

## Acknowledgments
- Created originally for STA410: Statistical Computation course at UofT taught by [Scott Schwartz](https://github.com/pointOfive/). Many of the methods are inspired by the [course content](https://github.com/pointOfive/STA410_tenfouroverandout).
