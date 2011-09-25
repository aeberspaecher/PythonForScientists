# functions:
def f(x, a=1.0, b=2.0):
    """Return a/x and a/x^b.
    """

    return a/x**b

# somewhere else:
a = 5
y1, y2 = f(x, 5.0)
y3, y4 = f(2, b=3.0)
