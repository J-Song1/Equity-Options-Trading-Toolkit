"""
1 month	2.184%	+27.0 bp	+215.4 bp					19 Aug
2 months	2.552%	+34.7 bp	n.a.					19 Aug
3 months	2.689%	+17.9 bp	+232.9 bp					19 Aug
6 months	3.135%	+12.5 bp	+248.7 bp					19 Aug
1 year	3.259%	+5.2 bp	+226.1 bp		96.84	-0.05 %	-2.19 %	19 Aug
2 years	3.242%	+0.3 bp	+177.2 bp		93.82	0.00 %	-3.40 %	19 Aug
3 years	3.272%	+3.4 bp	+159.4 bp		90.79	-0.10 %	-4.56 %	19 Aug
5 years	3.098%	-5.5 bp	+127.9 bp		85.85	+0.27 %	-6.05 %	19 Aug
7 years	3.055%	-7.4 bp	+114.3 bp		81.01	+0.51 %	-7.50 %	19 Aug
10 years	2.976%	-4.3 bp	+104.9 bp		74.58	+0.42 %	-9.73 %	19 Aug
20 years	3.447%	+1.0 bp	+114.4 bp		50.78	-0.18 %	-19.93 %	19 Aug
30 years	3.217%
"""

# As of 6:45PM Aug 19, 2022
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


US_RATES = [
    # (0, 0),
    (1/12, 2.184),
    (2/12, 2.552),
    (3/12, 2.689),
    (6/12, 3.135),
    (1, 3.259),
    (2, 3.242),
    (3, 3.272),
    (5, 3.098),
    (7, 3.055),
    (10, 2.976),
    (20, 3.447),
    (30, 3.217)
]

def get_rate(maturity, region='us'):
    """
    Uses Cubic-Spline Interpolation
    """
    assert region in ['us'] and 0 <= maturity

    maturities, rates = zip(*US_RATES)
    # maturity_range = np.linspace(0, 30, 360)

    yield_curve_cs = CubicSpline(maturities, rates)

    return yield_curve_cs(maturity)


def debug():
    tenors, rates = zip(*US_RATES[:-2]) # Excluding 20Y and 30Y
    tenor_domain = np.linspace(0, 10, 120)

    yield_curve_cs = CubicSpline(tenors, rates)
    plt.plot(tenor_domain, yield_curve_cs(tenor_domain), 'k-')
    plt.plot(tenors, rates, 'ro')
    
    print(yield_curve_cs(0.5))
    print(yield_curve_cs(0.75))
    plt.show()




    pass


if __name__ == '__main__':
    print(get_rate(0))
    #debug()
