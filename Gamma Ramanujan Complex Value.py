import cmath 
import math  
import numpy as np
from scipy.integrate import quad 
from matplotlib.pylab import plt
epsilon = 10**-12
def f(x):
	return (float)(np.sqrt(3/2 * np.log(x)+1))/np.pi
x = 369.8396749279
print((float)(np.sqrt(3/2 * np.log(x)+1)))