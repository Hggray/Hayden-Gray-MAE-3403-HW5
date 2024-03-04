# region imports
import hw5a as pta
import random as rnd
from matplotlib import pyplot as plt
# endregion

# region functions
def ffPoint(Re, rr):
    """
    This function takes Re and rr as parameters and outputs a friction factor according to the following:
    1.  if Re>4000 use Colebrook Equation
    2.  if Re<2000 use f=64/Re
    3.  else calculate a probabilistic friction factor where the distribution has a mean midway between the prediction
        of the f=64/Re and Colebrook Equations and a standard deviation of 20% of this mean
    :param Re:  the Reynolds number
    :param rr:  the relative roughness
    :return:  the friction factor
    """
    if Re >= 4000:
        """Use the colebrook equation for this reynolds number"""
        return pta.ff(Re, rr, CBEQN=True)
    if Re <= 2000:
        """Use the laminar equation for this reynolds number"""
        return pta.ff(Re, rr)
    CBff= pta.ff(Re, rr, CBEQN=True)
    #prediction of Colebrook Equation in Transition region
    Lamff= 64 / Re
    #prediction of Laminar Equation in Transition region
    mean = (CBff+Lamff)/2
    sig = 0.2*mean
    return rnd.normalvariate(mean, sig)

def PlotPoint(Re, f):
    pta.plotMoody(plotPoint=False)
    marker = '^' if 2000 < Re < 4000 else 'o'
    """Define Marker parameters for corresponding Reynolds number"""
    plt.plot(Re, f, marker=marker, markersize=10, color='red', linestyle='None')
    """Define color and size of given markers"""
    plt.show()

def main():
    Re = float(input("Enter the Reynolds number:  "))
    rr = float(input("Enter the relative roughness:  "))
    f = ffPoint(Re, rr)
    PlotPoint(Re, f)
# endregion

# region function calls
if __name__=="__main__":
    main()
# endregion