import numpy as np
from scipy.optimize import curve_fit
from matplotlib.pyplot import plot, show, legend

x, yExp = np.loadtxt("func.dat", unpack=True)
plot(x, yExp, ls="--", c="blue", lw="1.5", label="Exp.")

def fitFunc(x, a, b, c):
    return a*np.exp(-b*x) + c

pOpt, pCov = curve_fit(fitFunc, x, yExp)
yFit = fitFunc(x, a=pOpt[0], b=pOpt[1], c=pOpt[2])
plot(x, yFit, label="Fit: $a = %s; b = %s; c= %s$"\
     %(pOpt[0], pOpt[1], pOpt[2]), ls="-", lw="1.5", c="r")
legend(); show()
