import numpy as np
def expp(x):
    y = 0
    yold = 1
    n = 0
    atol = 1e-3 # tolerance
    while ( abs(y-yold) > atol ):
        yold = y
        term = ( x ** n ) / factorial(n)
        if ( n % 2 == 1 ):
            term = -term
        y += term
        n += 1
    return y
