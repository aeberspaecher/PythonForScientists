from matplotlib.pylab import *  # some of NumPy, SciPy, MPL

rVals = 2000; startVal = 0.5
throwAway = 300; samples = 800
vals = zeros(samples-throwAway)

for r in linspace(2.5, 4.0, rVals):  # iterate r
    x = startVal
    for s in range(samples):
        x = r*x*(1-x)  # logistic map
        if(s >= throwAway): vals[s-throwAway] = x
    scatter(r*ones(samples-throwAway), vals, c="k", \
            marker="o", s=0.3, lw=0)  # plot

xlabel("$r$"); ylabel("$x$"); title("Log. map"); show();
