from matplotlib.pylab import *  # some of NumPy, SciPy, Matplotlib

r_samples = 2000; start_val = 0.5  # this many r values; starting values
throw_away_samples = 300; samples = 800

vals = zeros(samples-throw_away_samples)

for r in linspace(2.5, 4.0, r_samples):  # iterate r
    x = start_val
    for s in range(samples):
        x = r*x*(1-x)  # logistic map
        if(s >= throw_away_samples):
            vals[s-throw_away_samples] = x
    scatter(r*ones(samples-throw_away_samples), vals, c="k", marker="o", \
            s=0.3, linewidths=0)

xlabel("$r$"); ylabel("long-term $x$"); title("Log. map"); show();
