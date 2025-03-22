from .methods.buffonsneedle import BuffonsNeedle
from .methods.circleratio import CircleRatio
from .methods.laplaceneedle import LaplaceNeedle
from .methods.mcintegral import MCIntegral
from .methods.drunkard import Drunkard
from .methods.chudnovsky import Chudnovsky
from .methods.newtons import Newtons

def estimate(sample_size: int, method: str, viz = False, **kwargs):
    """
    Estimate pi using a given method and sample size, with optional visualization.
    Visualization is not supported by all methods. Detailed descriptions of each
    method can be found in its docstring or the README.

    Args:
        samples (int): The number of samples to use in the estimation.
        method (str): The method to use in the estimation.
        viz (bool): Whether to visualize the estimation process. Not avaliable
        for laplace or avg-value methods.

    Avaliable methods:
        - 'mc-integral': Monte-Carlo integration estimation.
        - 'circle-ratio': Simple Monte-Carlo sampling from points in a circle.
        - 'drukard': Markov-chain simiulation similar to 'circle-samp' method.
        - 'buffon': Uses Buffon's needle to estimate pi.
        - 'laplace': Antithetic variates extension to Buffon's needle.
        - 'chudnovsky': Exact method for calculating pi.
        - 'newtons': Newton's method for calculating pi using sin(x).

    Returns:
        float: The estimated value of pi.
    """

    methods = {"mc-integral": MCIntegral, 
               "circle-ratio": CircleRatio,
               "drunkard": Drunkard, 
               "buffon": BuffonsNeedle, 
               "laplace": LaplaceNeedle,
               "chudnovsky": Chudnovsky,
               "newtons": Newtons}

    method_key = method.lower()
    if method_key not in methods:
        raise ValueError(f"Invalid method. Must be one of {list(methods.keys())}.")
    
    estimator = methods[method_key](sample_size=sample_size, viz=viz, **kwargs)

    return estimator.estimate()