"""
CEASIOMpy: Conceptual Aircraft Design Software

Description : Create a set of airfoil coordinates using CST parametrization method

Input  : wl = CST weight of lower surface
         wu = CST weight of upper surface
         dz = trailing edge thickness

Output : coord = set of x-y coordinates of airfoil generated by CST

Adapted from: Kulfan_CST/kulfan_to_coord.py
              by Ryan Barrett 'ryanbarr'
              https://github.com/Ry10/Kulfan_CST

 Adapted from: Airfoil generation using CST parameterization method
               by Pramudita Satria Palar
               http://www.mathworks.com/matlabcentral/fileexchange/42239-airfoil-generation-using-cst-parameterization-method

Python version: >=3.6

| Author: Aidan Jungo
| Creation: 2021-04-26
| Last modifiction: 2021-05-11

TODO:

    *

"""

#==============================================================================
#   IMPORTS
#==============================================================================

import os
import numpy as np
from math import pi, cos, sin, factorial
import matplotlib.pylab as plt

#==============================================================================
#   CLASSES
#==============================================================================

class CST_shape(object):
    def __init__(self, wl=[-1, -1, -1], wu=[1, 1, 1], dz=0, N=200):
        self.wl = wl
        self.wu = wu
        self.dz = dz
        self.N = N
        self.x_list = []
        self.y_list = []
        self.coordinate = np.zeros(N)

    def airfoil_coor(self):
        wl = self.wl
        wu = self.wu
        dz = self.dz
        N = self.N

        # Create x coordinate
        x = np.ones((N, 1))
        y = np.zeros((N, 1))
        zeta = np.zeros((N, 1))


        for i in range(0, N):
            zeta[i] = 2 * pi / N * i
            x[i] = 0.5*(cos(zeta[i])+1)

        # N1 and N2 parameters (N1 = 0.5 and N2 = 1 for airfoil shape)
        N1 = 0.5
        N2 = 1

        center_loc = np.where(x == 0)  # Used to separate upper and lower surfaces
        center_loc = center_loc[0][0]

        xl = np.zeros(center_loc)
        xu = np.zeros(N-center_loc)

        for i in range(len(xl)):
            xl[i] = x[i]            # Lower surface x-coordinates
        for i in range(len(xu)):
            xu[i] = x[i + center_loc]   # Upper surface x-coordinates

        yl = self.__ClassShape(wl, xl, N1, N2, -dz) # Call ClassShape function to determine lower surface y-coordinates
        yu = self.__ClassShape(wu, xu, N1, N2, dz)  # Call ClassShape function to determine upper surface y-coordinates

        y = np.concatenate([yl, yu])  # Combine upper and lower y coordinates

        self.coord = [x, y]  # Combine x and y into single output

        self.x_list = x.ravel().tolist()
        self.y_list = y.ravel().tolist()

        # self.plotting()
        # self.__writeToFile(x, y)
        return self.coord

    # Function to calculate class and shape function
    def __ClassShape(self, w, x, N1, N2, dz):


        # Class function; taking input of N1 and N2
        C = np.zeros(len(x))
        for i in range(len(x)):
            C[i] = x[i]**N1*((1-x[i])**N2)

        # Shape function; using Bernstein Polynomials
        n = len(w) - 1  # Order of Bernstein polynomials

        K = np.zeros(n+1)
        for i in range(0, n+1):
            K[i] = factorial(n)/(factorial(i)*(factorial((n)-(i))))

        S = np.zeros(len(x))
        for i in range(len(x)):
            S[i] = 0
            for j in range(0, n+1):
                S[i] += w[j]*K[j]*x[i]**(j) * ((1-x[i])**(n-(j)))

        # Calculate y output
        y = np.zeros(len(x))
        for i in range(len(y)):
            y[i] = C[i] * S[i] + x[i] * dz

        return y

    def __writeToFile(self, x, y):

        basepath = os.path.dirname(os.path.realpath(__file__))
        airfoil_shape_file = basepath + os.path.sep + 'airfoil_shape.dat'

        coord_file = open(airfoil_shape_file, 'w')
        print('airfoil_shape.dat',file=coord_file)
        for i in range(len(x)):
            print('{:<10f}\t{:<10f}'.format(float(x[i]), float(y[i])),file=coord_file)
        coord_file.close()

    def airfoilToPlot(self):
        wl = self.wl
        wu = self.wu
        dz = self.dz
        N = self.N

        # Create x coordinate
        x = np.ones((N, 1))
        y = np.zeros((N, 1))
        zeta = np.zeros((N, 1))


        for i in range(0, N):
            zeta[i] = 2 * pi / N * i
            x[i] = 0.5*(cos(zeta[i])+1)

        # N1 and N2 parameters (N1 = 0.5 and N2 = 1 for airfoil shape)
        N1 = 0.5
        N2 = 1

        center_loc = np.where(x == 0)  # Used to separate upper and lower surfaces
        center_loc = center_loc[0][0]

        xl = np.zeros(center_loc)
        xu = np.zeros(N-center_loc)

        for i in range(len(xl)):
            xl[i] = x[i]            # Lower surface x-coordinates
        for i in range(len(xu)):
            xu[i] = x[i + center_loc]   # Upper surface x-coordinates

        yl = self.__ClassShape(wl, xl, N1, N2, -dz) # Call ClassShape function to determine lower surface y-coordinates
        yu = self.__ClassShape(wu, xu, N1, N2, dz)  # Call ClassShape function to determine upper surface y-coordinates

        y = np.concatenate([yl, yu])  # Combine upper and lower y coordinates

        self.coord = [x, y]  # Combine x and y into single output

        self.plotting()

    def inv_airfoil_coor(self, x):
        wl = self.wl
        wu = self.wu
        dz = self.dz
        N = self.N

        # N1 and N2 parameters (N1 = 0.5 and N2 = 1 for airfoil shape)
        N1 = 0.5
        N2 = 1

        center_loc = np.where(x == 0)  # Used to separate upper and lower surfaces
        center_loc = center_loc[0][0]

        xl = np.zeros(center_loc)
        xu = np.zeros(N-center_loc)

        for i in range(len(xl)):
            xl[i] = x[i]            # Lower surface x-coordinates
        for i in range(len(xu)):
            xu[i] = x[i + center_loc]   # Upper surface x-coordinates

        yl = self.__ClassShape(wl, xl, N1, N2, -dz) # Call ClassShape function to determine lower surface y-coordinates
        yu = self.__ClassShape(wu, xu, N1, N2, dz)  # Call ClassShape function to determine upper surface y-coordinates

        y = np.concatenate([yl, yu])  # Combine upper and lower y coordinates

        self.coord = [x, y]  # Combine x and y into single output

        # self.plotting()
        # self.__writeToFile(x, y)
        return self.coord


    def getVar(self):
        return self.wl, self.wu

    def plotting(self):
        x_coor = self.coord[0]
        y_coor = self.coord[1]
        fig7 = plt.figure()
        ax7 = plt.subplot(111)
        ax7.plot(x_coor, y_coor,'-o')
        plt.xlabel('x/c')
        plt.ylabel('y/c')
        plt.ylim(ymin=-0.75, ymax=0.75)
        ax7.spines['right'].set_visible(False)
        ax7.spines['top'].set_visible(False)
        ax7.yaxis.set_ticks_position('left')
        ax7.xaxis.set_ticks_position('bottom')
        ax7.axis('equal')
        plt.show()


#==============================================================================
#    MAIN
#==============================================================================

if __name__ == '__main__':

    print('Test run')

    # Test coef
    wu = [0.2,0.45,-0.12,1.0,-0.473528,0.95,0.14,0.38,0.11,0.38] # Upper surface
    wl = [-0.13,0.044,-0.38,0.43,-0.74,0.54,-0.51,0.10,-0.076,0.062] # Lower surface
    dz = 0.00
    N = 100

    airfoil_CST = CST_shape(wl, wu, dz, N)
    airfoil_CST.airfoil_coor()
    airfoil_CST.plotting()
