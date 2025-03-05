import decimal

class Chudnovsky:
    """
    Implements Chudnovsky algorithm for calculating pi to a given number of 
    decimal places. Chudnovsky is an exact method, so sample_size arg is used
    to specify the number of decimal places to calculate pi to.
    """

    def __init__(self, sample_size, viz):
        self.sample_size = sample_size
        self.viz = viz

    def estimate(self):
        print("Calculating pi using Chudnovsky method to " + str(self.sample_size) 
              + " decimal places.")
        if self.viz:
            print("WARNING: Visualization is not available for Chudnovsky method." + "\n" +
                  "Continuing without visualization.")
        if self.sample_size > 100000:
            print("Decimal places past 100,000 not recommended.")

        # initalize k to 0
        k = 0

        # Intialize number of decimal places
        decimal.getcontext().prec = self.sample_size

        return self.num()/self.den(k)
        
    def fact(self, n):
        """Basic recursive factorial calculation.
        Not recommended for large n, but ok under 1 million."""
        if n == 0:
            return 1
        else:
            return n * self.fact(n - 1)

    def den(self, k):
        """Calculates the deonminator of the Chudnovsky algorithm."""
        a = decimal.Decimal(self.fact(6*k)*(545140134*k+13591409))
        b = decimal.Decimal(self.fact(3*k)*(self.fact(k)**3)*((-262537412640768000)**k))
        res = a / b
        if k > 0:
            return res + self.den(k - 1)
        else:
            return res

    def num(self):
        """Calculates the numerator of the Chudnovsky algorithm.
        root_precision is the number of significant digits to use when 
        calculating the root."""
        p = decimal.getcontext().prec

        # Update the percision
        decimal.getcontext().prec = self.sample_size
        decimal.getcontext().prec = p

        return 426880 * decimal.Decimal(10005).sqrt()
