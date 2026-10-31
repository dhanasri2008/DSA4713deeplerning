import numpy as np
from scipy.stats import binom
p = binom.pmf(3, 5, 0.5)
print("Probability:", p)
