from matplotlib.pylab import * # some of NumPy, SciPy, Matplotlib

rVals = 2000; startVal = 0.5 # this many r values; starting values
throwAway = 300; samples = 800

vals = zeros(samples-throwAway)

for r in linspace(2.5, 4.0, rVals): # iterate r
    x = startVal 
    for s in range(samples):
        x = r*x*(1-x) # logistic map
        if(s >= throwAway):
            vals[s-throwAway] = x
    scatter(r*ones(samples-throwAway), vals, c="k", marker="o", \
            s=0.3, linewidths=0) # plot

xlabel("$r$"); ylabel("long-term $x$"); title("Log. map"); show();
