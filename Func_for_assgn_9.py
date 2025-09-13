#Name:Roshan Yadav
#Roll No: 2311144
#Assignment_9: Finding Roots of polynomial

import math, copy


class poly():

    """This Class defines a polynomial and 
    does various operations on it."""
    
    def __init__(self,L):

        """If P(x) = sum(i=n to 0)( (a_i) * (x^i)), 
        then L is list of coefficients i.e L= [a_i]
        for all i from n to 0 (in the descending order of power) 
        where n is the degree of the polynomial"""

        if isinstance(L, list):
            D = {}
            for i in range(len(L)):
                power = len(L) - 1 - i 
                D[power] = L[i]
        else:
            # Already a dictionary
            D = L.copy()

        self.coff = D #For dictionary format: {power: coefficient} Example: {3: 1, 2: -2, 1: 0, 0: -3} represents x³ - 2x² - 3
        self.degree = max(D.keys()) if D else 0

    def comp(self,a):

        """ This function computes P(a). """

        N = self.coff
        val = 0

        for power, coeff in N.items():
            val = val + coeff * (a ** power)

        return val

    def poly_der(self,m):

        """ This Function returns the mth derivative 
        of the polynomial"""

        C = self.coff.copy()
        R = {}
        
        for power, coeff in C.items():
            if power < m:
                # This term disappears after m derivatives
                continue
            else:
                # Apply derivative m times
                new_coeff = coeff
                for j in range(m):
                    new_coeff = new_coeff * (power - j)
                R[power - m] = new_coeff
                
        return poly(R)

    def SDM(self, a):
        """ This function does synthetic division of P(x)
        by x-a where input 'a' is a root of P(x). """

        R = {}
        max_power = max(self.coff.keys())
        
        # Bring down first coefficient 
        R[max_power - 1] = self.coff[max_power]
        
        # Synthetic division loop 
        for i in range(max_power - 1, -1, -1):
            coeff = self.coff.get(i, 0)  # Get coefficient or 0 which means there is no x^i term.
            if i > 0:  # No Negative powers
                R[i - 1] = coeff + a * R[i]
        
        return poly(R) 

    def lag(self,a,e=10**-6,max_iter=100):

        """ This Function finds one root of polynomial through
        Laguerre's Method. The input 'a' is the intial guess 
        and e is the error tolerence. """

        for i in range(max_iter):
            if abs(self.comp(a)) < e:
                return a
                
            n = self.degree
            P_1 = self.poly_der(1)
            P_2 = self.poly_der(2)

            G = P_1.comp(a) / self.comp(a)
            H = G**2 - (P_2.comp(a) / self.comp(a))

            d_1 = (G + ((n-1) * (n*H - G**2))**0.5)
            d_2 = (G - ((n-1) * (n*H - G**2))**0.5)

            if abs(d_1) > abs(d_2):
                d = d_1
            else:
                d = d_2
            
            b = n / d
            a_new = a - b

            if abs(a_new - a) < e:
                return a_new
            
            a = a_new
        
        return a
            
    def root(self,a):

        """ This Function finds roots of polynomial through
        Laguerre's Method and do deflation through synthetic 
        division method. The input 'a' is the intial guess 
        and e is the error tolerence. """

        R = []
        n = self.degree
        P = poly(self.coff)

        for i in range(n):
            r = P.lag(a)
            R.append(r)
            P = P.SDM(r)
        
        return R


def pRNG(s=0.1, c=3.95, n=10000):
    '''This function is a Pseudo random number generator 
    which uses equation x(i+1) = c*x(i)*(1-x(i)), 
    where x(0)=s and c are given as input.
    Returns a list of n random numbers'''

    L = []
    L.append(s)  # x(0) = s
    
    for i in range(n-1):
        t = c * L[i] * (1 - L[i])  # x(i+1) = c*x(i)*(1-x(i))
        L.append(t)
    
    return L[n-1]
