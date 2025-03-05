# PyEatsPi - A Python Package for Estimating Pi

## Overview
Pyeatspi is a Python package that provides six different methods for estimating the mathematical constant \( \pi \), with a focus on Monte-Carlo simulation methods.

Users can easily estimate Pi using a simple function call, analyze the estimation variance, and visualize the process for some methods. The demo.ipynb file provides a detailed usage demostration.

## Installation
Clone this repository and install manually:

```sh
git clone https://github.com/yourusername/pyeatspi.git
cd pyeatspi
```

## Usage

### Basic Example
```python
import pyeatspi

# Estimate Pi using Buffon's Needle Method with 1000 samples
pi_value = piest.estimate(samples=1000, method="buffons", viz=True)
print("Estimated Pi: ", pi_value)

# Compare the variance between two methods
variances = pyeatspi.compare_variance(sample_size=10000, simulation_size=100, methods=["buffon", "laplace"])
```

### Estimate Method

The following methods are avaliable.
```python
pi = pyeatspi.estimate(samples=1000, method="mc-integral")
pi = pyeatspi.estimate(samples=5000, method="circle-ratio", viz=True)
pi = pyeatspi.estimate(samples=5000, method="drunkard", viz=True)
pi = pyeatspi.estimate(samples=5000, method="buffon", viz=True)
pi = pyeatspi.estimate(samples=5000, method="laplace")
pi = pyeatspi.estimate(samples=5000, method="chudnovsky")
```

Parameters:
- `samples` *(int)*: The number of samples to use for estimation. However, for the Chudnovsky method, samples represent the number of decimals to estimate to.
- `method` *(str)*: One of the methods provided above.
- `viz` *(bool, optional)*: Whether to visualize the process (only for `"circle-ratio"`, `"drunkard"`, and `"buffon"` methods).

### Compare_variance Method

The `compare_std` method compares the standard deviation of any combination of monte-carlo methods (Chudnovsky method excluded). A list of methods may be provided, or if left blank, all methods will be compared. The method returns a dictionary of method-standard deviation pairs.

```python
# Compare the variance between three methods
stds = pyeatspi.compare_std(sample_size=10000, simulation_size=100, methods=["buffon", "laplace", "drunkard"])

# Compare the variance of all methods
stds = pyeatspi.compare_std(sample_size=10000, simulation_size=100)
```

## Methods Explained

For a detailed explaination of all the methods, please see demo.ipynb!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by **Alex Yu**

## Acknowledgments
- Created originally for STA410: Statistical Computation course at UofT taught by [Scott Schwartz](https://github.com/pointOfive/). Many of the methods are inspired by the [course content](https://github.com/pointOfive/STA410_tenfouroverandout).
